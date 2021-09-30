from flask_wtf import form
from balance import app
from flask import render_template, request, redirect, url_for, flash
from balance.models import DBManager
from balance.forms import MovimientoFormulario
from datetime import date

ruta_basedatos = app.config.get("RUTA_BASE_DE_DATOS")
dbManager = DBManager(ruta_basedatos)

@app.route("/")
def inicio():

    consulta = """
        SELECT * 
        FROM movimientoS
        ORDER BY fecha;
    """
    movimientos = dbManager.consultaSQL(consulta)
    
    return render_template("inicio.html", items=movimientos)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo():
    formulario = MovimientoFormulario()

    if request.method == "GET":
        return render_template("nuevo_movimiento.html", form=formulario)
    else: 
        if formulario.validate():
            consulta = """
                INSERT INTO movimientos (fecha, concepto, ingreso_gasto, cantidad)
                 VALUES (:fecha, :concepto, :ingreso_gasto, :cantidad)
            """
            try: 
                dbManager.modificaSQL(consulta, formulario.data) 
            except Exception as e:
                print("Se ha producido un error de acceso a base de datos:", e)
                flash("Se ha producido un error en la base de datos. Consulte con su administrador")
                return render_template("nuevo_movimiento.html", form=formulario)

            return redirect(url_for("inicio")) 

        else: 
            return render_template("nuevo_movimiento.html", form=formulario)

@app.route("/borrar/<int:id>", methods=["GET", "POST"])
def borrar(id):
    if request.method == 'GET':
        consulta = """
        SELECT id, fecha, concepto, ingreso_gasto, cantidad 
          FROM movimientos 
        WHERE id = ?;
        """
        
        movimientos = dbManager.consultaSQL(consulta, [id])
        if len(movimientos) == 0:
            flash(f"Movimiento {id} no encontrado")
            return redirect(url_for("inicio"))

        el_movimiento = movimientos[0]
        el_movimiento["fecha"] = date.fromisoformat(el_movimiento["fecha"])
        formulario = MovimientoFormulario(data=el_movimiento)

        return render_template("borrar_movimiento.html", form=formulario)
    else:
        pass 
        # TODO  lo mismo que de la linea 31 a 45 de este programa pero con delete en lugar de con insert
        # validacion opcional

    return 'Hola, soy un POST'

   