import os
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
    """
    A decorator to protect views that are only accessible
    if the user is logged in. Code from
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


def anonymous_required(f):
    """
    A decorator to protect views that are only accessible
    if the user is anonymous. Code adapted from
    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" in session:
            flash("That page is only for unauthenticated users."
                  " Please logout if you wish to access this.", "error")
            return redirect("..")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
def index():
    """
    The below accesses MongoDB quotes table and gets a
    list of all quotes objects before selecting one
    at random to be shown on page load. Everytime the page
    is refreshed a new random quote will be found.
    """

    single_quote = random.choice(list(mongo.db.quotes.find()))

    context = {
        "quote": single_quote,
    }
    return render_template("index.html", **context)


@app.route("/recipes/")
def recipes():
    """
    A function to render a page of all recipes, with options
    to filter and search.
    """

    recipes = list(mongo.db.recipes.find().sort("created", 1))

    context = {
        "recipes": recipes,
    }
    return render_template("recipes.html", **context)


@app.route("/products/")
def products():
    """
    A function to render a page of all products, with options
    to filter and search.
    """

    products = list(mongo.db.quotes.find())

    context = {
        "products": products,
    }
    return render_template("products.html", **context)


@app.route("/login/", methods=["GET", "POST"])
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
            # Check hashed password is valid
            if check_password_hash(
                user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")),
                    "success")
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


@app.route("/logout/")
@login_required
def logout():
    """
    A function to logout a user; removing the username
    from session cookies.
    """
    flash("You have been logged out.", "success")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/register/", methods=["GET", "POST"])
@anonymous_required
def register():
    """
    A function to render a page for the purpose of
    registering a user.
    """
    if request.method == "POST":
        # Check if email is in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists!", "error")
            return redirect(url_for("register"))

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already exists!", "error")
            return redirect(url_for("register"))

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
            "password": generate_password_hash(password1)
        }
        mongo.db.users.insert_one(register)

        # Put the current user into "session" so they are logged in.
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull!", "success")
        return redirect(url_for("index"))

    return render_template("register.html")


@app.route("/profile/<username>/", methods=["GET", "POST"])
@login_required
def profile(username):
    """
    A function to render a user profile page; including
    profile & users recipes. A modal is included to edit
    the users profile.
    """

    if request.method == "POST":
        submit = {'$set': {
            "first_name": request.form.get("firstname"),
            "last_name": request.form.get("lastname"),
            "email": request.form.get("email"),
        }}

        mongo.db.users.update({"username": session["user"]}, submit)
        flash("Profile Updated", "success")
        return redirect(url_for('profile', username=session["user"]))

    # grab the session user's username from db
    user = mongo.db.users.find_one({"username": session["user"]})

    # A for loop to delete the password key from the user dict
    password_key = "password"
    for key in user.keys():
        if key == password_key:
            del user[key]
            break

    context = {
        "user": user,
    }

    if session["user"]:
        return render_template("profile.html", **context)

    return redirect(url_for("login"))


@app.route("/add-recipe/", methods=["GET", "POST"])
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
                    ingridients += " ~ " + val
                    for_loop_idx_ing += 1
                else:
                    ingridients += val
                    for_loop_idx_ing += 1
            if key.startswith("step"):
                if for_loop_idx_steps > 0:
                    steps += " ~ " + val
                    for_loop_idx_steps += 1
                else:
                    steps += val
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
