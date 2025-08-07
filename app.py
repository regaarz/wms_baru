from flask import Flask, render_template, request,redirect,url_for
from db import getProduct, addTask

app = Flask(__name__)


@app.route("/")
def home():
    product = getProduct()
    return render_template("wms.html", Product = product)

@app.route("/add", methods=['POST'])
def add():
    productname = request.form['productName']
    categoryproduct = request.form['categoryProduct']
    duedate = request.form['dueDate']
    status_ = request.form['status']
    addTask(productname,categoryproduct,duedate,status_)
    return redirect(url_for('home'))

app.run()