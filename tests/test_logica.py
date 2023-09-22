import os
import random
import sys
import time
import unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.join(current_dir, '..') 
sys.path.append(project_dir)

from datetime import datetime, timedelta
from src.modelo.entrenamiento import EjercicioEntrenamiento
from src.modelo.declarative_base import session, engine
from src.modelo.persona import Persona
from src.modelo.ejercicio import Ejercicio
from sqlalchemy import MetaData, Table,func
from src.logica.Logica import Logica


class ListarPersona(unittest.TestCase):

    def setUp(self):
        self.session = session

        self.logica = Logica()
        
    def tearDown(self):
        metadata = MetaData()
        mi_tabla = Table('Persona', metadata)
        session.execute(mi_tabla.delete())
        session.commit()

        self.logica = None
        
    def __agregar_personas(self):
        persona1 = Persona(
            nombre='Juan',
            apellido='Perez',
            talla=175,
            peso=70,
            edad=30,
            medidaBrazos=30,
            medidaPecho=95,
            medidaAbdomen=80,
            medidaCintura=75,
            medidaPiernas=95,
            fechaDeInicioEntrenamiento='2023-01-01',
            fechaDeFinEntrenamiento='2023-09-20',
            razonDeFinEntrenamiento='Objetivo alcanzado'
        )

        persona2 = Persona(
            nombre='Anderson',
            apellido='Rodriguez',
            talla=176,
            peso=72,
            edad=21,
            medidaBrazos=22,
            medidaPecho=45,
            medidaAbdomen=34,
            medidaCintura=75,
            medidaPiernas=34,
            fechaDeInicioEntrenamiento='2023-01-01',
            fechaDeFinEntrenamiento='2023-09-20',
            razonDeFinEntrenamiento='Objetivo alcanzado'
        )

        self.session.add(persona1)
        self.session.add(persona2)

        self.session.commit()
        self.session.close()

    def test_lista_vacia(self):
        personas = self.logica.dar_personas()
        self.assertEqual(len(personas), 0, "lista de personas vacia")

    def test_lista_varias_personas(self):
        self.__agregar_personas()
        personas = self.logica.dar_personas()
        self.assertNotEqual(len(personas), 0)
        self.assertGreater(len(personas), 0)

    def test_lista_personas_ordenadas_alfabeticamente(self):
        self.__agregar_personas()
        personas_ordenadas = self.logica.dar_personas()

        for i in range(len(personas_ordenadas) - 1):
            assert personas_ordenadas[i]['nombre'] <= personas_ordenadas[i + 1]['nombre']

class CrearEjercicio(unittest.TestCase):

    def setUp(self):
        self.session = session
        self.logica = Logica()
        
    def tearDown(self):
        metadata = MetaData()
        mi_tabla = Table('Ejercicio', metadata)
        session.execute(mi_tabla.delete())
        session.commit()
        self.logica = None
        session.close()

    def test_crear_ejercicio_error_nombre(self):
        nombres = ""
        descripcion = "con el peso en la parte posterior subir y bajar"
        enlaces = "http://www.ejemplo1.com"
        calorias = 500

        resultado = self.logica.crear_ejercicio(nombres, descripcion, enlaces, calorias)
        
        self.assertEqual(resultado, False)


    def test_crear_ejercicio_error_descripcion(self):
        nombres = "sentadilla"
        descripcion = ""
        enlaces = "http://www.ejemplo1.com"
        calorias = 500

        resultado = self.logica.crear_ejercicio(nombres, descripcion, enlaces, calorias)
        
        self.assertEqual(resultado, False)

    def test_crear_ejercicio_error_enlace(self):
        nombres = "sentadilla"
        descripcion = "con el peso en la parte posterior subir y bajar"
        enlaces = ""
        calorias = 500

        resultado = self.logica.crear_ejercicio(nombres, descripcion, enlaces, calorias)
        
        self.assertEqual(resultado, False)

    def test_crear_ejercicio_correctamente(self):
        nombres = "sentadilla"
        descripcion = "con el peso en la parte posterior subir y bajar"
        enlaces = "http://www.ejemplo1.com"
        calorias = 500

        resultado = self.logica.crear_ejercicio(nombres, descripcion, enlaces, calorias)
        self.assertEqual(resultado, True)

        metadata = MetaData()
        tabla_ejercicio = Table('Ejercicio', metadata)
        contador = self.session.query(func.count()).select_from(tabla_ejercicio).scalar()
        self.assertEqual(contador, 1)

class ListarEjercicio(unittest.TestCase):

    def setUp(self):
        self.session = session
        self.logica = Logica()
        
    def tearDown(self):
        metadata = MetaData()
        tabla_ejercicio = Table('Ejercicio', metadata)
        session.execute(tabla_ejercicio.delete())
        session.commit()
        self.logica = None

    def __agregar_ejercicios(self):
        ejercicio1 = Ejercicio(
            nombre="Sentadillas",
            descripcion="Con el peso en la parte posterior subir y bajar",
            enlaceVideoYoutube="http://www.ejemplo.com/sentadillas",
            caloriasPorRepeticion=150
        )

        ejercicio2 = Ejercicio(
            nombre="Flexiones",
            descripcion="Ejercicio para fortalecer el pecho y brazos",
            enlaceVideoYoutube="http://www.ejemplo.com/flexiones",
            caloriasPorRepeticion=120
        )

        ejercicio3 = Ejercicio(
            nombre="Burpees",
            descripcion="Un ejercicio de cuerpo completo que combina saltos y flexiones",
            enlaceVideoYoutube="http://www.ejemplo.com/burpees",
            caloriasPorRepeticion=200
        )

        self.session.add(ejercicio1)
        self.session.add(ejercicio2)
        self.session.add(ejercicio3)

        self.session.commit()
        self.session.close()

    def test_lista_vacia(self):
        ejercicios = self.logica.dar_ejercicios()
        self.assertEqual(len(ejercicios), 0, "lista de ejercicios vacío")

    def test_lista_varios_ejercicios(self):
        self.__agregar_ejercicios()
        ejercicios = self.logica.dar_ejercicios()
        self.assertNotEqual(len(ejercicios), 0)
        self.assertGreater(len(ejercicios), 0)

class ObtenerPersona(unittest.TestCase):
    def setUp(self):
        self.session = session

        self.logica = Logica()
        
    def tearDown(self):
        metadata = MetaData()
        mi_tabla = Table('Persona', metadata)
        session.execute(mi_tabla.delete())
        session.commit()
        self.session.close()
        self.logica = None

    def __agregar_persona(self):
        persona1 = Persona(
            nombre='Camilo',
            apellido='Lesmes',
            talla=176,
            peso=72,
            edad=21,
            medidaBrazos=22,
            medidaPecho=45,
            medidaAbdomen=34,
            medidaCintura=75,
            medidaPiernas=34,
            fechaDeInicioEntrenamiento='2023-01-01',
            fechaDeFinEntrenamiento='2023-06-30',
            razonDeFinEntrenamiento='Objetivo alcanzado'
        )

        self.session.add(persona1)
        self.session.commit()
        return persona1

     
    def test_persona_no_encontrada(self):
        personas = self.logica.dar_persona(id_persona=541051)
        self.assertEqual(len(personas), 0, "Persona no encontrada")

    def test_persona_encontrada(self):
        self.__agregar_persona()
        persona = self.logica.dar_persona(id_persona=1)
        self.assertNotEqual(len(persona), 0)
        self.assertGreater(len(persona), 0)

    def test_dar_persona_retorna_todos_los_campos(self):

        persona = self.__agregar_persona()
        dar_persona = self.logica.dar_persona(id_persona=1)

        self.assertEqual(dar_persona['nombre'], persona.nombre)
        self.assertEqual(dar_persona['apellido'], persona.apellido)
        self.assertEqual(dar_persona['edad'], persona.edad)
        self.assertEqual(dar_persona['talla'], persona.talla)
        self.assertEqual(dar_persona['peso'], persona.peso)
        self.assertEqual(dar_persona['brazo'], persona.medidaBrazos)
        self.assertEqual(dar_persona['pecho'], persona.medidaPecho)
        self.assertEqual(dar_persona['cintura'], persona.medidaCintura)
        self.assertEqual(dar_persona['pierna'], persona.medidaPiernas)
        self.assertEqual(dar_persona['fecha_retiro'], persona.fechaDeFinEntrenamiento)
        self.assertEqual(dar_persona['razon_retiro'], persona.razonDeFinEntrenamiento)

class ListarEntrenamiento(unittest.TestCase):

    def setUp(self):
        self.session = session
        self.logica = Logica()
        self.__crear_ejercicios_persona_1()
        self.__crear_ejercicios_persona_2()

    def __crear_ejercicios_persona_1(self):
        ejercicio1 = Ejercicio(
            nombre="Sentadillas",
            descripcion="Con el peso en la parte posterior subir y bajar",
            enlaceVideoYoutube="http://www.ejemplo.com/sentadillas",
            caloriasPorRepeticion=150
        )

        ejercicio2 = Ejercicio(
            nombre="Flexiones",
            descripcion="Ejercicio para fortalecer el pecho y brazos",
            enlaceVideoYoutube="http://www.ejemplo.com/flexiones",
            caloriasPorRepeticion=120
        )

        persona1 = Persona(
            nombre='Camilo',
            apellido='Lesmes',
            talla=175,
            peso=70,
            edad=30,
            medidaBrazos=30,
            medidaPecho=95,
            medidaAbdomen=80,
            medidaCintura=75,
            medidaPiernas=95,
            fechaDeInicioEntrenamiento='2023-09-14',
            fechaDeFinEntrenamiento='2023-09-20',
            razonDeFinEntrenamiento='Objetivo alcanzado'
        )


        session.add_all([persona1, ejercicio1, ejercicio2])
        session.commit()

        entrenamiento1 = EjercicioEntrenamiento(persona=persona1, ejercicio=ejercicio1, cantidad_repeticiones=50,tiempo_ejercicio="20 min", fecha=datetime.now())
        entrenamiento2 = EjercicioEntrenamiento(persona=persona1, ejercicio=ejercicio2, cantidad_repeticiones=40,tiempo_ejercicio="50 min", fecha=datetime.now())
        session.add_all([entrenamiento1, entrenamiento2])
        session.commit()

    def __crear_ejercicios_persona_2(self):
        ejercicio3 = Ejercicio(
            nombre="Burpees",
            descripcion="Un ejercicio de cuerpo completo que combina saltos y flexiones",
            enlaceVideoYoutube="http://www.ejemplo.com/burpees",
            caloriasPorRepeticion=200
        )

        persona2 = Persona(
            nombre='Andersson',
            apellido='Rodriguez',
            talla=175,
            peso=70,
            edad=30,
            medidaBrazos=30,
            medidaPecho=95,
            medidaAbdomen=80,
            medidaCintura=75,
            medidaPiernas=95,
            fechaDeInicioEntrenamiento='2023-09-14',
            fechaDeFinEntrenamiento='2023-09-20',
            razonDeFinEntrenamiento='Objetivo alcanzado'
        )

        session.add_all([persona2, ejercicio3])
        session.commit()

        entrenamiento4 = EjercicioEntrenamiento(persona=persona2, ejercicio=ejercicio3, cantidad_repeticiones=1,tiempo_ejercicio="2 min", fecha=datetime.now())

        session.add_all([entrenamiento4])
        session.commit()

    def tearDown(self):
        metadata = MetaData()
        tabla_ejercicio = Table('Ejercicio', metadata)
        session.execute(tabla_ejercicio.delete())
        tabla_persona = Table('Persona', metadata)
        session.execute(tabla_persona.delete())
        tabla_entrenamiento = Table('EjercicioEntrenamiento', metadata)
        session.execute(tabla_entrenamiento.delete())
        session.commit()
        session.close()
        self.logica = None

    def test_lista_vacia(self):
        entrenamiento = self.logica.dar_entrenamientos(id_persona=5424)
        self.assertEqual(len(entrenamiento), 0, "lista de entrenamientos vacío")

    def test_lista_ejercicios_usuario(self):
        entrenamientos = self.logica.dar_entrenamientos(id_persona=1)
        self.assertNotEqual(len(entrenamientos), 0)
        self.assertGreater(len(entrenamientos), 0)

    def test_validar_campos_completos_lista_usuario(self):
        entrenamientos = self.logica.dar_entrenamientos(id_persona=2)
        self.assertNotEqual(len(entrenamientos), 0)
        self.assertGreater(len(entrenamientos), 0)

        for entrenamiento in entrenamientos:
            self.assertIsNotNone(entrenamiento['persona'])
            self.assertIsNotNone(entrenamiento['ejercicio'])
            self.assertIsNotNone(entrenamiento['fecha'])
            self.assertIsNotNone(entrenamiento['repeticiones'])

class DarReporte(unittest.TestCase):
    def setUp(self):
        self.session = session
        self.logica = Logica()

    def tearDown(self):
        metadata = MetaData()
        tabla_ejercicio = Table('Ejercicio', metadata)
        session.execute(tabla_ejercicio.delete())
        tabla_persona = Table('Persona', metadata)
        session.execute(tabla_persona.delete())
        tabla_entrenamiento = Table('EjercicioEntrenamiento', metadata)
        session.execute(tabla_entrenamiento.delete())
        session.commit()
        session.close()
        self.logica = None

    def __crear_persona(self):
        persona = Persona(
            nombre='Camilo',
            apellido='Lesmes',
            talla=175,
            peso=70,
            edad=30,
            medidaBrazos=30,
            medidaPecho=95,
            medidaAbdomen=80,
            medidaCintura=75,
            medidaPiernas=95,
            fechaDeInicioEntrenamiento='2023-09-14',
            fechaDeFinEntrenamiento='2023-09-20',
            razonDeFinEntrenamiento='Objetivo alcanzado'
        )

        session.add_all([persona])
        session.commit()

        return persona

    def __crear_ejercicio(self):
        ejercicio = Ejercicio(
            nombre="Sentadillas",
            descripcion="Con el peso en la parte posterior subir y bajar",
            enlaceVideoYoutube="http://www.ejemplo.com/sentadillas",
            caloriasPorRepeticion=150
        )

        session.add_all([ejercicio])
        session.commit()

        return ejercicio

    def __crear_entrenamiento(self, persona, ejercicio):
        fecha = datetime.now() + timedelta(days=5)
        entrenamiento = EjercicioEntrenamiento(persona=persona, ejercicio=ejercicio, cantidad_repeticiones=50,
                                                tiempo_ejercicio="20 min", fecha=fecha)

        session.add_all([entrenamiento])
        session.commit()
        return entrenamiento

    def __crear_entrenamientos(self, persona, ejercicio, cantidad=1):
        for i in range(cantidad):
            fecha = datetime.now() + timedelta(days=random.randint(1, 10))
            entrenamiento = EjercicioEntrenamiento(persona=persona, ejercicio=ejercicio, cantidad_repeticiones=random.randint(13, 100),
                                                   tiempo_ejercicio="20 min", fecha=fecha)

            session.add_all([entrenamiento])
            session.commit()

    def test_dar_reporte_fechas_estadisticas_vacio(self):
        reporte = self.logica.dar_reporte(id_persona=5424)
        entrenamientos = reporte['estadisticas']['entrenamientos']
        self.assertEqual(len(entrenamientos), 0)

    def test_dar_reporte_fechas_estadisticas_un_registro(self):
        persona = self.__crear_persona()
        ejercicio = self.__crear_ejercicio()
        self.__crear_entrenamiento(persona, ejercicio)
        reporte = self.logica.dar_reporte(id_persona=persona.id)
        entrenamientos = reporte['estadisticas']['entrenamientos']
        self.assertEqual(len(entrenamientos), 1)

    def tes_dar_reporte_fechas_entrenamientos_varios_registros(self):
        persona = self.__crear_persona()
        ejercicio = self.__crear_ejercicio()
        self.__crear_entrenamientos(
            persona=persona,
            ejercicio=ejercicio,
            cantidad=3
        )
        reporte = self.logica.dar_reporte(id_persona=persona.id)
        entrenamientos = reporte['estadisticas']['entrenamientos']
        self.assertEqual(len(entrenamientos), 3)

    def test_dar_reporte_fechas_campo_fecha(self):
        persona = self.__crear_persona()
        ejercicio = self.__crear_ejercicio()
        self.__crear_entrenamiento(persona, ejercicio)
        reporte = self.logica.dar_reporte(id_persona=persona.id)
        entrenamientos = reporte['estadisticas']['entrenamientos']
        self.assertIsNotNone(entrenamientos[0]['fecha'])

    def test_dar_reporte_fechas_campo_ejercicios_realizados(self):
        persona = self.__crear_persona()
        ejercicio = self.__crear_ejercicio()
        self.__crear_entrenamiento(persona, ejercicio)
        reporte = self.logica.dar_reporte(id_persona=persona.id)
        entrenamientos = reporte['estadisticas']['entrenamientos']
        self.assertIsNotNone(entrenamientos[0]['repeticiones'])

    def test_dar_reporte_fechas_campo_calorias(self):
        persona = self.__crear_persona()
        ejercicio = self.__crear_ejercicio()
        self.__crear_entrenamiento(persona, ejercicio)
        reporte = self.logica.dar_reporte(id_persona=persona.id)
        entrenamientos = reporte['estadisticas']['entrenamientos']
        self.assertIsNotNone(entrenamientos[0]['calorias'])

    def test_dar_reporte_fechas_campo_total_repeticiones(self):
        persona = self.__crear_persona()
        ejercicio = self.__crear_ejercicio()
        self.__crear_entrenamiento(persona, ejercicio)
        reporte = self.logica.dar_reporte(id_persona=persona.id)
        total_repeticiones = reporte['estadisticas']['total_repeticiones']
        self.assertIsNotNone(total_repeticiones)

    def test_dar_reporte_total_repeticiones_igual_suma_repeticiones(self):
        persona = self.__crear_persona()
        ejercicio = self.__crear_ejercicio()
        self.__crear_entrenamientos(
            persona=persona,
            ejercicio=ejercicio,
            cantidad=3
        )
        reporte = self.logica.dar_reporte(id_persona=persona.id)
        total_repeticiones = reporte['estadisticas']['total_repeticiones']
        entrenamientos = reporte['estadisticas']['entrenamientos']
        suma_repeticiones = 0
        for entrenamiento in entrenamientos:
            suma_repeticiones += entrenamiento['repeticiones']
        self.assertEqual(total_repeticiones, suma_repeticiones)

    def test_dar_reporte_total_calorias_igual_suma_calorias(self):
        persona = self.__crear_persona()
        ejercicio = self.__crear_ejercicio()
        self.__crear_entrenamientos(
            persona=persona,
            ejercicio=ejercicio,
            cantidad=3
        )
        reporte = self.logica.dar_reporte(id_persona=persona.id)
        total_calorias = reporte['estadisticas']['total_calorias']
        entrenamientos = reporte['estadisticas']['entrenamientos']
        suma_calorias = 0
        for entrenamiento in entrenamientos:
            suma_calorias += entrenamiento['calorias']
        self.assertEqual(total_calorias, suma_calorias)

    def test_dar_reporte_campo_persona_contiene_nombre_no_vacio(self):
        persona = self.__crear_persona()
        ejercicio = self.__crear_ejercicio()
        self.__crear_entrenamiento(persona, ejercicio)
        reporte = self.logica.dar_reporte(id_persona=persona.id)

        self.assertIsNotNone(reporte['persona'])
        self.assertNotEqual(reporte['persona']['nombre'], "")

    def test_dar_reporte_dos_entrenamietos_misma_fecha_diferente_ejercicio(self):
        persona = self.__crear_persona()
        ejercicio1 = self.__crear_ejercicio()
        ejercicio2 = self.__crear_ejercicio()
        self.__crear_entrenamiento(
            persona=persona,
            ejercicio=ejercicio1
        )
        self.__crear_entrenamiento(
            persona=persona,
            ejercicio=ejercicio2
        )
        reporte = self.logica.dar_reporte(id_persona=persona.id)
        total_repeticiones = reporte['estadisticas']['total_repeticiones']
        entrenamientos = reporte['estadisticas']['entrenamientos']
        suma_repeticiones = 0
        for entrenamiento in entrenamientos:
            suma_repeticiones += entrenamiento['repeticiones']
        self.assertEqual(total_repeticiones, suma_repeticiones)

class CrearEntrenamiento(unittest.TestCase):
    def setUp(self):
        self.session = session
        self.logica = Logica()
        self.__crear_ejercicios_persona_1()

    def __crear_ejercicios_persona_1(self):
        ejercicio1 = Ejercicio(
            nombre="Sentadillas",
            descripcion="Con el peso en la parte posterior subir y bajar",
            enlaceVideoYoutube="http://www.ejemplo.com/sentadillas",
            caloriasPorRepeticion=150
        )

        ejercicio2 = Ejercicio(
            nombre="Flexiones",
            descripcion="Ejercicio para fortalecer el pecho y brazos",
            enlaceVideoYoutube="http://www.ejemplo.com/flexiones",
            caloriasPorRepeticion=120
        )

        persona1 = Persona(
            nombre='Camilo',
            apellido='Lesmes',
            talla=175,
            peso=70,
            edad=30,
            medidaBrazos=30,
            medidaPecho=95,
            medidaAbdomen=80,
            medidaCintura=75,
            medidaPiernas=95,
            fechaDeInicioEntrenamiento='2023-09-14',
            fechaDeFinEntrenamiento='2023-09-20',
            razonDeFinEntrenamiento='Objetivo alcanzado'
        )


        session.add_all([persona1, ejercicio1, ejercicio2])
        session.commit()

    def __agregar_persona(self):
        persona = Persona(
            nombre='Juan',
            apellido='Perez',
            talla=175,
            peso=70,
            edad=30,
            medidaBrazos=30,
            medidaPecho=95,
            medidaAbdomen=80,
            medidaCintura=75,
            medidaPiernas=95,
            fechaDeInicioEntrenamiento='2023-01-01',
            fechaDeFinEntrenamiento='',
            razonDeFinEntrenamiento=''
        )

        self.session.add(persona)

        self.session.commit()
        self.session.close()
        return persona

    def __agregar_ejercicio(self):
        ejercicio = Ejercicio(
            nombre="Sentadillas",
            descripcion="Con el peso en la parte posterior subir y bajar",
            enlaceVideoYoutube="http://www.ejemplo.com/sentadillas",
            caloriasPorRepeticion=150
        )

        self.session.add(ejercicio)

        self.session.commit()
        self.session.close()

        return ejercicio

    def tearDown(self):
        metadata = MetaData()
        tabla_ejercicio = Table('Ejercicio', metadata)
        session.execute(tabla_ejercicio.delete())
        tabla_persona = Table('Persona', metadata)
        session.execute(tabla_persona.delete())
        tabla_entrenamiento = Table('EjercicioEntrenamiento', metadata)
        session.execute(tabla_entrenamiento.delete())
        session.commit()
        session.close()
        self.logica = None

    def test_validar_persona(self):
        error = self.logica.validar_crear_editar_entrenamiento(None, None, None, None, None)
        self.assertEqual("Debe seleccionar una persona", error)

    def test_validar_ejercicio(self):
        persona = self.__agregar_persona()
        error = self.logica.validar_crear_editar_entrenamiento(persona, None, None, None, None)
        self.assertEqual("Debe seleccionar un ejercicio", error)

    def test_validar_fecha(self):
        persona = self.__agregar_persona()
        ejercicio = self.__agregar_ejercicio()
        error = self.logica.validar_crear_editar_entrenamiento(persona, ejercicio, None, None, None)
        self.assertEqual("Debe ingresar una fecha", error)

    def test_validar_fecha_formato(self):
        persona = self.__agregar_persona()
        ejercicio = self.__agregar_ejercicio()
        error = self.logica.validar_crear_editar_entrenamiento(persona, ejercicio, "30-09-2023", None, None)
        self.assertEqual("Formato de fecha incorrecto", error)

    def test_validar_repeticiones(self):
        persona = self.__agregar_persona()
        ejercicio = self.__agregar_ejercicio()
        error = self.logica.validar_crear_editar_entrenamiento(persona, ejercicio, "2023-09-14", None, None)
        self.assertEqual("Debe ingresar una cantidad de repeticiones", error)

    def test_validar_repeticiones_diferente_numero(self):
        persona = self.__agregar_persona()
        ejercicio = self.__agregar_ejercicio()
        error = self.logica.validar_crear_editar_entrenamiento(persona, ejercicio, "2023-09-14", "a", None)
        self.assertEqual("La cantidad de repeticiones debe ser un número", error)

    def test_validar_tiempo(self):
        persona = self.__agregar_persona()
        ejercicio = self.__agregar_ejercicio()
        error = self.logica.validar_crear_editar_entrenamiento(persona, ejercicio, "2023-09-14", "20", None)
        self.assertEqual("Debe ingresar un tiempo de entrenamiento", error)

    def test_validar_tiempo_diferente_numero(self):
        persona = self.__agregar_persona()
        ejercicio = self.__agregar_ejercicio()
        error = self.logica.validar_crear_editar_entrenamiento(persona, ejercicio, "2023-09-14", "20", "a")
        self.assertEqual("El tiempo de entrenamiento debe ser un número", error)

    def test_validar_crear_entrenamiento_correctamente(self):
        persona = self.__agregar_persona()
        ejercicio = self.__agregar_ejercicio()
        error = self.logica.validar_crear_editar_entrenamiento(persona, ejercicio, "2023-09-14", "20", "20")
        self.assertEqual("", error)

    def test_crear_entrenamiento_correctamente(self):
        self.__agregar_persona()
        persona = self.logica.dar_personas()[0]
        self.__agregar_ejercicio()
        ejercicio = self.logica.dar_ejercicios()[0]
        fecha = datetime.now()
        repeticiones = "20"
        tiempo = "20"

        error = self.logica.validar_crear_editar_entrenamiento(persona, ejercicio, fecha, repeticiones, tiempo)
        self.assertEqual("", error)

        self.logica.crear_entrenamiento(persona, ejercicio, datetime.now(), repeticiones, tiempo)
        metadata = MetaData()
        tabla_entrenamiento = Table('EjercicioEntrenamiento', metadata)
        contador = self.session.query(func.count()).select_from(tabla_entrenamiento).scalar()
        self.assertEqual(1, contador)

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main(testRunner=runner)