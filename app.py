from elec_config import elemSearch, iupacName, electronicConfiguration
from elec_config_data import elements1
from flask import Flask, redirect, render_template, request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index(): 
    if request.method == "GET":
        return render_template("index.html", elementList = elements1)
    else:
        elem = int(request.form.get("element"))
        if elem >= 119:
            element = iupacName(elem)
        else:
            element = elemSearch(elem)
        return render_template("indexed.html", element = element, elecConfig = electronicConfiguration(elem), elementList = elements1)
        