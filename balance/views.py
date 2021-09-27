from balance.models import DBManager
from balance import app
from flask import render_template
from balance.models import DBManager

ruta_basedatos = app.config.get("RUTA_BASE_DE_DATOS")
dbManager = DBManager(ruta_basedatos)

@app.route("/")
def inicio():
    
    movimientos = dbManager.consultaSQL("SELECT * FROM movimientos order by fecha;")
    
    return render_template("inicio.html", items=movimientos)

@app.route("/nuevo", methods=("GET", "POST"))
def nuevo():
    return "Página de alta de movimiento"

@app.route("/borrar/<int:id>", methods=("GET", "POST"))
def borrar(id):
    return f"Página de borrado {id}"