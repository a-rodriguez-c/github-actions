from datetime import datetime
from PyQt5 import QtCore

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class VistaCrearEntrenamiento(QDialog):
    # Diálogo para crear o editar el entrenamiento de una persona

    def __init__(self, entrenamiento, interfaz, ejercicios):
        """
        Constructor del diálogo
        """
        super().__init__()

        self.interfaz = interfaz
        self.ejercicios = ejercicios

        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))

        self.resultado = ""

        self.widget_dialogo = QListWidget()

        distribuidor_dialogo = QGridLayout()
        self.setLayout(distribuidor_dialogo)
        numero_fila = 0

        # Si se va a crear un nuevo entrenamiento o se va a editar, usamos el mismo diálogo

        titulo = ""
        if (entrenamiento == None):
            titulo = "Nuevo entrenamiento"
        else:
            titulo = "Editar entrenamiento"

        self.setWindowTitle("En Forma- {}".format(titulo))

        # Creación de las etiquetas y los campos de texto
        etiqueta_ejercicio = QLabel("Ejercicio")
        distribuidor_dialogo.addWidget(etiqueta_ejercicio, numero_fila, 0)

        self.combobox_ejercicios = QComboBox(self)
        for ejercicio in self.ejercicios:
            self.combobox_ejercicios.addItem(ejercicio["nombre"])
        self.combobox_ejercicios.setCurrentIndex(0)
        distribuidor_dialogo.addWidget(self.combobox_ejercicios, numero_fila, 1, 1, 2)
        numero_fila = numero_fila + 1

        etiqueta_fecha = QLabel("Fecha")
        distribuidor_dialogo.addWidget(etiqueta_fecha, numero_fila, 0)

        self.fecha = QDateEdit(self)
        self.fecha.setDisplayFormat("yyyy-MM-dd")
        self.fecha.setDate(datetime.now())
        distribuidor_dialogo.addWidget(self.fecha, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_repeticiones = QLabel("Cantidad de repeticiones")
        distribuidor_dialogo.addWidget(etiqueta_repeticiones, numero_fila, 0)

        self.texto_repeticiones = QLineEdit(self)
        distribuidor_dialogo.addWidget(self.texto_repeticiones, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_tiempo = QLabel("Tiempo haciendo el ejercicio")
        distribuidor_dialogo.addWidget(etiqueta_tiempo, numero_fila, 0)

        self.texto_tiempo = QLineEdit(self)
        distribuidor_dialogo.addWidget(self.texto_tiempo, numero_fila, 1)
        numero_fila = numero_fila + 1

        # Creación de los botones para guardar o cancelar
        caja_botones = QGroupBox()
        caja_botones.setLayout(QHBoxLayout())
        caja_botones.setStyleSheet('''
                QGroupBox{border:none}''')

        self.btn_guardar = QPushButton("Guardar ejercicio de entrenamiento")
        caja_botones.layout().addWidget(self.btn_guardar)
        self.btn_guardar.clicked.connect(self.guardar)

        self.btn_cancelar = QPushButton("Cancelar")
        caja_botones.layout().addWidget(self.btn_cancelar)
        self.btn_cancelar.clicked.connect(self.cancelar)

        distribuidor_dialogo.addWidget(caja_botones, numero_fila, 0, 1, 2)

        # Si el diálogo se va a usar para editar, se pone la información correspondiente en los campos de texto
        if (entrenamiento != None):
            indice_ejercicio = self.combobox_ejercicios.findText(entrenamiento["ejercicio"])
            self.combobox_ejercicios.setCurrentIndex(indice_ejercicio)
            self.fecha.setDate(QtCore.QDate.fromString(str(entrenamiento["fecha"]), "yyyy-MM-dd"))
            self.texto_repeticiones.setText(str(entrenamiento["repeticiones"]))
            self.texto_tiempo.setText(str(entrenamiento["tiempo"]))

    def guardar(self):
        """
        Esta función envía la información de la solicitud de guardar los cambios
        """
        self.resultado = 1
        self.close()
        return self.resultado

    def cancelar(self):
        """
        Esta función envía la información de cancelación de la operación
        """
        self.resultado = 0
        self.close()
        return self.resultado
