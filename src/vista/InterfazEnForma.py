from PyQt5.QtWidgets import QApplication

from .VistaPersona import VistaPersona
from .VistaListaEjercicios import VistaListaEjercicios
from .VistaListaPersonas import VistaListaPersonas
from .VistaDejarDeEntrenarPersona import VistaDejarDeEntrenarPersona
from .VistaReporte import VistaReporte
from .VistaListaEntrenamientos import VistaListaEntrenamientos


class App_EnForma(QApplication):
    """
    Clase principal de la interfaz que coordina las diferentes vistas/ventanas de la aplicación
    """

    def __init__(self, sys_argv, logica):
        """
        Constructor de la interfaz. Debe recibir la lógica e iniciar la aplicación en la ventana principal.
        """
        super(App_EnForma, self).__init__(sys_argv)

        self.logica = logica
        self.mostrar_vista_lista_personas()

    def mostrar_vista_lista_personas(self):
        """
        Esta función inicializa la ventana de lista de personas
        """
        self.vista_lista_personas = VistaListaPersonas(self)
        self.vista_lista_personas.mostrar_personas(self.logica.dar_personas())

    def crear_persona(self):
        """
        Esta función muestra la ventana para crear una persona
        """
        self.mostrar_persona()

    def mostrar_persona(self, id_persona=-1):
        """
        Esta función muestra la ventana con la información de una persona
        """
        self.persona_actual = id_persona
        if id_persona != -1:
            self.vista_persona = VistaPersona(self)
            self.vista_persona.mostrar_persona(self.logica.dar_persona(self.persona_actual))
        else:
            self.vista_persona = VistaPersona(self)
            self.vista_persona.mostrar_persona(None)

    def guardar_persona(self, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):
        """
        Esta función permite crear una nueva persona o los cambios sobre una existente
        """
        validacion = self.logica.validar_crear_editar_persona(self.persona_actual, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna)
        if validacion == "":
            if self.persona_actual == -1:
                self.logica.crear_persona(nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna)
            else:
                self.logica.editar_persona(self.persona_actual, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna)
            self.vista_lista_personas.mostrar_personas(self.logica.dar_personas())
        return validacion

    def eliminar_persona(self, indice):
        """
        Esta función permite eliminar una persona
        """
        self.logica.eliminar_persona(indice)
        self.vista_lista_personas.mostrar_personas(self.logica.dar_personas())

    def mostrar_ejercicios(self):
        """
        Esta función muestra la ventana con la lista de ejercicios
        """
        self.vista_lista_ejercicios=VistaListaEjercicios(self)
        self.vista_lista_ejercicios.mostrar_ejercicios(self.logica.dar_ejercicios())

    def crear_ejercicio(self, nombre, descripcion, enlace, calorias):
        """
        Esta función permite crear un nuevo ejercicio
        """
        validacion = self.logica.validar_crear_editar_ejercicio(nombre, descripcion, enlace, calorias)
        if validacion == "":
            self.logica.crear_ejercicio(nombre, descripcion, enlace, calorias)
        else:
            self.vista_lista_ejercicios.error(validacion)
        self.vista_lista_ejercicios.mostrar_ejercicios(self.logica.dar_ejercicios())
        return validacion

    def editar_ejercicio(self, id, nombre, descripcion, enlace, calorias):
        """
        Esta función permite editar un ejercicio
        """
        validacion = self.logica.validar_crear_editar_ejercicio(nombre, descripcion, enlace, calorias)
        if validacion == "":
            self.logica.editar_ejercicio(id, nombre, descripcion, enlace, calorias)
        else:
            self.vista_lista_ejercicios.error(validacion)

    def eliminar_ejercicio(self, indice):
        """
        Esta función permite eliminar un ejercicio
        """
        self.logica.eliminar_ejercicio(indice)
        self.vista_lista_ejercicios.mostrar_ejercicios(self.logica.dar_ejercicios())

    def mostrar_entrenamientos(self, id_persona=-1):
        """
        Esta función muestra la ventana con la lista de entrenamientos de una persona
        """
        self.persona_actual = id_persona
        if id_persona != -1:
            persona = self.logica.dar_persona(id_persona)
            ejercicios = self.logica.dar_ejercicios()
            self.vista_lista_entrenamientos = VistaListaEntrenamientos(self, persona, ejercicios)
            self.vista_lista_entrenamientos.mostrar_entrenamientos(self.persona_actual,
                                                                   self.logica.dar_entrenamientos(self.persona_actual))
        else:
            self.vista_lista_entrenamientos = VistaListaEntrenamientos(self)
            self.vista_lista_entrenamientos.mostrar_entrenamientos(None)

    def crear_entrenamiento(self, id_persona, ejercicio, fecha, repeticiones, tiempo):
        """
        Esta función permite registrar un entrenamiento a una persona especifica
        """
        persona = self.logica.dar_persona(id_persona)
        validacion = self.logica.validar_crear_editar_entrenamiento(persona, ejercicio, fecha, repeticiones, tiempo)
        if validacion == "":
            self.logica.crear_entrenamiento(persona, ejercicio, fecha, repeticiones, tiempo)
        else:
            self.vista_lista_entrenamientos.error(validacion)
        self.mostrar_entrenamientos(id_persona)
        return validacion

    def editar_entrenamiento(self, id_entrenamiento, id_persona, ejercicio, fecha, repeticiones, tiempo):
        """
        Esta función permite editar un entrenamiento
        """
        persona = self.logica.dar_persona(id_persona)
        validacion = self.logica.validar_crear_editar_entrenamiento(persona, ejercicio, fecha, repeticiones, tiempo)
        if validacion == "":
            self.logica.editar_entrenamiento(id_entrenamiento,persona, ejercicio, fecha, repeticiones, tiempo)
        else:
            self.vista_lista_ejercicios.error(validacion)

    def eliminar_entrenamiento(self, id_entrenamiento, id_persona):
        """
        Esta función permite eliminar un entrenamiento
        """
        persona = self.logica.dar_persona(id_persona)
        self.logica.eliminar_entrenamiento(id_entrenamiento, persona)
        self.vista_lista_entrenamientos.mostrar_entrenamientos(self.persona_actual,
                                                               self.logica.dar_entrenamientos(self.persona_actual))

    def mostrar_ventana_dejar_de_entrenar_persona(self, id_persona=-1):
        """
        Esta función muestra la ventana para dejar de entrenar a una persona
        """
        self.persona_actual = id_persona
        self.vista_dejar_de_entrenar_persona = VistaDejarDeEntrenarPersona(self)
        self.vista_dejar_de_entrenar_persona.mostrar_dejar_de_entrenar(self.logica.dar_persona(self.persona_actual))

    def guardar_retiro_persona(self, fecha, razon):
        """
        Esta función guarda el retiro de una persona cuando el entrenador deja de entrenarla
        """
        validacion = self.logica.validar_dejar_de_entrenar_persona(self.persona_actual, fecha, razon)
        if validacion == "":
            self.logica.dejar_de_entrenar_persona(self.persona_actual, fecha, razon)
            self.vista_lista_personas.mostrar_personas(self.logica.dar_personas())
        return validacion

    def mostrar_reporte(self, id_persona):
        """
        Esta función muestra el reporte de entrenamientos de una persona
        """
        datos_reporte = self.logica.dar_reporte(id_persona)
        self.vista_reporte = VistaReporte(self, datos_reporte['persona'])
        self.vista_reporte.mostrar_datos(id_persona, datos_reporte)
