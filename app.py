import os
import datetime
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
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Function to return the home page (index.html) of the site
@app.route("/")
def index():

    context = {
    }
    return render_template("index.html")


# Function to return the current year, for use with copyright year
def get_current_year():
    current_datetime = datetime.datetime.now()
    return current_datetime.year


# Context processor for all templates
@app.context_processor
def context_processor():
    return {
        'year': get_current_year
    }


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
