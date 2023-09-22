'''
Esta clase es tan sólo un mock con datos para probar la interfaz
'''
from src.logica.FachadaEnForma import FachadaEnForma


class LogicaMock(FachadaEnForma):


    def __init__(self):
        #Este constructor contiene los datos falsos para probar la interfaz
        self.personas = [{'nombre': 'Federico', 'apellido': 'Contreras', 'edad': 15, 'talla': 1.53, 'peso': 50, 'brazo': 15, 'pecho': 80, 'cintura': 70, 'pierna': 35, 'fecha_retiro': '', 'razon_retiro': ''},
                         {'nombre': 'Angelica', 'apellido': 'Mora', 'edad': 42, 'talla': 1.90, 'peso': 75, 'brazo': 18, 'pecho': 95, 'cintura': 76, 'pierna': 40, 'fecha_retiro': '2023-03-30', 'razon_retiro': 'Incapacidad'},
                         {'nombre': 'Julian', 'apellido': 'Salazar', 'edad': 30, 'talla': 1.69, 'peso': 59, 'brazo': 17, 'pecho': 69, 'cintura': 60, 'pierna': 28, 'fecha_retiro': '2023-01-18', 'razon_retiro': 'Cambio de instructor'},
                         {'nombre': 'Bruno', 'apellido': 'Galan', 'edad': 26, 'talla': 1.53, 'peso': 60, 'brazo': 16, 'pecho': 72, 'cintura': 54, 'pierna': 20, 'fecha_retiro': '', 'razon_retiro': ''},
                        ]

        self.ejercicios = [
            {'nombre': 'Press de pierna', 'descripcion': 'Ejercicio de entrenamiento con pesas en el que el individuo empuja un peso o una resistencia con las piernas', 'youtube': 'https://www.youtube.com/watch?v=zac9BPZiUTQ', 'calorias': 120}, \
            {'nombre': 'Sentadilla', 'descripcion': 'Ejercicio de fuerza en el que se baja la cadera desde una posición de pie y luego vuelve a levantarse.', 'youtube': 'https://www.youtube.com/watch?v=l7aszLSPCVg', 'calorias': 80}, \
            {'nombre': 'Abducción de cadera', 'descripcion': 'Mover la pierna derecha hacia la derecha o alejarla del cuerpo y viceversa', 'youtube': 'https://www.youtube.com/watch?v=dILxTvY88uI', 'calorias': 90}
        ]

        self.entrenamientos = [{'persona': 'Federico', 'ejercicio': 'Press de pierna', 'fecha': '2023-01-18', 'repeticiones': 15, 'tiempo': 20},
                               {'persona': 'Federico', 'ejercicio': 'Sentadilla', 'fecha': '2023-01-18', 'repeticiones': 12, 'tiempo': 5},
                               {'persona': 'Federico', 'ejercicio': 'Press de pierna', 'fecha': '2023-03-11', 'repeticiones': 15, 'tiempo': 20},
                               {'persona': 'Bruno', 'ejercicio': 'Press de pierna', 'fecha': '2023-01-18', 'repeticiones': 15, 'tiempo': 30},
                               {'persona': 'Bruno', 'ejercicio': 'Sentadilla', 'fecha': '2023-07-02', 'repeticiones': 10, 'tiempo': 5}
                               ]

        self.reportes = [{'persona': 'Federico', 'imc': 21.4, 'clasificacion': 'Peso saludable', 'entrenamientos': [{'fecha': '2023-01-18', 'repeticiones': 27, 'calorias': 2760}, {'fecha': '2023-03-11', 'repeticiones': 15, 'calorias': 1800 }], 'total_repeticiones': 42, 'total_calorias': 4560},
                         {'persona': 'Bruno', 'imc': 25.6, 'clasificacion': 'Sobrepeso', 'entrenamientos': [{'fecha': '2023-01-18', 'repeticiones': 15, 'calorias': 1800}, {'fecha': '2023-07-02', 'repeticiones': 10, 'calorias': 800 }], 'total_repeticiones': 25, 'total_calorias': 2600}
                         ]


    def dar_personas(self):
        return self.personas.copy()

    def dar_persona(self, id_persona):
        return self.personas[id_persona].copy()

    def validar_crear_editar_persona(self, id_persona, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):
        return ""

    def crear_persona(self, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):
        self.personas.append({'nombre': nombre, 'apellido': apellido, 'edad': edad, 'talla': talla, \
                           'peso': peso, 'brazo': brazo, 'pecho': pecho, 'cintura': cintura, 'pierna': pierna, \
                           'fecha_retiro': '', 'razon_retiro': '' })

    def editar_persona(self, id_persona, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):
        self.personas[id_persona]['nombre'] = nombre
        self.personas[id_persona]['apellido'] = apellido
        self.personas[id_persona]['edad'] = edad
        self.personas[id_persona]['talla'] = talla
        self.personas[id_persona]['peso'] = peso
        self.personas[id_persona]['brazo'] = brazo
        self.personas[id_persona]['pecho'] = pecho
        self.personas[id_persona]['cintura'] = cintura
        self.personas[id_persona]['pierna'] = pierna

    def eliminar_persona(self, id_persona):
        del self.personas[id_persona]

    def dar_ejercicios(self):
        return self.ejercicios.copy()

    def validar_crear_editar_ejercicio(self, nombre, descripcion, enlace, calorias):
        return ""

    def crear_ejercicio(self, nombre, descripcion, enlace, calorias):
        self.ejercicios.append({'nombre': nombre, 'descripcion': descripcion, 'youtube': enlace, 'calorias': calorias})

    def editar_ejercicio(self,id_ejercicio, nombre, descripcion, enlace, calorias):
        self.ejercicios[id_ejercicio]['nombre']= nombre
        self.ejercicios[id_ejercicio]['descripcion'] = descripcion
        self.ejercicios[id_ejercicio]['enlace'] = enlace
        self.ejercicios[id_ejercicio]['calorias'] = calorias

    def eliminar_ejercicio(self, id_ejercicio):
        del self.ejercicios[id_ejercicio]

    def dar_entrenamientos(self, id_persona):
        persona = self.dar_persona(id_persona)
        return list(filter(lambda x: x['persona'] == persona['nombre'], self.entrenamientos))
        return self.entrenamientos.copy()

    def validar_crear_editar_entrenamiento(self, persona, ejercicio, fecha, repeticiones, tiempo):
        return ""

    def crear_entrenamiento(self, persona, ejercicio, fecha, repeticiones, tiempo):
        self.entrenamientos.append({'persona': persona['nombre'], 'ejercicio': ejercicio, 'fecha': fecha, 'repeticiones': repeticiones, 'tiempo': tiempo})

    def editar_entrenamiento(self, id_entrenamiento, persona, ejercicio, fecha, repeticiones, tiempo):
        entrenamientos_persona = list(filter(lambda x: x['persona'] == persona['nombre'], self.entrenamientos))
        entrenamientos_persona[id_entrenamiento]['ejercicio'] = ejercicio
        entrenamientos_persona[id_entrenamiento]['fecha'] = fecha
        entrenamientos_persona[id_entrenamiento]['repeticiones'] = repeticiones
        entrenamientos_persona[id_entrenamiento]['tiempo'] = tiempo

    def eliminar_entrenamiento(self, id_entrenamiento, persona):
        entrenamientos_persona = list(filter(lambda x: x['persona'] == persona['nombre'], self.entrenamientos))
        entrenamientos_diferentes = list(filter(lambda x: x['persona'] != persona['nombre'], self.entrenamientos))
        entrenamientos_persona.pop(id_entrenamiento)
        self.entrenamientos = entrenamientos_diferentes + entrenamientos_persona

    def validar_dejar_de_entrenar_persona(self, id_persona, fecha, razon):
        return ""

    def dejar_de_entrenar_persona(self, id_persona, fecha, razon):
        self.personas[id_persona]['fecha_retiro'] = fecha
        self.personas[id_persona]['razon_retiro'] = razon

    def dar_reporte(self, id_persona):
        persona = self.dar_persona(0)
        estadisticas = list(filter(lambda x: x['persona'] == persona['nombre'], self.reportes))[0]
        self.reportes.copy()
        return {'persona': persona, 'estadisticas': estadisticas}
