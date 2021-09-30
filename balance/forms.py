from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms.fields.core import FloatField, RadioField, StringField
from wtforms.fields.simple import HiddenField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class MovimientoFormulario(FlaskForm):

    id = HiddenField()
    
    fecha = DateField("Fecha", validators=[DataRequired(message="Debe informar la fecha")])
    concepto = StringField("Concepto", validators=[DataRequired(message="Debe informar el concepto"), Length(min=10)])
    cantidad = FloatField("Cantidad", validators=[DataRequired(message="Debe informar el monto del movimiento"), 
                                                    NumberRange(message="Debe informar un importe positivo", min=0.01)])
    ingreso_gasto = RadioField(validators=[DataRequired(message="Debe informar el tipo de movimiento")], 
                                            choices=[("G", "Gasto"), ("I", "Ingreso")])
    
    submit = SubmitField("Aceptar")  