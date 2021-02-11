import os
import datetime
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

    recipes = list(mongo.db.quotes.find())

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


@app.route("/login/")
def login():
    """
    A function to render a page for the purpose of
    logging the user in to the site.
    """

    context = {
    }
    return render_template("login.html", **context)


@app.route("/register/", methods=["GET", "POST"])
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
            flash("Username already exists")
            return redirect(url_for("register"))

        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already exists")
            return redirect(url_for("register"))

        password1 = request.form.get("password")
        password2 = request.form.get("password2")

        if password1 != password2:
            flash("Both passwords must match!")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "first_name": request.form.get("firstname").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(password1)
        }
        mongo.db.users.insert_one(register)

        # Put the current user into "session" so they are logged in.
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull")

    context = {
    }
    return render_template("register.html", **context)


def get_current_year():
    """
    Function to return the current year, for use with copyright in footer
    """
    current_datetime = datetime.datetime.now()
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
