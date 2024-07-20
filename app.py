from elec_config import elemSearch, iupacName, electronicConfiguration, elemSymbol
from elec_config_data import elements1
from flask import Flask, redirect, render_template, request
import mendeleev

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index(): 
    if request.method == "GET":
        return render_template("index.html", elementList = elements1)
    else:
        elem = int(request.form.get("element"))
        if elem >= 119:
            element = iupacName(elem)
            m = d = mp = bp = name_origin = False
        else:
            element = elemSearch(elem)
            elemSym = elemSymbol(elem)
            m = getattr(mendeleev, elemSym).mass
            d = round(float(getattr(mendeleev, elemSym).density)*1000, 3)
            mp = round(getattr(mendeleev, elemSym).melting_point, 2)
            bp = round(getattr(mendeleev, elemSym).boiling_point, 2)
            name_origin = getattr(mendeleev, elemSym).name_origin

        return render_template("indexed.html", 
                               element = element, 
                               elecConfig = electronicConfiguration(elem), 
                               elementList = elements1, 
                               mass = m, 
                               density = d,
                               meltingPoint = mp,
                               boilingPoint = bp,
                               nameOrigin = name_origin
                               )
        