from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

from functools import partial

from src.vista.VistaCrearEntrenamiento import VistaCrearEntrenamiento


class VistaListaEntrenamientos(QWidget):
    #Ventana que muestra la lista de entrenamientos

    def __init__(self, interfaz, persona, ejercicios):
        """
        Constructor de la ventana
        """
        super().__init__()

        #Se establecen las características de la ventana
        self.titulo = 'En Forma- Entrenamientos'
        self.interfaz = interfaz
        self.persona = persona
        self.ejercicios = ejercicios

        self.width =720
        self.height = 560
        self.inicializar_GUI()
        self.show()


    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))
         
        self.distribuidor_base = QVBoxLayout(self)        

        #Creación del grupo de botones
        caja_botones = QGroupBox()
        caja_botones.setLayout(QHBoxLayout())

        #Creación de los botones
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(170, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.btn_volver.clicked.connect(self.volver)

        self.btn_crear_entrenamiento=QPushButton("Registrar ejercicio", self)
        self.btn_crear_entrenamiento.setFixedSize(170, 40)
        self.btn_crear_entrenamiento.setToolTip("Registrar ejercicio")
        self.btn_crear_entrenamiento.setIcon(QIcon("src/recursos/006-add.png"))
        self.btn_crear_entrenamiento.clicked.connect(self.mostrar_dialogo_crear_entrenamiento)

        self.btn_crear_reporte = QPushButton("Reporte", self)
        self.btn_crear_reporte.setFixedSize(170, 40)
        self.btn_crear_reporte.setToolTip("Reporte de seguridad")
        self.btn_crear_reporte.setIcon(QIcon("src/recursos/reporte.png"))
        self.btn_crear_reporte.setIconSize(QSize(30, 30))
        self.btn_crear_reporte.clicked.connect(self.mostrar_ventana_reporte)

        self.contenedor_tabla = QGroupBox(self)
        self.contenedor_tabla.setLayout(QHBoxLayout())
        self.contenedor_tabla.setTitle('Entrenamientos')
        self.distribuidor_base.addWidget(self.contenedor_tabla)

        #Creación de la tabla con la lista de entrenamientos
        self.tabla_entrenamientos = QScrollArea(self)
        self.tabla_entrenamientos.setWidgetResizable(True)
        self.tabla_entrenamientos.setStyleSheet('QScrollArea{border:none}')
        self.tabla_entrenamientos.setFixedSize(620, 460)
        self.widget_tabla_entrenamientos = QWidget()
        self.distribuidor_tabla_entrenamientos = QGridLayout(self.widget_tabla_entrenamientos)
        self.tabla_entrenamientos.setWidget(self.widget_tabla_entrenamientos)
        self.contenedor_tabla.layout().addWidget(self.tabla_entrenamientos)

        self.distribuidor_tabla_entrenamientos.setColumnStretch(0, 0)
        self.distribuidor_tabla_entrenamientos.setColumnStretch(1, 0)
        self.distribuidor_tabla_entrenamientos.setColumnStretch(2, 0)

        self.distribuidor_tabla_entrenamientos.setSpacing(0)

        #Creación de las etiquetas de encabezado
        etiqueta_ejercicio = QLabel("Ejercicio")
        etiqueta_ejercicio.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla_entrenamientos.addWidget(etiqueta_ejercicio, 0, 0, Qt.AlignTop)

        etiqueta_fecha = QLabel("Fecha")
        etiqueta_fecha.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla_entrenamientos.addWidget(etiqueta_fecha, 0, 1, alignment=Qt.AlignLeft | Qt.AlignTop)

        etiqueta_repeticiones = QLabel("Repeticiones")
        etiqueta_repeticiones.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla_entrenamientos.addWidget(etiqueta_repeticiones, 0, 2, Qt.AlignLeft | Qt.AlignTop)

        etiqueta_tiempo = QLabel("Tiempo")
        etiqueta_tiempo.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla_entrenamientos.addWidget(etiqueta_tiempo, 0, 3, Qt.AlignLeft | Qt.AlignTop)

        etiqueta_accion = QLabel("Acciones")
        etiqueta_accion.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla_entrenamientos.addWidget(etiqueta_accion, 0, 4, 0, 2, alignment=Qt.AlignCenter | Qt.AlignTop)

        #Se añaden los botones a la caja de botones
        caja_botones.layout().addWidget(self.btn_volver)
        caja_botones.layout().addWidget(self.btn_crear_entrenamiento)
        caja_botones.layout().addWidget(self.btn_crear_reporte)
        caja_botones.layout().setContentsMargins(0, 0, 0, 0)
        caja_botones.setObjectName("MyBox")
        caja_botones.setStyleSheet("#MyBox{border:3px}")
        self.distribuidor_base.addWidget(caja_botones)

    def mostrar_entrenamientos(self, id_persona, lista_entrenamientos):
        """
        Esta función muestra la lista de entrenamientos
        """
        self.persona_actual = id_persona
        nombre_completo = self.persona['nombre'] + " " + self.persona['apellido']
        self.contenedor_tabla.setTitle('Entrenamientos  de {}'.format(nombre_completo))
        self.entrenamientos = lista_entrenamientos
        
        if len(lista_entrenamientos) == 0:
            self.btn_crear_reporte.setDisabled(True)

        #Ciclo para poblar la tabla
        numero_fila = 0
        for entrenamiento in self.entrenamientos:

            etiqueta_nombre=QLabel(entrenamiento['ejercicio'])
            etiqueta_nombre.setWordWrap(True)
            etiqueta_nombre.setFixedSize(90,40)
            self.distribuidor_tabla_entrenamientos.addWidget(etiqueta_nombre, numero_fila + 1, 0, Qt.AlignTop)

            etiqueta_fecha = QLabel(entrenamiento['fecha'])
            etiqueta_fecha.setWordWrap(True)
            etiqueta_fecha.setFixedSize(90, 40)
            self.distribuidor_tabla_entrenamientos.addWidget(etiqueta_fecha, numero_fila + 1, 1, Qt.AlignTop)

            etiqueta_repeticiones = QLabel(str(entrenamiento['repeticiones']))
            etiqueta_repeticiones.setWordWrap(True)
            etiqueta_repeticiones.setFixedSize(90, 40)
            self.distribuidor_tabla_entrenamientos.addWidget(etiqueta_repeticiones, numero_fila + 1, 2, Qt.AlignTop)

            etiqueta_tiempo = QLabel(str(entrenamiento['tiempo']))
            etiqueta_tiempo.setWordWrap(True)
            etiqueta_tiempo.setFixedSize(90, 40)
            self.distribuidor_tabla_entrenamientos.addWidget(etiqueta_tiempo, numero_fila + 1, 3, Qt.AlignTop)

            boton_editar=QPushButton("",self)
            boton_editar.setToolTip("Editar")
            boton_editar.setFixedSize(30,30)
            boton_editar.setIcon(QIcon("src/recursos/004-edit-button.png"))
            boton_editar.clicked.connect(partial(self.mostrar_dialogo_editar_entrenamiento, numero_fila))
            self.distribuidor_tabla_entrenamientos.addWidget(boton_editar, numero_fila + 1, 4, Qt.AlignTop)

            boton_eliminar=QPushButton("",self)
            boton_eliminar.setToolTip("Borrar")
            boton_eliminar.setFixedSize(30,30)
            boton_eliminar.setIcon(QIcon("src/recursos/005-delete.png"))
            boton_eliminar.clicked.connect(partial(self.eliminar_entrenamiento, numero_fila))
            self.distribuidor_tabla_entrenamientos.addWidget(boton_eliminar, numero_fila + 1, 5, Qt.AlignTop)

            numero_fila=numero_fila+1

        if self.persona["fecha_retiro"] != "":
            self.btn_crear_entrenamiento.setDisabled(True)

        #Elemento para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla_entrenamientos.layout().setRowStretch(numero_fila + 1, 1)

    def mostrar_dialogo_crear_entrenamiento(self):
        """
        Esta función ejecuta el diálogo para crear un nuevo entrenamiento
        """
        dialogo=VistaCrearEntrenamiento(None, self.interfaz, self.ejercicios)
        dialogo.exec_()
        if dialogo.resultado==1:
            self.interfaz.crear_entrenamiento(self.persona_actual, dialogo.combobox_ejercicios.currentText(), dialogo.fecha.text(), dialogo.texto_repeticiones.text(),
                                          dialogo.texto_tiempo.text())

    def mostrar_dialogo_editar_entrenamiento(self, id_entrenamiento):
        """
        Esta función ejecuta el diálogo para editar un entrenamiento
        """    
        dialogo=VistaCrearEntrenamiento(self.entrenamientos[id_entrenamiento], self.interfaz, self.ejercicios)
        dialogo.exec_()
        if dialogo.resultado==1:            
            self.interfaz.editar_entrenamiento(id_entrenamiento, self.persona_actual, dialogo.combobox_ejercicios.currentText(), dialogo.fecha.text(), dialogo.texto_repeticiones.text(),
                                          dialogo.texto_tiempo.text())
            self.hide()
            self.interfaz.mostrar_entrenamientos(self.persona_actual)

    def eliminar_entrenamiento(self, id_entrenamiento):
        """
        Esta función informa a la interfaz el entrenamiento a eliminar
        """    
        mensaje_confirmacion=QMessageBox()
        mensaje_confirmacion.setIcon(QMessageBox.Question)
        mensaje_confirmacion.setText("¿Esta seguro de que desea eliminar este entrenamiento?\nRecuerde que esta acción es irreversible")
        mensaje_confirmacion.setWindowTitle("¿Desea borrar este entrenamiento?")
        mensaje_confirmacion.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))
        mensaje_confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No ) 
        respuesta=mensaje_confirmacion.exec_()
        if respuesta == QMessageBox.Yes:
            self.interfaz.eliminar_entrenamiento(id_entrenamiento, self.persona_actual)
            self.hide()
            self.interfaz.mostrar_entrenamientos(self.persona_actual)

    def mostrar_ventana_reporte(self):
        """
        Esta función informa a la interfaz para desplegar la ventana del reporte de entrenamientos
        """
        self.hide()
        self.interfaz.mostrar_reporte(self.persona_actual)

    def volver(self):
        """
        Esta función permite volver a la ventana de lista de personas
        """
        self.hide()
        self.interfaz.mostrar_vista_lista_personas()

    def error_clave(self, error):
            mensaje_error=QMessageBox()
            mensaje_error.setIcon(QMessageBox.Question)
            mensaje_error.setText("Error : " + error)
            mensaje_error.setWindowTitle("Error guardar clave")
            mensaje_error.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))
            mensaje_error.setStandardButtons(QMessageBox.Ok ) 
            respuesta=mensaje_error.exec_()

    def closeEvent(self, event):
        self.hide()
        self.interfaz.mostrar_vista_lista_personas()
        event.accept()
