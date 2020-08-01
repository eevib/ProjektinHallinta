from flask import Flask
from flask import redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask import request

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/newCustomer")
def newCustomer():
	return render_template("newCustomer.html")

@app.route("/create", methods=["POST"])
def create():
	name = request.form["name"]
	email = request.form["email"]
	phone= request.form["phone"]
	sql= "INSERT INTO customers (name, email, phone) VALUES (:name, :email, :phone)" 
	reuslt= db.session.execute(sql, {"name":name, "email":email, "phone":phone})
	db.session.commit()
	return redirect("/")
