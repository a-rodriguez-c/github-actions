from datetime import datetime
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class VistaDejarDeEntrenarPersona(QWidget):
    #Ventana para dejar de entrenar a una persona

    def __init__(self,principal):
        """
        Constructor de la ventana
        """   
        super().__init__()

        self.titulo = 'En Forma- Dejar de entrenar'
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.interfaz=principal

        self.width = 500
        self.height = 400
        self.inicializar_GUI()
        self.show()
       

    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))

        self.distribuidor_base = QVBoxLayout(self)

        self.widget_login = QWidget()
        self.distribuidor_dejar_de_entrenar_persona = QGridLayout()
        self.widget_login.setLayout(self.distribuidor_dejar_de_entrenar_persona)
        self.distribuidor_base.addWidget(self.widget_login, Qt.AlignTop)
        numero_fila = 0

        etiqueta_fecha = QLabel("Fecha")
        self.distribuidor_dejar_de_entrenar_persona.addWidget(etiqueta_fecha, numero_fila, 0)

        self.fecha = QDateEdit(self)
        self.fecha.setDisplayFormat("yyyy-MM-dd")
        self.fecha.setDate(datetime.now())
        self.distribuidor_dejar_de_entrenar_persona.addWidget(self.fecha, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_razon=QLabel("Razón")
        self.distribuidor_dejar_de_entrenar_persona.addWidget(etiqueta_razon, numero_fila, 0)

        self.texto_razon = QTextEdit(self)
        self.texto_razon.setMinimumHeight(150)
        self.distribuidor_dejar_de_entrenar_persona.addWidget(self.texto_razon, numero_fila, 1)

        #Creación de la caja con los botones
        self.widget_botones = QWidget()
        self.distribuidor_botones = QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)
        self.distribuidor_base.addWidget(self.widget_botones, Qt.AlignTop)

       #Creación de los botones con las diferentes operaciones
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(150, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.distribuidor_botones.addWidget(self.btn_volver, 0, 0, Qt.AlignCenter)
        self.btn_volver.clicked.connect(self.volver)

        self.btn_guardar_retiro = QPushButton("Guardar", self)
        self.btn_guardar_retiro.setFixedSize(150, 40)
        self.btn_guardar_retiro.setToolTip("Guardar")
        self.btn_guardar_retiro.setIcon(QIcon("src/recursos/floppy-disk.png"))
        self.distribuidor_botones.addWidget(self.btn_guardar_retiro, 0, 2, Qt.AlignCenter)
        self.btn_guardar_retiro.clicked.connect(self.guardar_cambios)

    def mostrar_dejar_de_entrenar(self, persona):
        self.persona = persona
        if self.persona["fecha_retiro"] != "":
            self.fecha.setDate(QtCore.QDate.fromString(str(self.persona["fecha_retiro"]), "yyyy-MM-dd"))
            self.fecha.setDisabled(True)
            self.texto_razon.setText(str(persona["razon_retiro"]))
            self.texto_razon.setDisabled(True)
            self.btn_guardar_retiro.setDisabled(True)

    def guardar_cambios(self):
        """
        Esta función guarda los cambios cuando un entrenador deja de entrenar a una persona
        """
        resultado = self.interfaz.guardar_retiro_persona(self.fecha.text(), self.texto_razon.toPlainText())
        if resultado == "":
            self.hide()
            self.interfaz.mostrar_vista_lista_personas()
        else:
            self.error(resultado)

    def volver(self):
        """
        Esta función permite volver a la lista de personas
        """
        self.hide()
        self.interfaz.mostrar_vista_lista_personas()

    def error(self, error):
        mensaje_error=QMessageBox()
        mensaje_error.setIcon(QMessageBox.Question)
        mensaje_error.setText("Error: " + str(error))
        mensaje_error.setWindowTitle("Error al guardar")
        mensaje_error.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))
        mensaje_error.setStandardButtons(QMessageBox.Ok ) 
        respuesta=mensaje_error.exec_()

    def closeEvent(self, event):
        self.hide()
        self.interfaz.mostrar_vista_lista_personas()
        event.accept()
