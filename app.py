from flask import Flask, render_template

app = Flask(__name__)

product = [["oil",True],['palu',True],['kampak',False]]

@app.route("/")
def honme():
    return render_template("wms.html", Product = product)


app.run()