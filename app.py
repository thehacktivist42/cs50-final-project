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
            m = d = mp = bp = discovery_year = discoverers = False
            elemName = element
            name_origin = "Named using the conventions laid out by IUPAC for the nomenclature of undiscovered elements"
            description = f"The properties of {elemName} are not known."
            color = 'light'
            block = ''
        else:
            element = elemSearch(elem)
            elemSym = elemSymbol(elem)
            elemName = getattr(mendeleev, elemSym).name
            m = (getattr(mendeleev, elemSym).mass if getattr(mendeleev, elemSym).mass else "Not known")
            d = (round(float(getattr(mendeleev, elemSym).density)*1000, 3) if getattr(mendeleev, elemSym).density else "Not known")
            mp = (round(getattr(mendeleev, elemSym).melting_point, 2) if getattr(mendeleev, elemSym).melting_point else "Not known")
            bp = (round(getattr(mendeleev, elemSym).boiling_point, 2) if getattr(mendeleev, elemSym).boiling_point else "Not known")
            block = getattr(mendeleev, elemSym).block
            name_origin = (getattr(mendeleev, elemSym).name_origin if getattr(mendeleev, elemSym).name_origin else "Not known")
            description = (getattr(mendeleev, elemSym).description if getattr(mendeleev, elemSym).description else f"Not much is known about {elemName} due to its recent discovery and short half-life.")
            discovery_year = (getattr(mendeleev, elemSym).discovery_year if getattr(mendeleev, elemSym).discovery_year else f"Not known")
            discoverer = (getattr(mendeleev, elemSym).discoverers if getattr(mendeleev, elemSym).discoverers else "Not known")
            discoverers = ''
            if type(discoverer) is list:
                discoverers = ', '.join(discoverer)
            else:
                discoverers = discoverer
            color = ''
            match block:
                case 's':
                    color = 'danger'
                case 'p':
                    color = 'warning'
                case 'd':
                    color = 'primary'
                case 'f':
                    color = 'success'
                case _:
                    color = 'light'
        return render_template("indexed.html", 
                               element = element, 
                               elecConfig = electronicConfiguration(elem), 
                               elementList = elements1, 
                               mass = m, 
                               density = d,
                               meltingPoint = mp,
                               boilingPoint = bp,
                               nameOrigin = name_origin,
                               elementName = elemName,
                               description = description,
                               discoverers = discoverers,
                               discoveryYear = discovery_year,
                               colour = color,
                               block = block
                               )
        