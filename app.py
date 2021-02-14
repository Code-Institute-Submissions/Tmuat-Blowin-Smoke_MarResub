import os
import math
from datetime import date, datetime
import random
from flask import (
    Flask,
    flash,
    render_template,
    redirect,
    request,
    session,
    url_for
)
from flask_pymongo import PyMongo
from functools import wraps
from bson.objectid import ObjectId
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


def login_required(f):
    """login_required: \n
    * This function creates a decorator to check if a user is logged in \n
    * It performs 2 checks, if 'user' is in the session and secondly,
        if the session user is registered in the database. \n
    * It performs 2 checks to ensure the user is checked server side
        and not simply rely on the session. \n
    \n
    \n Returns: \n
    * If the user is logged in and recognised, it allows the user to
        access the view \n
    * If the user is not recognised or logged in, they are redirected
        to the login page \n
    \n
    \n Reference: \n
    * https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            user = None
        else:
            user = mongo.db.users.find_one(
                {"username": session["user"].lower()})
        if not user:
            flash("User not recognised!", "error")
            return redirect(url_for('login'))
        elif "user" not in session:
            flash("You must be logged in for this view", "error")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def is_admin(f):
    """is_admin: \n
    * This function creates a decorator to check if a user is logged in and
        also if the user is a registered admin. \n
    * It performs a number of checks, if 'user' is in the session, 
        if the session user is registered in the database. If these are true,
        it moves on to check if the user is an admin and then if admin
        is in the session variables. \n
    * It checks server side by accessing the database instead of relying
        solely on the session variables. \n
    \n
    \n Returns: \n
    * If the user is logged in, recognised and an admin, it allows 
        the user to access the view they were trying to access. \n
    * If the user is not recognised or logged in, they are redirected
        to the home page with a toast appearing. \n
    * If the user is recognised but they aren't a recognised admin it
        also redirects them to the home page with a toast. \n
    \n
    \n Reference: \n
    * https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user") is None:
            user = None
        else:
            user = mongo.db.users.find_one(
                {"username": session["user"].lower()})
        if not user:
            flash("User not recognised!", "error")
            return redirect(url_for('index'))
        elif user["admin"].lower() == "false":
            flash("This page is for admin only!", "error")
            return redirect(url_for('index'))
        elif "admin" not in session:
            flash("This page is for admin only!", "error")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


def anonymous_required(f):
    """is_admin: \n
    * This function creates a decorator to check if the visitor is
        not logged in. Such as accessing the login view once logged in. \n
    * It performs the opposite of the logged in function, checking to
        see if 'User' is in the session variables. \n
    \n
    \n Returns: \n
    * If the user is not logged in it allows them access to the view
        they were trying to access. \n
    * If the user is in the session, they are redirected to the home 
        page with a toast appearing. \n
    \n
    \n Reference: \n
    * https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" in session:
            flash("That page is only for unauthenticated users."
                  " Please logout if you wish to access this.", "error")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    """index: \n
    * This function renders the sites home page (index.html). \n
    * It accesses MongoDB to get a random choice of a single quote to display
        on page load and passes this to the template as 'quote'. \n
    * It accesses MongoDB to get a list of recipes in the database. \n
    * It checks the length of the recipe list to ensure it is more than seven;
        if it is less than seven it sets a the length as the sample. If over
        six it defaults to six to be sampled for the home page. \n
    * It passes the sample of six or less recipes to the template
        as 'recipes' \n
    * It accesses MongoDB to get a list of products in the database. \n
    * It checks the length of the product list to ensure it is more than seven;
        if it is less than seven it sets a the length as the sample. If over
        six it defaults to six to be sampled for the home page. \n
    * It passes the sample of six or less product to the template
        as 'products' \n
    \n
    \n Returns: \n
    * It returns 'index.html' \n
    * It returns a single quote \n
    * It returns a sample of recipes \n
    * It returns a sample of products \n
    """

    single_quote = random.choice(list(mongo.db.quotes.find()))

    recipe_list = list(mongo.db.recipes.find())

    product_list = list(mongo.db.products.find())

    if len(recipe_list) < 7:
        sample = len(recipe_list)
    else:
        sample = 6

    if len(product_list) < 7:
        sample_products = len(product_list)
    else:
        sample_products = 6

    recipes = random.sample(recipe_list, k=sample)

    products = random.sample(product_list, k=sample_products)

    context = {
        "quote": single_quote,
        "recipes": recipes,
        "products": products
    }
    return render_template("index.html", **context)


@app.route("/recipes")
def recipes():
    """recipes: \n
    * This function renders the recipes page (recipes.html). \n
    * It sets a limit of products to be displayed per page (9). \n
    * It checks if either 'q' for a search query or 'category' for a category
        filter are in the request arguements to filter the queryset from
        MongoDB. \n
    * If a search query or category are in the args, it
        adjusts the filters sent to MongoDB prior to pagination. \n
    * It gets the total length of the MongoDB queryset based on the
        filters or if there aren't any filters. This part of the pagination
        is a known bug as this produces two database queries (original query
        & the filtered query). The total recipes returned are passed to the
        template as 'total_recipes'. \n
    * It gets the filtered queryset to be passed to the template as
        'recipes'. \n
    * From the current page, offset and any filters or search queries
        it calulates strings for next and previous paginated pages. \n
    * It accesses MongoDB to get all the recipe categories to be
        used as filters. They are passed to the template as 'categories'. \n
    \n
    \n Returns: \n
    * It returns 'recipes.html' \n
    * It returns all recipes or filtered recipes \n
    * It returns all recipe categories \n
    * It returns an integer of the total length of the recipe list \n
    * It returns the filter or query if there was one \n
    * It returns the pagination info of next_url, prev_url and page.
    \n
    \n Reference: \n
    * Pagination code - https://www.youtube.com/watch?v=Lnt6JqtzM7I

    """
    # Number of items to be displayed per page
    limit = 9

    # Checks if 'category' in request arguements, if not sets a default
    if 'category' in request.args:
        category = request.args.get('category')
    else:
        category = None

    # Checks if 'q' in request arguements, if not sets a default
    if 'q' in request.args:
        search_key = request.args.get('q')
    else:
        search_key = None

    # Gets the filtered lists or by default all recipes. It then checks
    # if the len is == 0 to avoid server errors if it doesn't exist.
    if category:
        all_recipes = list(mongo.db.recipes.find(
            {"category": category}).sort("_id", -1))
        if len(all_recipes) == 0:
            flash("No '{}' category exists!".format(
                category.capitalize()), "error")
            return redirect(url_for("recipes"))
    elif search_key:
        all_recipes = list(mongo.db.recipes.find(
            {"$text": {"$search": search_key}}).sort("_id", -1))
        if len(all_recipes) == 0:
            flash("No match for '{}'".format(
                search_key.capitalize()), "error")
            return redirect(url_for("recipes"))
    else:
        all_recipes = list(mongo.db.recipes.find().sort("_id", -1))

    # Gets the length of the list being sent to the template
    total_recipes = len(all_recipes)

    # Setting the offset of the queryset dependent on current page
    # from request args. Defensive programming to ensure the user
    # can't force a page out of the queryset range
    if 'page' in request.args:
        if int(request.args['page']) <= 1:
            page = 1
            offset = 0
            redirect(url_for("recipes"))
        elif ((int(request.args['page']) * limit) - limit) > total_recipes:
            page = math.ceil((total_recipes/limit))
            offset = limit * (page - 1)
            flash("Page out of range", "error")
        else:
            page = int(request.args['page'])
            offset = limit * (page - 1)
    else:
        page = 1
        offset = 0

    # Getting the last id to with the offset being passed in
    last_id = all_recipes[offset]["_id"]

    # Getting the filtered queryset including the offset using 'lte'
    # It then uses the set page limit (9) to get the page recipes.
    if category:
        query = {"$and": [{"category": category}, {'_id': {'$lte': last_id}}]}
        display_recipes = list(
            mongo.db.recipes.find(query).sort("_id", -1).limit(limit))
    elif search_key:
        query = {"$and": [
            {"$text": {"$search": search_key}}, {'_id': {'$lte': last_id}}]}
        display_recipes = list(
            mongo.db.recipes.find(query).sort("_id", -1).limit(limit))
    else:
        display_recipes = list(
            mongo.db.recipes.find(
                {'_id': {'$lte': last_id}}).sort("_id", -1).limit(limit))

    # Getting the next & prev url dependent on which parameters are in 
    # the request arguements.
    if search_key:
        if offset + limit >= total_recipes:
            next_url = None
        else:
            next_url = "?page=" + str(page + 1) + "&q=" + str(search_key)
        if offset == 0:
            prev_url = None
        else:
            prev_url = "?page=" + str(page - 1) + "&q=" + str(search_key)
    elif category:
        if offset + limit >= total_recipes:
            next_url = None
        else:
            next_url = "?page=" + str(page + 1) + "&category=" + str(category)
        if offset == 0:
            prev_url = None
        else:
            prev_url = "?page=" + str(page - 1) + "&category=" + str(category)
    else:
        if offset + limit >= total_recipes:
            next_url = None
        else:
            next_url = "?page=" + str(page + 1)
        if offset == 0:
            prev_url = None
        else:
            prev_url = "?page=" + str(page - 1)

    # Getting categories to be used for filters
    categories = list(mongo.db.categories.find().sort("category", 1))

    context = {
        "recipes": display_recipes,
        "categories": categories,
        "results": total_recipes,
        "filter": category,
        "query": search_key,
        "next": next_url,
        "prev": prev_url,
        "page": page
    }
    return render_template("recipes.html", **context)


@app.route("/products")
def products():
    """
    A function to render a page of all products, with options
    to filter and search.

    This code allows pagination of results
    Code from https://www.youtube.com/watch?v=Lnt6JqtzM7I
    """
    # Number of items per page
    limit = 6

    if 'category' in request.args:
        category = request.args.get('category')
    else:
        category = None

    # Getting the total number of products
    if category:
        all_products = list(mongo.db.products.find(
            {"category": category}).sort("_id", -1))
        if len(all_products) == 0:
            flash("No '{}' category exists!".format(
                category.capitalize()), "error")
            return redirect(url_for("products"))
    else:
        all_products = list(mongo.db.products.find().sort("_id", -1))

    total_products = len(all_products)

    # Getting the offset (page number)
    if 'page' in request.args:
        if int(request.args['page']) <= 1:
            page = 1
            offset = 0
            redirect(url_for("products"))
        elif ((int(request.args['page']) * limit) - limit) > total_products:
            page = math.ceil((total_products/limit))
            offset = limit * (page - 1)
            flash("Page out of range", "error")
        else:
            page = int(request.args['page'])
            offset = limit * (page - 1)
    else:
        page = 1
        offset = 0

    # Getting the last id to with the offset used
    last_id = all_products[offset]["_id"]

    # Getting the first id in the filtered queryset
    if category:
        query = {"$and": [{"category": category}, {'_id': {'$lte': last_id}}]}
        products = list(
            mongo.db.products.find(query).sort("_id", -1).limit(limit))
    else:
        products = list(
            mongo.db.products.find(
                {'_id': {'$lte': last_id}}).sort("_id", -1).limit(limit))

    # Getting the next & prev url
    if category:
        if offset + limit >= total_products:
            next_url = None
        else:
            next_url = "?page=" + str(page + 1) + "&category=" + str(category)
        if offset == 0:
            prev_url = None
        else:
            prev_url = "?page=" + str(page - 1) + "&category=" + str(category)
    else:
        if offset + limit >= total_products:
            next_url = None
        else:
            next_url = "?page=" + str(page + 1)
        if offset == 0:
            prev_url = None
        else:
            prev_url = "?page=" + str(page - 1)

    # Getting categories to be used for filters
    categories = list(mongo.db.product_categories.find().sort("category", 1))

    context = {
        "products": products,
        "categories": categories,
        "results": total_products,
        "filter": category,
        "next": next_url,
        "prev": prev_url,
        "page": page
    }

    return render_template("products.html", **context)


@app.route("/login", methods=["GET", "POST"])
@anonymous_required
def login():
    """
    A function to render a page for the purpose of
    logging the user in to the site.
    """
    if request.method == "POST":
        # Check if email is in db
        user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if user:
            # Check if user is admin
            if user["admin"].lower() == "true":
                # Check hashed password is valid
                if check_password_hash(user["password"], request.form.get(
                        "password")):
                    session["user"] = request.form.get("username").lower()
                    session["admin"] = "true"
                    flash("Welcome, {} (Admin)".format(
                        request.form.get("username")), "success")
                    return redirect(url_for("index"))
                else:
                    # Invalid password
                    flash("Incorect Username and/or Password", "error")
                    return redirect(url_for("login"))
            else:
                # Check hashed password is valid
                if check_password_hash(user["password"], request.form.get(
                        "password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")), "success")
                    return redirect(url_for("index"))
                else:
                    # Invalid password
                    flash("Incorect Username and/or Password", "error")
                    return redirect(url_for("login"))
        else:
            # Username doesn't exist
            flash("Incorect Username and/or Password", "error")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    """
    A function to logout a user; removing the username
    from session cookies.
    """
    flash("You have been logged out.", "success")
    session.pop("user")
    if "admin" in session:
        session.pop("admin")
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
@anonymous_required
def register():
    """
    A function to render a page for the purpose of
    registering a user.
    """
    if request.method == "POST":
        # Check if user is in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!", "error")
            return redirect(url_for("register"))

        # Check if email is in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already exists!", "error")
            return redirect(url_for("register"))

        # Check if password1 & password2 match
        password1 = request.form.get("password")
        password2 = request.form.get("password2")

        if password1 != password2:
            flash("Both passwords must match!", "error")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "first_name": request.form.get("firstname").lower(),
            "last_name": request.form.get("lastname").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(password1),
            "admin": "false"
        }
        mongo.db.users.insert_one(register)

        # Put the current user into "session" so they are logged in.
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull!", "success")
        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
@login_required
def profile(username):
    """
    A function to render a user profile page; including
    profile & users recipes. A modal is included to edit
    the users profile.
    """

    # grab the session user's username from db
    user = mongo.db.users.find_one({"username": session["user"]})

    # A for loop to delete the password key from the user dict and
    # get the username value
    password_key = "password"
    for key, values in user.items():
        if key == password_key:
            del user[key]
            break
        if key == "username":
            username = values

    """
    The below is to populate the recipes with pagination.
    """

    # Number of items per page
    limit = 6

    # get the users recipes
    user_recipes = list(mongo.db.recipes.find(
        {"created_by": username}).sort("_id", -1))

    # Getting the length of the all the recipes to display total
    total_recipes = len(user_recipes)

    # Getting the offset (page number)
    if 'p' in request.args:
        if int(request.args['p']) <= 1:
            page = 1
            offset = 0
            redirect(url_for("profile", username=user["username"]))
        elif ((int(request.args['p']) * limit) - limit) > total_recipes:
            page = math.ceil((total_recipes/limit))
            offset = limit * (page - 1)
            flash("Page out of range", "error")
        else:
            page = int(request.args['p'])
            offset = limit * (page - 1)
    else:
        page = 1
        offset = 0

    if total_recipes > 0:
        # Getting the last id to with the offset used
        last_id = user_recipes[offset]["_id"]

        # Getting the page recipes using the last ID to offset and
        # limit to get set amount of results
        all_recipes_username = list(mongo.db.recipes.find(
                                    {'_id': {'$lte': last_id}})
                                    .sort("_id", -1))

        filtering_recipes = [
            key for key in all_recipes_username if key[
                'created_by'] == username
        ]
        recipes = filtering_recipes[:limit]
    else:
        recipes = []

    # Getting the next & prev url
    if offset + limit >= total_recipes:
        next_url = None
    else:
        next_url = "?p=" + str(page + 1)

    if offset == 0:
        prev_url = None
    else:
        prev_url = "?p=" + str(page - 1)

    # Function for updating the user profile
    if request.method == "POST":
        submit = {'$set': {
            "first_name": request.form.get("firstname"),
            "last_name": request.form.get("lastname"),
            "email": request.form.get("email"),
        }}

        mongo.db.users.update_one({"username": session["user"]}, submit)
        flash("Profile Updated", "success")
        return redirect(url_for('profile', username=session["user"]))

    context = {
        "user": user,
        "recipes": recipes,
        "results": total_recipes,
        "next": next_url,
        "prev": prev_url,
        "page": page
    }

    if session["user"]:
        return render_template("profile.html", **context)

    return redirect(url_for("login"))


@app.route("/admin/<username>", methods=["GET", "POST"])
@is_admin
def admin(username):
    """
    A function to render an admin page; including
    categories & products.
    """

    # grab the session user's username from db
    user = mongo.db.users.find_one({"username": session["user"]})

    # Check the user is an admin user
    if user["admin"].lower() == "false":
        flash("This page is for admin only!", "error")
        return redirect(url_for('index'))

    """
    The below is to populate the products with pagination.
    """

    # Number of items per page
    limit = 6

    # get all the products
    starting_id = list(mongo.db.products.find().sort("_id", -1))

    # Getting the length of the all the products to display total
    total_products = len(starting_id)

    # Getting the offset (page number)
    if 'p' in request.args:
        if int(request.args['p']) <= 1:
            page = 1
            offset = 0
            redirect(url_for("products"))
        elif ((int(request.args['p']) * limit) - limit) > total_products:
            page = math.ceil((total_products/limit))
            offset = limit * (page - 1)
            flash("Page out of range", "error")
        else:
            page = int(request.args['p'])
            offset = limit * (page - 1)
    else:
        page = 1
        offset = 0

    if total_products > 0:
        # Getting the last id to with the offset used
        last_id = starting_id[offset]["_id"]

        # Getting the page products using the last ID to offset and
        # limit to get set amount of results
        products = list(
            mongo.db.products.find({'_id': {'$lte': last_id}}).sort("_id", -1)
        )
    else:
        products = []

    # Getting the next & prev url
    if offset + limit >= total_products:
        next_url = None
    else:
        next_url = "?p=" + str(page + 1)

    if offset == 0:
        prev_url = None
    else:
        prev_url = "?p=" + str(page - 1)

    product_categories = list(
        mongo.db.product_categories.find().sort("category", 1)
    )

    recipe_categories = list(mongo.db.categories.find().sort("category", 1))

    context = {
        "user": user,
        "products": products,
        "results": total_products,
        "next": next_url,
        "prev": prev_url,
        "page": page,
        "product_categories": product_categories,
        "recipe_categories": recipe_categories
    }

    if session["user"] and session["admin"]:
        return render_template("admin.html", **context)

    return redirect(url_for("index"))


@app.route("/edit-category/<category_id>", methods=["GET", "POST"])
@is_admin
def edit_category_recipe(category_id):
    """
    A function to render a page for the purpose of
    the editing categories.
    """
    if request.method == "POST":

        submit = {'$set': {
            "category": request.form.get("category").lower(),
        }}

        mongo.db.categories.update_one({"_id": ObjectId(category_id)}, submit)
        flash("Category Updated Successfully", "success")
        return redirect(url_for('admin', username=session["user"]))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})

    context = {
        "category": category,
    }

    return render_template("edit-category.html", **context)


@app.route("/add-category/", methods=["GET", "POST"])
@is_admin
def add_category_recipe():
    """
    A function to render a page for the purpose of
    the adding recipe categories.
    """
    if request.method == "POST":

        submit = {
            "category": request.form.get("category").lower(),
        }

        mongo.db.categories.insert_one(submit)
        flash("Category Successfully Added", "success")
        return redirect(url_for('admin', username=session["user"]))

    return render_template("add-category.html")


@app.route("/edit-category/product/<category_id>", methods=["GET", "POST"])
@is_admin
def edit_category_product(category_id):
    """
    A function to render a page for the purpose of
    the editing categories.
    """
    if request.method == "POST":

        submit = {'$set': {
            "category": request.form.get("category").lower(),
        }}

        mongo.db.product_categories.update_one(
            {"_id": ObjectId(category_id)}, submit)
        flash("Category Updated Successfully", "success")
        return redirect(url_for('admin', username=session["user"]))

    category = mongo.db.product_categories.find_one(
        {"_id": ObjectId(category_id)})

    context = {
        "category": category,
    }

    return render_template("edit-category-product.html", **context)


@app.route("/add-category/product", methods=["GET", "POST"])
@is_admin
def add_category_product():
    """
    A function to render a page for the purpose of
    the adding product categories.
    """
    if request.method == "POST":

        submit = {
            "category": request.form.get("category").lower(),
        }

        mongo.db.product_categories.insert_one(submit)
        flash("Category Successfully Added", "success")
        return redirect(url_for('admin', username=session["user"]))

    return render_template("add-category-product.html")


@app.route("/add-recipe", methods=["GET", "POST"])
@login_required
def add_recipe():
    """
    A function to render a page for the purpose of
    the user adding recipes.
    """
    if request.method == "POST":
        """
        As the recipe form allows a dynamic amount of
        ingridients and steps, the below loops through
        the ingridients/steps creating a string split
        by the character "~".
        """
        ingridients = ""
        steps = ""
        for_loop_idx_ing = 0
        for_loop_idx_steps = 0
        for key, val in request.form.items():
            if key.startswith("ingridients"):
                if for_loop_idx_ing > 0:
                    ingridients += " ~ " + val.lower()
                    for_loop_idx_ing += 1
                else:
                    ingridients += val.lower()
                    for_loop_idx_ing += 1
            if key.startswith("steps"):
                if for_loop_idx_steps > 0:
                    steps += " ~ " + val.lower()
                    for_loop_idx_steps += 1
                else:
                    steps += val.lower()
                    for_loop_idx_steps += 1

        recipe = {
            "name": request.form.get("recipename").lower(),
            "category": request.form.get("category").lower(),
            "description": request.form.get("recipedesc").lower(),
            "cook_time": request.form.get("cooktime"),
            "prep_time": request.form.get("preptime"),
            "image_url": request.form.get("imageurl").lower(),
            "ingridients": ingridients,
            "steps": steps,
            "created": str(date.today().strftime("%x")),
            "created_by": session["user"]
        }

        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added", "success")
        return redirect(url_for('profile', username=session["user"]))

    categories = mongo.db.categories.find().sort("category", 1)

    context = {
        "categories": categories,
    }

    return render_template("add-recipe.html", **context)


@app.route("/edit-recipe/<recipe_id>", methods=["GET", "POST"])
@login_required
def edit_recipe(recipe_id):
    """
    A function to render a page for the purpose of
    the editing recipes.
    """
    if request.method == "POST":
        """
        As the recipe form allows a dynamic amount of
        ingridients and steps, the below loops through
        the ingridients/steps creating a string split
        by the character "~".
        """
        ingridients = ""
        steps = ""
        for_loop_idx_ing = 0
        for_loop_idx_steps = 0
        for key, val in request.form.items():
            if key.startswith("ingridients"):
                if for_loop_idx_ing > 0:
                    ingridients += " ~ " + val.lower()
                    for_loop_idx_ing += 1
                else:
                    ingridients += val.lower()
                    for_loop_idx_ing += 1
            if key.startswith("steps"):
                if for_loop_idx_steps > 0:
                    steps += " ~ " + val.lower()
                    for_loop_idx_steps += 1
                else:
                    steps += val.lower()
                    for_loop_idx_steps += 1

        recipe = {'$set': {
            "name": request.form.get("recipename").lower(),
            "category": request.form.get("category").lower(),
            "description": request.form.get("recipedesc").lower(),
            "cook_time": request.form.get("cooktime"),
            "prep_time": request.form.get("preptime"),
            "image_url": request.form.get("imageurl").lower(),
            "ingridients": ingridients,
            "steps": steps
        }}

        mongo.db.recipes.update_one({"_id": ObjectId(recipe_id)}, recipe)
        flash("Recipe Updated Successfully", "success")
        return redirect(url_for('profile', username=session["user"]))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipe_ings = recipe["ingridients"].split(" ~ ")
    recipe_steps = recipe["steps"].split(" ~ ")

    categories = mongo.db.categories.find().sort("category", 1)

    context = {
        "categories": categories,
        "recipe": recipe,
        "recipe_steps": recipe_steps,
        "recipe_ings": recipe_ings
    }

    return render_template("edit-recipe.html", **context)


@app.route("/add-product", methods=["GET", "POST"])
@is_admin
def add_product():
    """
    A function to render a page for the purpose of
    the adding a product.
    """

    if request.method == "POST":
        product = {
            "name": request.form.get("productname").lower(),
            "category": request.form.get("category").lower(),
            "description": request.form.get("productdesc").lower(),
            "image_url": request.form.get("imageurl"),
            "purchase": request.form.get("purchaseurl"),
        }

        mongo.db.products.insert_one(product)
        flash("Product Successfully Added", "success")
        return redirect(url_for('admin', username=session["user"]))

    categories = mongo.db.product_categories.find().sort("category", 1)

    context = {
        "categories": categories,
    }

    return render_template("add-product.html", **context)


@app.route("/edit-product/<product_id>", methods=["GET", "POST"])
@is_admin
def edit_product(product_id):
    """
    A function to render a page for the purpose of
    the editing a product.
    """
    if request.method == "POST":
        product = {'$set': {
            "name": request.form.get("productname").lower(),
            "category": request.form.get("category").lower(),
            "description": request.form.get("productdesc").lower(),
            "image_url": request.form.get("imageurl"),
            "purchase": request.form.get("purchaseurl"),
        }}

        mongo.db.products.update_one({"_id": ObjectId(product_id)}, product)
        flash("Product Updated Successfully", "success")
        return redirect(url_for('admin', username=session["user"]))

    product = mongo.db.products.find_one({"_id": ObjectId(product_id)})

    categories = mongo.db.product_categories.find().sort("category", 1)

    context = {
        "categories": categories,
        "product": product,
    }

    return render_template("edit-product.html", **context)


@app.route("/recipe/<recipe_id>")
def view_recipe(recipe_id):
    """
    This view displays an individual recipe for site
    visitors to view.
    """

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipe_ings = recipe["ingridients"].split(" ~ ")
    recipe_steps = recipe["steps"].split(" ~ ")

    # The below is used to capitalize the first letter of each sentence
    recipe_steps_formatted = []
    for step in recipe_steps:
        split = step.split(". ")
        string = []
        for step in split:
            sentence = str(step[0].upper() + step[1:] + ".")
            if sentence[-2:] == ('..'):
                sentence = sentence[:-1]
            string.append(sentence)
        recipe_steps_formatted.append(str(" ".join(string)))

    context = {
        "recipe": recipe,
        "recipe_steps": recipe_steps_formatted,
        "recipe_ings": recipe_ings
    }
    return render_template("view_recipe.html", **context)


@app.route("/delete-category/<category_id>")
@is_admin
def delete_category(category_id):
    """delete_category: \n
    * This function deletes a selected recipe category. \n
    \n
    \n Args: \n
    * category_id (str): A id of the obj to be deleted from the
        database.
    \n
    \n Returns: \n
    * It redirects the user back to the admin page \n
    * It shows a toast to indicate the category has been deleted \n
    """
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted", "success")
    return redirect(url_for("admin", username=session['user']))


@app.route("/delete-product-category/<category_id>")
@is_admin
def delete_product_category(category_id):
    """delete_product_category: \n
    * This function deletes a selected product category. \n
    \n
    \n Args: \n
    * category_id (str): A id of the obj to be deleted from the
        database.
    \n
    \n Returns: \n
    * It redirects the user back to the admin page \n
    * It shows a toast to indicate the product category has been deleted \n
    """
    mongo.db.product_categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted", "success")
    return redirect(url_for("admin", username=session['user']))


@app.route("/delete-product/<product_id>")
@is_admin
def delete_product(product_id):
    """delete_product: \n
    * This function deletes a selected product. \n
    \n
    \n Args: \n
    * product_id (str): A id of the obj to be deleted from the
        database.
    \n
    \n Returns: \n
    * It redirects the user back to the admin page \n
    * It shows a toast to indicate the product has been deleted \n
    """
    mongo.db.products.remove({"_id": ObjectId(product_id)})
    flash("Product Successfully Deleted", "success")
    return redirect(url_for("admin", username=session['user']))


@app.route("/delete-recipe/<recipe_id>")
@login_required
def delete_recipe(recipe_id):
    """delete_recipe: \n
    * This function deletes a selected recipe. \n
    \n
    \n Args: \n
    * recipe_id (str): A id of the obj to be deleted from the
        database.
    \n
    \n Returns: \n
    * It redirects the user back to the profile page \n
    * It shows a toast to indicate the recipe has been deleted \n
    """
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted", "success")
    return redirect(url_for("profile", username=session['user']))


def get_current_year():
    """
    Function to return the current year, for use with copyright in footer
    """
    current_datetime = datetime.now()
    return current_datetime.year


@app.context_processor
def context_processor():
    """
    Context processor for all templates
    """
    return {
        'year': get_current_year
    }


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
