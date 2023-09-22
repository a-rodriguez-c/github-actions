'''
Esta clase es la fachada con los métodos a implementar en la lógica
'''
class FachadaEnForma:

    def dar_personas(self):
        ''' Retorna la lista de personas registradas en el sistema
        Retorna:
            (list): La lista con los dict o los objetos de personas
        '''
        raise NotImplementedError("Método no implementado")

    def dar_persona(self, id_persona):
        ''' Retorna una persona a partir de su identificador
        Parámetros:
            id_persona (int): El identificador de la persona a retornar
        Retorna:
            (dict): La persona identificada con el id_persona recibido como parámetro
        '''
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_persona(self, id_persona, nombre, apellido, edad, talla, peso, brazo, pecho, cintura,
                                     pierna):
        ''' Valida que una persona se pueda crear o editar
        Parámetros:
            nombre (string): El nombre de la persona
            apellido (string): El apellido de la persona
            edad (string): La edad de la persona
            talla (string): La talla de la persona
            peso (string): El peso de la persona en Kg
            brazo (string): La medida del diametro del brazo de la persona en cm
            pecho (string): La medida del pecho de la persona en cm
            cintura (string): La medida de la cintura de la persona en cm
            pierna (string): La medida del diametro de la pierna de la persona en cm
        Retorna:
            (string): El mensaje de error generado al presentarse errores en la
            validación o una cadena de caracteres vacía si no hay errores.
        '''
        raise NotImplementedError("Método no implementado")

    def crear_persona(self, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):
        ''' Crea una persona
        Parámetros:
            nombre (string): El nombre de la persona
            apellido (string): El apellido de la persona
            edad (string): La edad de la persona
            talla (string): La talla de la persona
            peso (string): El peso de la persona en Kg
            brazo (string): La medida del diametro del brazo de la persona en cm
            pecho (string): La medida del pecho de la persona en cm
            cintura (string): La medida de la cintura de la persona en cm
            pierna (string): La medida del diametro de la pierna de la persona en cm
        '''
        raise NotImplementedError("Método no implementado")

    def editar_persona(self, id_persona, nombre, apellido, edad, talla, peso, brazo, pecho, cintura, pierna):
        ''' Edita una persona
        Parámetros:
            id_persona(int): El identificador de la persona que se va a editar
            nombre (string): El nombre de la persona
            apellido (string): El apellido de la persona
            edad (string): La edad de la persona
            talla (string): La talla de la persona
            peso (string): El peso de la persona en Kg
            brazo (string): La medida del diametro del brazo de la persona en cm
            pecho (string): La medida del pecho de la persona en cm
            cintura (string): La medida de la cintura de la persona en cm
            pierna (string): La medida del diametro de la pierna de la persona en cm
        '''
        raise NotImplementedError("Método no implementado")

    def eliminar_persona(self, id_persona):
        ''' Elimina una persona de la lista de personas
        Parámetros:
            id_persona (int): El identificador de la persona que se desea eliminar
        '''
        raise NotImplementedError("Método no implementado")

    def dar_ejercicios(self):
        ''' Retorna la lista de ejercicios
        Retorna:
            (list): La lista con los dict o los objetos de los ejercicios
        '''
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_ejercicio(self, nombre, descripcion, enlace, calorias):
        ''' Valida que un ejercicio se pueda crear o editar
        Parámetros:
            nombre (string): El nombre del ejercicio
            descripcion (string): La descripción del ejercicio
            enlace (string): El enlace al video del ejercicio en YouTube
            calorias (string): El número de calorias consumidas por repetición del ejercicio
        Retorna:
            (string): El mensaje de error generado al presentarse errores en la
            validación o una cadena de caracteres vacía si no hay errores.
        '''
        raise NotImplementedError("Método no implementado")

    def crear_ejercicio(self, nombre, descripcion, enlace, calorias):
        ''' Crea un ejercicio
        Parámetros:
            nombre (string): El nombre del ejercicio
            descripcion (string): La descripción del ejercicio
            enlace (string): El enlace al video del ejercicio en YouTube
            calorias (string): El número de calorias consumidas por repetición del ejercicio
        '''
        raise NotImplementedError("Método no implementado")

    def editar_ejercicio(self, id_ejercicio, nombre, descripcion, enlace, calorias):
        ''' Edita un ejercicio
        Parámetros:
            id_ejercicio(int): El identificador del ejercicio que se va a editar
            nombre (string): El nombre del ejercicio
            descripcion (string): La descripción del ejercicio
            enlace (string): El enlace al video del ejercicio en YouTube
            calorias (string): El número de calorias consumidas por repetición del ejercicio
        '''
        raise NotImplementedError("Método no implementado")

    def eliminar_ejercicio(self, id_ejercicio):
        ''' Elimina un ejercicio de la lista de ejercicios
        Parámetros:
            id_ejercicio (int): El identificador del ejercicio que se desea eliminar
        '''
        raise NotImplementedError("Método no implementado")

    def dar_entrenamientos(self, id_persona):
        ''' Retorna la lista de entrenamientos de una persona
        Parámetros:
            id_persona (int): El identificador de la persona a consultar
        Retorna:
            (list): La lista con los dict o los objetos de los entrenamientos realizados por una persona
        '''
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_entrenamiento(self, persona, ejercicio, fecha, repeticiones, tiempo):
        ''' Valida que se pueda crear o editar un entrenamiento
        Parámetros:
            persona (dict): dict con los datos de la persona
            ejercicio (string): El nombre del ejercicio realizado por la persona
            fecha (string): La fecha de realización del ejercicio
            repeticiones (string): El número de repeticiones hechas del ejercicio
            tiempo (string): El tiempo gastado
        Retorna:
            (string): El mensaje de error generado al presentarse errores en la
            validación o una cadena de caracteres vacía si no hay errores.
        '''
        raise NotImplementedError("Método no implementado")

    def crear_entrenamiento(self, persona, ejercicio, fecha, repeticiones, tiempo):
        ''' Crea un entrenamiento
        Parámetros:
            persona (dict): dict con los datos de la persona
            ejercicio (string): El nombre del ejercicio realizado por la persona
            fecha (string): La fecha de realización del ejercicio
            repeticiones (string): El número de repeticiones hechas del ejercicio
            tiempo (string): El tiempo gastado
        '''
        raise NotImplementedError("Método no implementado")

    def editar_entrenamiento(self, id_entrenamiento, persona, ejercicio, fecha, repeticiones, tiempo):
        ''' Edita un entrenamiento
        Parámetros:
            id_entrenamiento(int): El identificador del entrenamiento que se va a editar
            persona (dict): dict con los datos de la persona
            ejercicio (string): El nombre del ejercicio realizado por la persona
            fecha (string): La fecha de realización del ejercicio
            repeticiones (string): El número de repeticiones hechas del ejercicio
            tiempo (string): El tiempo gastado
        '''
        raise NotImplementedError("Método no implementado")

    def eliminar_entrenamiento(self, id_entrenamiento, persona):
        ''' Elimina un entrenamiento de la lista de entrenamientos realizados por una persona
        Parámetros:
            id_entrenamiento (int): El identificador del entrenamiento que se desea eliminar
            persona (dict): dict con los datos de la persona
        '''
        raise NotImplementedError("Método no implementado")

    def validar_dejar_de_entrenar_persona(self, id_persona, fecha, razon):
        ''' Valida que se pueda dejar de entrenar a una persona
        Parámetros:
            id_persona (int): El identificador de la persona que se desea dejar de entrenar
            fecha (string): La fecha en que dejó de entrenar
            razon (string): La descripción del motivo por el cual dejó de entrenar
        Retorna:
            (string): El mensaje de error generado al presentarse errores en la
            validación o una cadena de caracteres vacía si no hay errores.
        '''
        raise NotImplementedError("Método no implementado")

    def dejar_de_entrenar_persona(self, id_persona, fecha, razon):
        ''' Deja de entrenar a una persona
        Parámetros:
            id_persona (int): El identificador de la persona que se desea dejar de entrenar
            fecha (string): La fecha en que dejó de entrenar
            razon (string): La descripción del motivo por el cual dejó de entrenar
        '''
        raise NotImplementedError("Método no implementado")

    def dar_reporte(self, id_persona):
        ''' Genera la información para el reporte de entrenamientos de una persona
        Parámetros:
            id_persona (int): El identificador de la persona
        Retorna:
            (dict): Un mapa con la información del reporte
        '''
        return NotImplementedError("Método no implementado")
