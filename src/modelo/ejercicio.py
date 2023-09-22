from sqlalchemy import Column, Integer, String, ForeignKey,CheckConstraint

from .declarative_base import Base


class Ejercicio(Base):
    __tablename__ = 'Ejercicio'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)  # El campo 'nombre' no puede ser nulo
    descripcion = Column(String, nullable=False)  # El campo 'descripcion' no puede ser nulo
    enlaceVideoYoutube = Column(String, nullable=False)  # El campo 'enlaceVideoYoutube' no puede ser nulo
    caloriasPorRepeticion = Column(Integer, nullable=False)  # El campo 'caloriasPorRepeticion' no puede ser nulo

    # Agregar una restricción de columna para asegurarse de que caloriasPorRepeticion sea positivo
    __table_args__ = (
        CheckConstraint('caloriasPorRepeticion >= 0', name='positive_calories_constraint'),
    )

