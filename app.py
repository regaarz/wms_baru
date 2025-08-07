from flask import Flask, render_template, request,redirect,url_for
from db import getProduct, addProduct, updateProduct, deleteProduct

app = Flask(__name__)


@app.route("/")
def home():
    product = getProduct()
    return render_template("wms.html", Product = product)

@app.route("/add", methods=['POST'])
def add_route():
    productname = request.form['productName']
    categoryproduct = request.form['categoryProduct']
    rfid = request.form['rfid']
    addProduct(productname,categoryproduct,rfid)
    return redirect(url_for('home'))

@app.route("/update", methods=["POST"])
def update_route():
    updateProductname = request.form["updateProduct"]
    id = request.form["id"]
    button = request.form['save_or_delete']
    if button == "save":
        updateProduct(updateProductname, id)
    elif button == "x":
        deleteProduct(id)
    return redirect(url_for('home'))



app.run()