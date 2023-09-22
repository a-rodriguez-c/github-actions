from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .declarative_base import Base

class EjercicioEntrenamiento(Base):
    __tablename__ = 'EjercicioEntrenamiento'

    id = Column(Integer, primary_key=True)
    persona_id = Column(Integer, ForeignKey('Persona.id'), nullable=False)
    ejercicio_id = Column(Integer, ForeignKey('Ejercicio.id'), nullable=False)
    cantidad_repeticiones = Column(Integer)
    tiempo_ejercicio = Column(String)
    fecha = Column(DateTime)

    # Definir relaciones con las tablas Persona y Ejercicio
    persona = relationship('Persona', back_populates='ejercicios_entrenamiento')
    ejercicio = relationship('Ejercicio')
