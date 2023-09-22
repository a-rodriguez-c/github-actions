from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class VistaPersona(QWidget):
    #Ventana de persona

    def __init__(self,interfaz):
        """
        Constructor de la ventana
        """   
        super().__init__()

        self.titulo = 'En Forma- Persona'
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.interfaz=interfaz

        self.width = 500
        self.height = 450
        self.inicializar_GUI()
        self.show()
       

    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))

        self.distribuidor_base = QVBoxLayout(self)

        self.widget_id = QWidget()
        self.distribuidor_persona = QGridLayout()
        self.widget_id.setLayout(self.distribuidor_persona)
        self.distribuidor_base.addWidget(self.widget_id, Qt.AlignTop)
        numero_fila = 0

        etiqueta_nombre_persona=QLabel("Nombre")
        self.distribuidor_persona.addWidget(etiqueta_nombre_persona, numero_fila, 0)

        self.texto_nombre_persona=QLineEdit(self)
        self.distribuidor_persona.addWidget(self.texto_nombre_persona, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_apellidos_persona=QLabel("Apellidos")
        self.distribuidor_persona.addWidget(etiqueta_apellidos_persona, numero_fila, 0)

        self.texto_apellidos_persona=QLineEdit(self)
        self.distribuidor_persona.addWidget(self.texto_apellidos_persona, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_edad = QLabel("Edad")
        self.distribuidor_persona.addWidget(etiqueta_edad, numero_fila, 0)

        self.texto_edad = QLineEdit(self)
        self.distribuidor_persona.addWidget(self.texto_edad, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_talla = QLabel("Talla (m)")
        self.distribuidor_persona.addWidget(etiqueta_talla, numero_fila, 0)

        self.texto_talla = QLineEdit(self)
        self.distribuidor_persona.addWidget(self.texto_talla, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_peso = QLabel("Peso (Kg)")
        self.distribuidor_persona.addWidget(etiqueta_peso, numero_fila, 0)

        self.texto_peso = QLineEdit(self)
        self.distribuidor_persona.addWidget(self.texto_peso, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_brazo = QLabel("Brazo (cm)")
        self.distribuidor_persona.addWidget(etiqueta_brazo, numero_fila, 0)

        self.texto_brazo = QLineEdit(self)
        self.distribuidor_persona.addWidget(self.texto_brazo, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_pecho = QLabel("Pecho (cm)")
        self.distribuidor_persona.addWidget(etiqueta_pecho, numero_fila, 0)

        self.texto_pecho = QLineEdit(self)
        self.distribuidor_persona.addWidget(self.texto_pecho, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_cintura = QLabel("Cintura (cm)")
        self.distribuidor_persona.addWidget(etiqueta_cintura, numero_fila, 0)

        self.texto_cintura = QLineEdit(self)
        self.distribuidor_persona.addWidget(self.texto_cintura, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_pierna = QLabel("Pierna (cm)")
        self.distribuidor_persona.addWidget(etiqueta_pierna, numero_fila, 0)

        self.texto_pierna = QLineEdit(self)
        self.distribuidor_persona.addWidget(self.texto_pierna, numero_fila, 1)

        #Creación de la caja con los botones
        self.widget_botones = QWidget()
        self.distribuidor_botones = QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)
        self.distribuidor_base.addWidget(self.widget_botones, Qt.AlignTop)

       #Creación de los botones con las diferentes operaciones
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(120, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.distribuidor_botones.addWidget(self.btn_volver, 0, 0, Qt.AlignCenter)
        self.btn_volver.clicked.connect(self.volver)

        self.btn_guardar_persona = QPushButton("Guardar persona", self)
        self.btn_guardar_persona.setFixedSize(120, 40)
        self.btn_guardar_persona.setToolTip("Guardar persona")
        self.btn_guardar_persona.setIcon(QIcon("src/recursos/floppy-disk.png"))
        self.distribuidor_botones.addWidget(self.btn_guardar_persona, 0, 2, Qt.AlignCenter)
        self.btn_guardar_persona.clicked.connect(self.guardar_cambios)

    def mostrar_persona(self, persona):
        self.persona=persona
        if (self.persona!=None):
            self.texto_nombre_persona.setText(self.persona["nombre"])
            self.texto_apellidos_persona.setText(self.persona["apellido"])
            self.texto_edad.setText(str(self.persona["edad"]))
            self.texto_talla.setText(str(self.persona["talla"]))
            self.texto_peso.setText(str(self.persona["peso"]))
            self.texto_brazo.setText(str(self.persona["brazo"]))
            self.texto_pecho.setText(str(self.persona["pecho"]))
            self.texto_cintura.setText(str(self.persona["cintura"]))
            self.texto_pierna.setText(str(self.persona["pierna"]))

    def guardar_cambios(self):
        """
        Esta función guarda los cambios de una persona (editando o guardando registros)
        """
        resultado = self.interfaz.guardar_persona(self.texto_nombre_persona.text(), self.texto_apellidos_persona.text(),
                                                  self.texto_edad.text(), self.texto_talla.text(),
                                                  self.texto_peso.text(),
                                                  self.texto_brazo.text(), self.texto_pecho.text(),
                                                  self.texto_cintura.text(),
                                                  self.texto_pierna.text())
        if resultado == "":
            self.hide()
            self.interfaz.mostrar_vista_lista_personas()
        else:
            self.error_id(resultado)

    def volver(self):
        """
        Esta función permite volver a la lista de personas
        """    
        self.hide()
        self.interfaz.mostrar_vista_lista_personas()

    def error_id(self, error):
        mensaje_error=QMessageBox()
        mensaje_error.setIcon(QMessageBox.Question)
        mensaje_error.setText("Error: " + error)
        mensaje_error.setWindowTitle("Error al guardar")
        mensaje_error.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))
        mensaje_error.setStandardButtons(QMessageBox.Ok ) 
        respuesta=mensaje_error.exec_()

    def closeEvent(self, event):
        self.hide()
        self.interfaz.mostrar_vista_lista_personas()
        event.accept()
