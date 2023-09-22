from sqlalchemy import Column, Integer, String, ForeignKey

from .declarative_base import Base
from sqlalchemy.orm import relationship


class Persona(Base):
    __tablename__ = 'Persona'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    talla = Column(Integer)
    peso = Column(Integer)
    edad = Column(Integer)
    medidaBrazos = Column(Integer)
    medidaPecho = Column(Integer)
    medidaAbdomen = Column(Integer)
    medidaCintura = Column(Integer)
    medidaPiernas = Column(Integer)
    fechaDeInicioEntrenamiento = Column(String)
    fechaDeFinEntrenamiento = Column(String)
    razonDeFinEntrenamiento = Column(String)

    # Agregar una relación uno a muchos con EjercicioEntrenamiento
    ejercicios_entrenamiento = relationship('EjercicioEntrenamiento', back_populates='persona')
