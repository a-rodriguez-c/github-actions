from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from functools import partial


class VistaListaPersonas(QWidget):
    #Ventana que muestra la lista de personas

    def __init__(self, interfaz):
        """
        Constructor de la ventanas
        """
        super().__init__()
        
        self.interfaz = interfaz
       
        #Se establecen las características de la ventana
        self.title = 'En Forma'
        self.width = 875
        self.height = 758
        self.inicializar_GUI()

    def inicializar_GUI(self):
        
        #inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))
         
        self.distribuidor_base = QVBoxLayout(self)

        #Creación del logo de encabezado
        self.logo=QLabel(self)
        self.pixmap = QPixmap("src/recursos/EnFormaLogo.png")
        self.pixmap = self.pixmap.scaled(488,158, Qt.KeepAspectRatio)
        self.logo.setPixmap(self.pixmap)
        self.logo.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.logo,alignment=Qt.AlignCenter)

        #Creación de las etiquetsa con textos de bienvenida
        self.etiqueta_bienvenida=QLabel("!!Bienvenido!!")
        self.etiqueta_bienvenida.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.etiqueta_bienvenida,Qt.AlignCenter)

        #Creación del espacio de los botones
        self.widget_botones=QWidget()
        self.distribuidor_botones=QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)

        #Creación de los botones
        self.btn_crear_persona=QPushButton("Crear persona",self)
        self.btn_crear_persona.setFixedSize(288,48)
        self.btn_crear_persona.setToolTip("Crear persona")
        self.btn_crear_persona.setIcon(QIcon("src/recursos/006-add.png"))
        self.btn_crear_persona.setIconSize(QSize(120,120))
        self.distribuidor_botones.addWidget(self.btn_crear_persona,0,1,Qt.AlignLeft)
        self.btn_crear_persona.clicked.connect(self.mostrar_ventana_crear_persona)

        self.btn_ver_ejercicios=QPushButton("Ejercicios",self)
        self.btn_ver_ejercicios.setFixedSize(288,48)
        self.btn_ver_ejercicios.setToolTip("Ejercicios")
        self.btn_ver_ejercicios.setIcon(QIcon("src/recursos/010-ejercicio.png"))
        self.btn_ver_ejercicios.setIconSize(QSize(30,30))
        self.distribuidor_botones.addWidget(self.btn_ver_ejercicios,0,2,Qt.AlignRight)
        self.distribuidor_base.addWidget(self.widget_botones,Qt.AlignCenter)
        self.btn_ver_ejercicios.clicked.connect(self.mostrar_ejercicios)

        #Creación del área con la información de las personas
        self.tabla_personas = QScrollArea(self)
        self.tabla_personas.setWidgetResizable(True)
        self.tabla_personas.setFixedSize(840, 400)
        self.widget_tabla_personas = QWidget()
        self.distribuidor_tabla_personas = QGridLayout()
        self.widget_tabla_personas.setLayout(self.distribuidor_tabla_personas);
        self.tabla_personas.setWidget(self.widget_tabla_personas)
        self.distribuidor_base.addWidget(self.tabla_personas)

        #Hacemos la ventana visible
        self.show()


    def mostrar_personas(self, lista_personas):
        """
        Esta función puebla la tabla con las personas
        """
        self.personas = lista_personas
        numero_fila=0

        self.distribuidor_tabla_personas.setColumnStretch(0,1)
        self.distribuidor_tabla_personas.setColumnStretch(1,1)
        self.distribuidor_tabla_personas.setColumnStretch(2,0)
        self.distribuidor_tabla_personas.setColumnStretch(3,0)
        self.distribuidor_tabla_personas.setColumnStretch(4,0)
        self.distribuidor_tabla_personas.setColumnStretch(5,0)

        #Ciclo para llenar la tabla
        if (self.personas!= None and len(self.personas)>0) :
            self.tabla_personas.setVisible(True)

            #Creación de las etiquetas
            etiqueta_nombre=QLabel("Nombre")
            etiqueta_nombre.setMinimumSize(QSize(0,0))
            etiqueta_nombre.setMaximumSize(QSize(65525,65525))
            etiqueta_nombre.setAlignment(Qt.AlignCenter)
            etiqueta_nombre.setFont(QFont("Times",weight=QFont.Bold)) 
            self.distribuidor_tabla_personas.addWidget(etiqueta_nombre, 0,0, Qt.AlignLeft)

            etiqueta_acciones=QLabel("Opciones")                      
            etiqueta_acciones.setMinimumSize(QSize(0,0))
            etiqueta_acciones.setMaximumSize(QSize(65525,65525))
            etiqueta_acciones.setAlignment(Qt.AlignCenter)
            etiqueta_acciones.setFont(QFont("Times",weight=QFont.Bold))               
            self.distribuidor_tabla_personas.addWidget(etiqueta_acciones, 0,2,1,3, Qt.AlignCenter)
       
            for dic_personas in self.personas:
                numero_fila=numero_fila+1

                etiqueta_nombre=QLabel(dic_personas['nombre'] + ' ' + dic_personas['apellido'])
                etiqueta_nombre.setWordWrap(True)
                self.distribuidor_tabla_personas.addWidget(etiqueta_nombre,numero_fila,0)

                #Creación de los botones asociados a cada acción
                btn_entrenamientos = QPushButton("", self)
                btn_entrenamientos.setToolTip("Entrenamientos")
                btn_entrenamientos.setFixedSize(40, 40)
                btn_entrenamientos.setIcon(QIcon("src/recursos/reporte.png"))
                btn_entrenamientos.clicked.connect(partial(self.mostrar_entrenamientos, numero_fila ))
                self.distribuidor_tabla_personas.addWidget(btn_entrenamientos, numero_fila, 2, Qt.AlignCenter)

                btn_editar_persona=QPushButton("",self)
                btn_editar_persona.setToolTip("Editar")
                btn_editar_persona.setFixedSize(40,40)
                btn_editar_persona.setIcon(QIcon("src/recursos/004-edit-button.png"))
                btn_editar_persona.clicked.connect(partial(self.mostrar_persona,numero_fila) )
                self.distribuidor_tabla_personas.addWidget(btn_editar_persona,numero_fila,3,Qt.AlignCenter)

                btn_dejar_de_entrenar_persona = QPushButton("", self)
                btn_dejar_de_entrenar_persona.setToolTip("Dejar de entrenar")
                btn_dejar_de_entrenar_persona.setFixedSize(40, 40)
                btn_dejar_de_entrenar_persona.setIcon(QIcon("src/recursos/002-door-open-fill-icon.png"))
                btn_dejar_de_entrenar_persona.clicked.connect(
                    partial(self.mostrar_ventana_dejar_de_entrenar_persona, numero_fila))
                self.distribuidor_tabla_personas.addWidget(btn_dejar_de_entrenar_persona, numero_fila, 4,
                                                           Qt.AlignCenter)

                btn_eliminar=QPushButton("",self)
                btn_eliminar.setToolTip("Borrar")
                btn_eliminar.setFixedSize(40,40)
                btn_eliminar.setIcon(QIcon("src/recursos/005-delete.png"))
                btn_eliminar.clicked.connect(partial(self.eliminar_persona,numero_fila) )
                self.distribuidor_tabla_personas.addWidget(btn_eliminar,numero_fila,5,Qt.AlignCenter)
        else:
                self.tabla_personas.setVisible(False)

        #persona para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla_personas.layout().setRowStretch(numero_fila+2, 1)

    def mostrar_ventana_crear_persona(self):
        """
        Esta función informa a la interfaz para desplegar la ventana para crear personas
        """
        self.hide()
        self.interfaz.crear_persona()

    def mostrar_persona(self, id_persona):
        """
        Esta función informa a la interfaz para desplegar la ventana con la información de la persona seleccionada
        """
        self.hide()
        self.interfaz.mostrar_persona(id_persona)

    def mostrar_ventana_dejar_de_entrenar_persona(self, id_persona):
        """
        Esta función informa a la interfaz para desplegar la ventana para dejar de entrenar a una persona
        """
        self.hide()
        self.interfaz.mostrar_ventana_dejar_de_entrenar_persona(id_persona)

    def eliminar_persona(self, indice):
        """
        Esta función elimina una persona tras solicitar una confirmación
        """
        mensaje_confirmacion = QMessageBox()
        mensaje_confirmacion.setIcon(QMessageBox.Question)
        mensaje_confirmacion.setText(
            "¿Esta seguro de que desea borrar esta persona?\nRecuerde que esta acción es irreversible")
        mensaje_confirmacion.setWindowTitle("¿Desea borrar esta persona?")
        mensaje_confirmacion.setWindowIcon(QIcon("src/recursos/EnFormaLogo.png"))
        mensaje_confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        respuesta = mensaje_confirmacion.exec_()
        if respuesta == QMessageBox.Yes:
            self.interfaz.eliminar_persona(indice)
            self.hide()
            self.interfaz.mostrar_vista_lista_personas()

    def mostrar_ejercicios(self):
        """
        Esta función informa a la interfaz para desplegar la ventana de lista de ejercicios
        """
        self.hide()
        self.interfaz.mostrar_ejercicios()

    def mostrar_entrenamientos(self, id_persona):
        """
        Esta función informa a la interfaz para desplegar la ventana de lista de entrenamientos
        """
        self.hide()
        self.interfaz.mostrar_entrenamientos(id_persona)
