from flask import Flask, render_template, request,redirect,url_for
from db import getProduct, getAccount, addProduct, updateProduct, deleteProduct, register, login, updateAccounts,getAccountById, deleteAccount

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = login(username, password)
        
        if user:
            return redirect(url_for('monitoring'))
        else:
            return "Login gagal. Username atau password salah."
    
    return render_template('login.html')

@app.route('/monitoring')
def monitoring():
    product = getProduct()
    return render_template("monitoring.html", Product = product)
    
@app.route("/add", methods=['GET', 'POST'])
def add_page():
    if request.method == 'POST':
        productname = request.form['productName']
        categoryproduct = request.form['categoryProduct']
        rfid = request.form['rfid']
        addProduct(productname, categoryproduct, rfid)
        return redirect(url_for('monitoring'))

    product = getProduct()
    return render_template("add.html", Product=product)


@app.route("/update", methods=["GET","POST"])
def update_route():
    if request.method == "GET":
        product = getProduct()
        return render_template("update.html", Product=product)

    id = request.form["id"]
    updateProductname = request.form.get(f"updateProduct_{id}")
    updateProduct(updateProductname, id)
    return redirect(url_for('monitoring'))

@app.route("/delete", methods = ["GET", "POST"])
def delete_route():
    if request.method == "GET":
        product = getProduct()
        return render_template("delete.html", Product=product)

    id = request.form["id"]
    deleteProduct(id)
    return redirect(url_for('monitoring'))

@app.route('/register', methods=['GET', 'POST'])
def register_route():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        fullname = request.form['fullname']
        email = request.form['email']
        role = request.form['role'] 
        register(username, password,fullname,email,role)
        return redirect(url_for('login_route'))  
    return render_template('register.html')  

@app.route('/management')
def management():
    account = getAccount()
    return render_template("user_management.html", Accounts = account)

@app.route('/editAccounts/<int:user_id>',methods=["GET", "POST"])
def editAccounts(user_id):
    if request.method == "GET":
        account = getAccountById(user_id)
        return render_template("editAccounts.html", Account = account)
    
    fullname = request.form['fullname']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    role = request.form['role']
    status = request.form['status']

    updateAccounts(fullname, email,username, password,role, status,user_id)
    return redirect(url_for('management'))

@app.route('/deleteAccounts/<int:user_id>', methods=['GET'])
def deleteAccounts(user_id):
    deleteAccount(user_id)
    return redirect(url_for('management'))


    


app.run()