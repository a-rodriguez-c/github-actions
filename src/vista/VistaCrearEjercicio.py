
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class VistaCrearEjercicio(QDialog):
    # Diálogo para crear o editar un ejercicio

    def __init__(self, ejercicio, interfaz):
        """
        Constructor del diálogo
        """
        super().__init__()

        self.interfaz = interfaz

        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))

        self.resultado = ""

        self.widget_dialogo = QListWidget()

        distribuidor_dialogo = QGridLayout()
        self.setLayout(distribuidor_dialogo)
        numero_fila = 0

        # Si se va a crear un nuevo ejercicio o se va a editar, usamos el mismo diálogo

        titulo = ""
        if (ejercicio == None):
            titulo = "Nuevo ejercicio"
        else:
            titulo = "Editar ejercicio"

        self.setWindowTitle("En Forma- {}".format(titulo))

        # Creación de las etiquetas y los campos de texto
        etiqueta_nombre = QLabel("Nombre")
        distribuidor_dialogo.addWidget(etiqueta_nombre, numero_fila, 0)

        self.texto_nombre = QLineEdit(self)
        distribuidor_dialogo.addWidget(self.texto_nombre, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_descripcion = QLabel("Descripción")
        distribuidor_dialogo.addWidget(etiqueta_descripcion, numero_fila, 0)

        self.texto_descripcion = QTextEdit(self)
        self.texto_descripcion.setMinimumHeight(120)
        distribuidor_dialogo.addWidget(self.texto_descripcion, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_enlace = QLabel("Enlace a YouTube")
        distribuidor_dialogo.addWidget(etiqueta_enlace, numero_fila, 0)

        self.texto_enlace = QLineEdit(self)
        distribuidor_dialogo.addWidget(self.texto_enlace, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_calorias = QLabel("Calorias por repetición")
        distribuidor_dialogo.addWidget(etiqueta_calorias, numero_fila, 0)

        self.texto_calorias = QLineEdit(self)
        distribuidor_dialogo.addWidget(self.texto_calorias, numero_fila, 1)
        numero_fila = numero_fila + 1

        # Creación de los botones para guardar o cancelar
        caja_botones = QGroupBox()
        caja_botones.setLayout(QHBoxLayout())
        caja_botones.setStyleSheet('''
                QGroupBox{border:none}''')

        self.btn_guardar = QPushButton("Guardar")
        caja_botones.layout().addWidget(self.btn_guardar)
        self.btn_guardar.clicked.connect(self.guardar)

        self.btn_cancelar = QPushButton("Cancelar")
        caja_botones.layout().addWidget(self.btn_cancelar)
        self.btn_cancelar.clicked.connect(self.cancelar)

        distribuidor_dialogo.addWidget(caja_botones, numero_fila, 0, 1, 2)

        # Si el diálogo se va a usar para editar, se pone la información correspondiente en los campos de texto
        if (ejercicio != None):
            self.texto_nombre.setText(ejercicio["nombre"])
            self.texto_descripcion.setText(ejercicio["descripcion"])
            self.texto_enlace.setText(ejercicio["youtube"])
            self.texto_calorias.setText(str(ejercicio["calorias"]))

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

