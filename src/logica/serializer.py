from marshmallow import Schema, fields, validate

class EjercicioSchema(Schema):
    nombre = fields.String(required=True, validate=validate.Length(min=4))
    descripcion = fields.String(required=True, validate=validate.Length(min=10))
    enlaceVideoYoutube = fields.String(required=True, validate=validate.URL())
    caloriasPorRepeticion = fields.Integer(required=True, validate=validate.Range(min=10))
