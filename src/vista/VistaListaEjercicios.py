from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

from functools import partial

from src.vista.VistaCrearEjercicio import VistaCrearEjercicio


class VistaListaEjercicios(QWidget):
    #Ventana que muestra la lista de ejercicios

    def __init__(self, interfaz):
        """
        Constructor de la ventana
        """
        super().__init__()

        #Se establecen las características de la ventana
        self.titulo = 'En Forma- Ejercicios'
        self.interfaz=interfaz

        self.width = 400
        self.height = 500
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

        self.btn_crear_ejercicio=QPushButton("Crear ejercicio", self)
        self.btn_crear_ejercicio.setFixedSize(170, 40)
        self.btn_crear_ejercicio.setToolTip("Crear ejercicio")
        self.btn_crear_ejercicio.setIcon(QIcon("src/recursos/006-add.png"))
        self.btn_crear_ejercicio.clicked.connect(self.mostrar_dialogo_crear_ejercicio)

        self.contenedor_tabla = QGroupBox(self)
        self.contenedor_tabla.setLayout(QHBoxLayout())
        self.contenedor_tabla.setTitle('Ejercicios')
        self.distribuidor_base.addWidget(self.contenedor_tabla)

        #Creación de la tabla con la lista de ejercicios
        self.tabla_ejercicios = QScrollArea(self)
        self.tabla_ejercicios.setWidgetResizable(True)
        self.tabla_ejercicios.setStyleSheet('QScrollArea{border:none}')
        self.tabla_ejercicios.setFixedSize(300, 300)
        self.widget_tabla_ejercicios = QWidget()
        self.distribuidor_tabla_ejercicios = QGridLayout(self.widget_tabla_ejercicios)
        self.tabla_ejercicios.setWidget(self.widget_tabla_ejercicios)
        self.contenedor_tabla.layout().addWidget(self.tabla_ejercicios)

        self.distribuidor_tabla_ejercicios.setColumnStretch(0, 0)
        self.distribuidor_tabla_ejercicios.setColumnStretch(1, 0)
        self.distribuidor_tabla_ejercicios.setColumnStretch(2, 0)

        self.distribuidor_tabla_ejercicios.setSpacing(0)

        #Creación de las etiquetas de encabezado
        etiqueta_nombre = QLabel("Nombre")
        etiqueta_nombre.setFixedSize(145,40)
        etiqueta_nombre.setFont(QFont("Times",weight=QFont.Bold)) 
        self.distribuidor_tabla_ejercicios.addWidget(etiqueta_nombre, 0, 0, Qt.AlignTop)

        etiqueta_accion = QLabel("Acción")
        etiqueta_accion.setFixedSize(60,40)
        etiqueta_accion.setFont(QFont("Times",weight=QFont.Bold)) 
        etiqueta_accion.setAlignment(Qt.AlignCenter)
        self.distribuidor_tabla_ejercicios.addWidget(etiqueta_accion, 0, 1, 0, 2, Qt.AlignTop | Qt.AlignCenter)

        #Se añaden los botones a la caja de botones
        caja_botones.layout().addWidget(self.btn_volver)
        caja_botones.layout().addWidget(self.btn_crear_ejercicio)
        caja_botones.layout().setContentsMargins(0, 0, 0, 0)
        caja_botones.setObjectName("MyBox")
        caja_botones.setStyleSheet("#MyBox{border:3px}")
        self.distribuidor_base.addWidget(caja_botones)

    def mostrar_ejercicios(self, lista_ejercicios):
        """
        Esta función muestra la lista de ejercicios
        """
        self.ejercicios = lista_ejercicios

        #Ciclo para poblar la tabla
        numero_fila = 0
        for ejercicio in self.ejercicios:

            etiqueta_nombre=QLabel(ejercicio["nombre"])
            etiqueta_nombre.setWordWrap(True)
            etiqueta_nombre.setFixedSize(90,40)
            self.distribuidor_tabla_ejercicios.addWidget(etiqueta_nombre, numero_fila + 1, 0, Qt.AlignTop)

            boton_editar=QPushButton("",self)
            boton_editar.setToolTip("Editar")
            boton_editar.setFixedSize(30,30)
            boton_editar.setIcon(QIcon("src/recursos/004-edit-button.png"))
            boton_editar.clicked.connect(partial(self.mostrar_dialogo_editar_ejercicio, numero_fila))
            self.distribuidor_tabla_ejercicios.addWidget(boton_editar, numero_fila + 1, 1, Qt.AlignTop)

            etiqueta_eliminar=QPushButton("",self)
            etiqueta_eliminar.setToolTip("Borrar")
            etiqueta_eliminar.setFixedSize(30,30)
            etiqueta_eliminar.setIcon(QIcon("src/recursos/005-delete.png"))
            etiqueta_eliminar.clicked.connect(partial(self.eliminar_ejercicio, numero_fila))
            self.distribuidor_tabla_ejercicios.addWidget(etiqueta_eliminar, numero_fila + 1, 2, Qt.AlignTop)

            numero_fila=numero_fila+1

        #persona para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla_ejercicios.layout().setRowStretch(numero_fila + 1, 1)

    def mostrar_dialogo_crear_ejercicio(self):
        """
        Esta función ejecuta el diálogo para crear un nuevo ejercicio
        """
        dialogo=VistaCrearEjercicio(None, self.interfaz)
        dialogo.exec_()
        if dialogo.resultado==1:
            self.interfaz.crear_ejercicio(dialogo.texto_nombre.text(), dialogo.texto_descripcion.toPlainText(), dialogo.texto_enlace.text(),
                                          dialogo.texto_calorias.text())

    def mostrar_dialogo_editar_ejercicio(self, id_ejercicio):
        """
        Esta función ejecuta el diálogo para editar un ejercicio
        """    
        dialogo=VistaCrearEjercicio(self.ejercicios[id_ejercicio], self.interfaz)
        dialogo.exec_()
        if dialogo.resultado==1:            
            self.interfaz.editar_ejercicio(id_ejercicio, dialogo.texto_nombre.text(), dialogo.texto_descripcion.toPlainText(),dialogo.texto_enlace.text(), dialogo.texto_calorias.text())
            self.hide()
            self.interfaz.mostrar_ejercicios()

    def eliminar_ejercicio(self, indice_ejercicio):
        """
        Esta función informa a la interfaz el ejercicio a eliminar
        """    
        mensaje_confirmacion=QMessageBox()
        mensaje_confirmacion.setIcon(QMessageBox.Question)
        mensaje_confirmacion.setText("¿Esta seguro de que desea eliminar este ejercicio?\nRecuerde que esta acción es irreversible")
        mensaje_confirmacion.setWindowTitle("¿Desea borrar este ejercicio?")
        mensaje_confirmacion.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))
        mensaje_confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No ) 
        respuesta=mensaje_confirmacion.exec_()
        if respuesta == QMessageBox.Yes:
            self.interfaz.eliminar_ejercicio(indice_ejercicio)
            self.hide()
            self.interfaz.mostrar_ejercicios()

    def volver(self):
        """
        Esta función permite volver a la ventana de lista de personas
        """
        self.hide()
        self.interfaz.mostrar_vista_lista_personas()

    def error(self, error):
            mensaje_error=QMessageBox()
            mensaje_error.setIcon(QMessageBox.Question)
            mensaje_error.setText("Error : " + error)
            mensaje_error.setWindowTitle("Error al guardar ejercicio")
            mensaje_error.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))
            mensaje_error.setStandardButtons(QMessageBox.Ok ) 
            respuesta=mensaje_error.exec_()

    def closeEvent(self, event):
        self.hide()
        self.interfaz.mostrar_vista_lista_personas()
        event.accept()
