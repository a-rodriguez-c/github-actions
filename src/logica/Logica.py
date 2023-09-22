import re
import time
from datetime import datetime

from src.modelo.entrenamiento import EjercicioEntrenamiento
from src.logica.serializer import EjercicioSchema
from src.logica.FachadaEnForma import FachadaEnForma
from src.modelo.persona import Persona
from src.modelo.ejercicio import Ejercicio
from src.modelo.declarative_base import Session, engine, Base
from sqlalchemy import func

def as_dict(record):
    return {column.name: getattr(record, column.name) for column in record.__table__.columns}

class Logica(FachadaEnForma):

    def __init__(self):
        Base.metadata.create_all(engine)

        self.session = Session()

    def __validar_fecha(self, fecha):
        try:
            if isinstance(fecha, str):
                datetime.strptime(fecha, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def __validar_numero(self, numero):
        try:
            int(numero)
            return True
        except ValueError:
            return False

    def dar_personas(self):
        registros = self.session.query(Persona).order_by(Persona.nombre).all()
        data = [as_dict(registro) for registro in registros]
        return data

    def validar_crear_editar_ejercicio(self, nombre, descripcion, enlace, calorias):
        return ""

    def crear_ejercicio(self, nombre, descripcion, enlace, calorias):

        data = {
            "nombre": nombre,
            "descripcion": descripcion,
            "enlaceVideoYoutube": enlace,
            "caloriasPorRepeticion": calorias
        }

        serializer = EjercicioSchema()

        try:
            validated_data = serializer.load(data)

            nuevo_ejercicio = Ejercicio(**validated_data)

            self.session.add(nuevo_ejercicio)
            self.session.commit()
            
            return True

        except Exception as e:
            self.session.rollback()
            return False

    def dar_ejercicios(self):
        registros = self.session.query(Ejercicio).order_by(Ejercicio.nombre).all()
        data = [as_dict(registro) for registro in registros]
        return data
    
    def dar_persona(self, id_persona):
        persona = self.session.query(Persona).filter(Persona.id == id_persona).first()
        if persona is not None:
            return {
                'nombre': persona.nombre,
                'apellido': persona.apellido,
                'edad': persona.edad,
                'talla': persona.talla,
                'peso': persona.peso,
                'brazo': persona.medidaBrazos,
                'pecho': persona.medidaPecho,
                'cintura': persona.medidaCintura,
                'pierna': persona.medidaPiernas,
                'fecha_retiro': persona.fechaDeFinEntrenamiento,
                'razon_retiro': persona.razonDeFinEntrenamiento
            }
        else:
            return {}
        
    def dar_entrenamientos(self, id_persona):
        persona = self.dar_persona(id_persona)

        if persona:
            ejercicios_persona = self.session.query(
                Ejercicio.nombre,
                Ejercicio.caloriasPorRepeticion,
                EjercicioEntrenamiento.fecha,
                EjercicioEntrenamiento.cantidad_repeticiones,
                EjercicioEntrenamiento.tiempo_ejercicio
            ).\
                outerjoin(Ejercicio, EjercicioEntrenamiento.ejercicio_id == Ejercicio.id).\
                where(EjercicioEntrenamiento.persona_id == id_persona)

            resultado = ejercicios_persona.all()
            entrenamientos = []
            for ejercicio, calorias, fecha, repeticiones, tiempo in resultado:
                entrenamientos.append({
                    'persona': persona['nombre'],
                    'ejercicio': ejercicio,
                    'calorias': calorias,
                    'fecha':  fecha.strftime('%Y-%m-%d'),
                    'repeticiones': repeticiones,
                    'tiempo': tiempo
                })

            return entrenamientos
        else:
            return []
    
    def dar_reporte(self, id_persona):
        persona = self.dar_persona(id_persona)

        entrenamientos = self.dar_entrenamientos(id_persona)

        reporte = {}
        total_repeticiones = 0
        total_calorias = 0
        for entrenamiento in entrenamientos:
            fecha = entrenamiento['fecha']
            if fecha not in reporte:
                reporte[fecha] = {
                    'fecha': fecha,
                    'repeticiones': 0,
                    'calorias': 0,
                }
            total_calorias_fecha = entrenamiento['repeticiones'] * entrenamiento['calorias']
            reporte[fecha]['repeticiones'] += entrenamiento['repeticiones']
            reporte[fecha]['calorias'] += total_calorias_fecha
            total_repeticiones += entrenamiento['repeticiones']
            total_calorias += total_calorias_fecha
        
        return {'persona': persona, 'estadisticas': {'total_repeticiones': total_repeticiones, 'total_calorias': total_calorias, 'imc': 0, 'clasificacion': '', 'entrenamientos': list(reporte.values())}}

    def validar_crear_editar_entrenamiento(self, persona, ejercicio, fecha, repeticiones, tiempo):
        if not persona:
            return 'Debe seleccionar una persona'
        if not ejercicio:
            return 'Debe seleccionar un ejercicio'
        if not fecha:
            return 'Debe ingresar una fecha'
        if not self.__validar_fecha(fecha):
            return 'Formato de fecha incorrecto'
        if not repeticiones:
            return 'Debe ingresar una cantidad de repeticiones'
        if not self.__validar_numero(repeticiones):
            return 'La cantidad de repeticiones debe ser un número'
        if not tiempo:
            return 'Debe ingresar un tiempo de entrenamiento'
        if not self.__validar_numero(tiempo):
            return 'El tiempo de entrenamiento debe ser un número'
        return ''

    def crear_entrenamiento(self, persona, ejercicio, fecha, repeticiones, tiempo):
        nuevo_entrenamiento = EjercicioEntrenamiento(
            persona_id=persona['id'],
            ejercicio_id=ejercicio['id'],
            fecha=fecha,
            cantidad_repeticiones=repeticiones,
            tiempo_ejercicio=tiempo
        )

        self.session.add(nuevo_entrenamiento)
        self.session.commit()
