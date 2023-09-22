from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget


class VistaReporte(QWidget):
    #Ventana que muestra el reporte de entrenamientos de una persona

    def __init__(self, interfaz, persona):
        """
        Constructor de la ventana
        """
        super().__init__()

        # Se establecen las características de la ventana
        self.titulo = 'En Forma- Reporte de entrenamientos de '
        self.left = 80
        self.top = 80
        self.width = 720
        self.height = 560

        self.setAttribute(Qt.WA_DeleteOnClose)

        self.interfaz = interfaz
        self.persona = persona

        self.inicializar_GUI()
        self.show()

    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo + self.persona['nombre'] + ' ' + self.persona['apellido'])
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))

        self.distribuidor_base = QVBoxLayout(self)

        # Creación de la tabla datos de cantidad de elementos
        self.tabla_reporte = QScrollArea(self)
        self.tabla_reporte.setWidgetResizable(True)
        self.widget_tabla_reporte = QWidget()
        self.distribuidor_tabla_reporte = QGridLayout(self.widget_tabla_reporte)
        self.tabla_reporte.setWidget(self.widget_tabla_reporte)

        self.distribuidor_tabla_reporte.setColumnStretch(0, 0)
        self.distribuidor_tabla_reporte.setColumnStretch(1, 0)

        self.contenedor_tabla_reporte = QGroupBox(self)
        self.contenedor_tabla_reporte.setLayout(QHBoxLayout())
        self.contenedor_tabla_reporte.setTitle('Información básica')
        self.distribuidor_base.addWidget(self.contenedor_tabla_reporte)

        self.contenedor_tabla_reporte.layout().addWidget(self.tabla_reporte)
        self.tabla_reporte.setStyleSheet('QScrollArea{border:none}')

        # Creación de las etiquetas con los encabezados
        etiqueta_talla = QLabel("Talla")
        etiqueta_talla.setFont(QFont("Times",weight=QFont.Bold))
        self.distribuidor_tabla_reporte.addWidget(etiqueta_talla, 0, 0, Qt.AlignTop)

        etiqueta_peso = QLabel("Peso")
        etiqueta_peso.setFont(QFont("Times",weight=QFont.Bold))
        self.distribuidor_tabla_reporte.addWidget(etiqueta_peso, 0, 1, Qt.AlignTop)

        etiqueta_imc = QLabel("IMC")
        etiqueta_imc.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla_reporte.addWidget(etiqueta_imc, 0, 2, Qt.AlignTop)

        etiqueta_clasificacion = QLabel("Clasificación según IMC")
        etiqueta_clasificacion.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla_reporte.addWidget(etiqueta_clasificacion, 0, 4, Qt.AlignTop)

        # Creación de la tabla con el detalle de los entrenamientos

        self.tabla_entrenamientos = QScrollArea(self)
        self.tabla_entrenamientos.setWidgetResizable(True)
        self.widget_tabla_entrenamientos = QWidget()
        self.distribuidor_tabla = QGridLayout(self.widget_tabla_entrenamientos)
        self.tabla_entrenamientos.setWidget(self.widget_tabla_entrenamientos)

        self.distribuidor_tabla.setColumnStretch(0, 0)
        self.distribuidor_tabla.setColumnStretch(1, 0)

        self.contenedor_tabla_entrenamientos = QGroupBox(self)
        self.contenedor_tabla_entrenamientos.setLayout(QHBoxLayout())
        self.contenedor_tabla_entrenamientos.setTitle('Detalle de entrenamientos')
        self.distribuidor_base.addWidget(self.contenedor_tabla_entrenamientos)

        self.contenedor_tabla_entrenamientos.layout().addWidget(self.tabla_entrenamientos)
        self.tabla_entrenamientos.setStyleSheet('QScrollArea{border:none}')

        # Creación de las etiquetas con los encabezados
        etiqueta_valor = QLabel("Fecha")
        etiqueta_valor.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla.addWidget(etiqueta_valor, 0, 0, Qt.AlignTop)

        etiqueta_valor = QLabel("Ejercicios realizados")
        etiqueta_valor.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla.addWidget(etiqueta_valor, 0, 1, Qt.AlignTop)

        etiqueta_valor = QLabel("Calorias consumidas (aprox)")
        etiqueta_valor.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla.addWidget(etiqueta_valor, 0, 2, Qt.AlignTop)

        #Creación de los botones de funciones de la ventana
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(200, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.btn_volver.setIconSize(QSize(120, 120))
        self.btn_volver.clicked.connect(self.volver)
        self.distribuidor_base.addWidget(self.btn_volver)
        self.distribuidor_base.setAlignment(self.btn_volver, Qt.AlignCenter)

    def mostrar_datos(self, id_persona, datos_reporte):
        """
        Esta función pobla el reporte con la información
        """
        self.persona_actual = id_persona

        #Mostrar información básica
        etiqueta_detalle = QLabel(str(datos_reporte['persona']['talla']))
        etiqueta_detalle.setWordWrap(True)
        self.distribuidor_tabla_reporte.addWidget(etiqueta_detalle, 1, 0, Qt.AlignTop)

        etiqueta_detalle = QLabel(str(datos_reporte['persona']['peso']))
        etiqueta_detalle.setWordWrap(True)
        self.distribuidor_tabla_reporte.addWidget(etiqueta_detalle, 1, 1, Qt.AlignTop)

        etiqueta_detalle = QLabel(str(datos_reporte['estadisticas']['imc']))
        etiqueta_detalle.setWordWrap(True)
        self.distribuidor_tabla_reporte.addWidget(etiqueta_detalle, 1, 2, Qt.AlignTop)

        etiqueta_detalle = QLabel(str(datos_reporte['estadisticas']['clasificacion']))
        etiqueta_detalle.setWordWrap(True)
        self.distribuidor_tabla_reporte.addWidget(etiqueta_detalle, 1, 4, Qt.AlignTop)

        # Elemento para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla_reporte.layout().setRowStretch(2, 1)

        #Mostrar detalle de entrenamientos
        numero_fila = 2
        for entrenamiento in datos_reporte['estadisticas']['entrenamientos']:
            etiqueta_fecha = QLabel(entrenamiento['fecha'])
            etiqueta_fecha.setWordWrap(True)
            etiqueta_fecha.setFixedSize(90, 40)
            self.distribuidor_tabla.addWidget(etiqueta_fecha, numero_fila + 1, 0, Qt.AlignTop)

            etiqueta_repeticiones = QLabel(str(entrenamiento['repeticiones']))
            etiqueta_repeticiones.setWordWrap(True)
            etiqueta_repeticiones.setFixedSize(90, 40)
            self.distribuidor_tabla.addWidget(etiqueta_repeticiones, numero_fila + 1, 1, Qt.AlignTop)

            etiqueta_calorias = QLabel(str(entrenamiento['calorias']))
            etiqueta_calorias.setWordWrap(True)
            etiqueta_calorias.setFixedSize(90, 40)
            self.distribuidor_tabla.addWidget(etiqueta_calorias, numero_fila + 1, 2, Qt.AlignTop)
            numero_fila = numero_fila + 1

        etiqueta_total= QLabel("Total")
        etiqueta_total.setWordWrap(True)
        etiqueta_total.setFixedSize(90, 40)
        etiqueta_total.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla.addWidget(etiqueta_total, numero_fila + 1, 0, Qt.AlignTop)

        etiqueta_total_repeticiones = QLabel(str(datos_reporte['estadisticas']['total_repeticiones']))
        etiqueta_total_repeticiones.setWordWrap(True)
        etiqueta_total_repeticiones.setFixedSize(90, 40)
        etiqueta_total_repeticiones.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla.addWidget(etiqueta_total_repeticiones, numero_fila + 1, 1, Qt.AlignTop)

        etiqueta_total_calorias = QLabel(str(datos_reporte['estadisticas']['total_calorias']))
        etiqueta_total_calorias.setWordWrap(True)
        etiqueta_total_calorias.setFixedSize(90, 40)
        etiqueta_total_calorias.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla.addWidget(etiqueta_total_calorias, numero_fila + 1, 2, Qt.AlignTop)

        # Elemento para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla.layout().setRowStretch(numero_fila + 1, 1)
        
    def volver(self):
        """
        Esta función permite volver a la ventana de lista de entrenamientos de la persona
        """   
        self.hide()
        self.interfaz.mostrar_entrenamientos(self.persona_actual)

    def closeEvent(self, event):
        self.hide()
        self.interfaz.mostrar_vista_lista_personas()
        event.accept()
