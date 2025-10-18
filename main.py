import customtkinter as ctk
import numpy as np
from tkinter import messagebox
from operaciones import *
from utils import *


class CalculadoraMatrices:
    def __init__(self, main, tamaño, operacion):
        
        
        
        # ---------------------------------------------------------------------------------------------------
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        #                                   SELF ES IGUAL A THIS DE JAVA
        # ---------------------------------------------------------------------------------------------------
        
        
        
        
        # Configuración de la ventana
        self.main = main
        self.main.title("Calculadora de Matrices")
        self.main.geometry("1000x700")

        # Estilo de la interfaz
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.main.configure(fg_color="#111315")

        # Variables de control
        self.matrizA = []
        self.matrizB = []
        self.size_matriz = ctk.StringVar(value=tamaño)
        self.operacion_matriz = ctk.StringVar(value=operacion)

        self.crear_interfaz()

    def crear_interfaz(self):
        # Titulo
        titulo = ctk.CTkLabel(
            self.main,
            text="Calculadora de Matrices",
            font=("Segoe UI", 26, "bold"),
            text_color="#EAEAEA"
        )
        titulo.pack(pady=(30, 15))

        # Frame de opciones
        frame_opciones = ctk.CTkFrame(self.main, corner_radius=25, fg_color="#1C1F26")
        frame_opciones.pack(pady=20, padx=20)

        contenedor = ctk.CTkFrame(frame_opciones, fg_color="transparent")
        contenedor.pack(padx=20, pady=10)

        # Tamaño
        ctk.CTkLabel(contenedor, text="Tamaño:", font=("Segoe UI", 16), text_color="#EAEAEA").grid(row=0, column=0, padx=10, pady=10)
        opciones_tamaño = ["2x2", "3x3", "2x3", "3x2", "4x4", "4x2", "2x4", "Rectangular"]
        menu_tamaño = ctk.CTkOptionMenu(
            contenedor,
            variable=self.size_matriz,
            values=opciones_tamaño,
            corner_radius=20,
            fg_color="#2A2D34",
            text_color="#EAEAEA",
            dropdown_fg_color="#2A2D34",
            dropdown_text_color="#EAEAEA",
            button_color="#0078D7",
            button_hover_color="#005a9e",
            command=lambda _: self.generar_campos()
        )
        menu_tamaño.grid(row=0, column=1, padx=10, pady=10)

        # Operación
        ctk.CTkLabel(contenedor, text="Operación:", font=("Segoe UI", 16), text_color="#EAEAEA").grid(row=0, column=2, padx=10, pady=10)
        operaciones = ["Suma", "Resta", "Multiplicación", "Determinante", "Inversa", "Cofactores", "Gauss-Jordan"]
        menu_operacion = ctk.CTkOptionMenu(
            contenedor,
            variable=self.operacion_matriz,
            values=operaciones,
            corner_radius=20,
            fg_color="#2A2D34",
            text_color="#EAEAEA",
            dropdown_fg_color="#2A2D34",
            dropdown_text_color="#EAEAEA",
            button_color="#0078D7",
            button_hover_color="#005a9e",
            command=lambda _: self.actualizar_operacion()
        )
        menu_operacion.grid(row=0, column=3, padx=10, pady=10)

        # Botones
        boton_calcular = ctk.CTkButton(
            contenedor, text="Calcular", corner_radius=20,
            fg_color="#0078D7", hover_color="#005a9e",
            font=("Segoe UI", 15, "bold"),
            command=self.calcular
        )
        boton_calcular.grid(row=0, column=4, padx=15, pady=10)

        boton_limpiar = ctk.CTkButton(
            contenedor, text="🗑️ Limpiar", corner_radius=20,
            fg_color="#2A2D34", text_color="#EAEAEA",
            hover_color="#383C44",
            font=("Segoe UI", 15),
            command=self.limpiar_campos
        )
        boton_limpiar.grid(row=0, column=5, padx=10, pady=10)

        # Área de matrices
        self.frame_matrices = ctk.CTkFrame(self.main, corner_radius=25, fg_color="#1C1F26")
        self.frame_matrices.pack(pady=25, padx=20)
        self.generar_campos()

        # Área de resultados
        frame_resultado = ctk.CTkFrame(self.main, corner_radius=25, fg_color="#1C1F26")
        frame_resultado.pack(pady=25, padx=20, fill="x")

        ctk.CTkLabel(frame_resultado, text="Resultado:", font=("Segoe UI", 18, "bold"), text_color="#EAEAEA").pack(pady=10)
        self.resultado_label = ctk.CTkTextbox(
            frame_resultado, height=150, width=700, font=("Consolas", 18),
            fg_color="#0E1012", text_color="#EAEAEA", border_width=0, corner_radius=15
        )
        self.resultado_label.pack(pady=(0, 15))

    def generar_campos(self):
        for widget in self.frame_matrices.winfo_children():
            widget.destroy()

        # Obtener tamaño de la matriz y crear campos de entrada conforme el usuario elija
        tamaño = self.size_matriz.get()
        if tamaño.lower() == "rectangular":
            filas, columnas = 3, 4  # Predeterminado? No se si funciona porque esta el menu inicio pero aca esta por si acaso
        else:
            filas, columnas = map(int, tamaño.split("x"))

        self.matrizA = []
        self.matrizB = []

        # Matriz A, esto me ayudó chatpgt la verdad porque no le entendi al 100
        ctk.CTkLabel(self.frame_matrices, text="Matriz A", font=("Segoe UI", 16, "bold"), text_color="#EAEAEA").grid(row=0, column=0, pady=10)
        frameA = ctk.CTkFrame(self.frame_matrices, corner_radius=20, fg_color="#2A2D34")
        frameA.grid(row=1, column=0, padx=20, pady=10)
        for i in range(filas):
            fila = []
            for j in range(columnas):
                entry = ctk.CTkEntry(frameA, width=60, corner_radius=10, fg_color="#0E1012", text_color="#EAEAEA", justify="center")
                entry.grid(row=i, column=j, padx=4, pady=4)
                fila.append(entry)
            self.matrizA.append(fila)

        # Matriz B tambien este 
        if self.operacion_matriz.get() in ["Suma", "Resta", "Multiplicación"]:
            ctk.CTkLabel(self.frame_matrices, text="Matriz B", font=("Segoe UI", 16, "bold"), text_color="#EAEAEA").grid(row=0, column=1, pady=10)
            frameB = ctk.CTkFrame(self.frame_matrices, corner_radius=20, fg_color="#2A2D34")
            frameB.grid(row=1, column=1, padx=20, pady=10)
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    entry = ctk.CTkEntry(frameB, width=60, corner_radius=10, fg_color="#0E1012", text_color="#EAEAEA", justify="center")
                    entry.grid(row=i, column=j, padx=4, pady=4)
                    fila.append(entry)
                self.matrizB.append(fila)

    def actualizar_operacion(self):
        self.generar_campos()

    def limpiar_campos(self):
        for lista in (self.matrizA + self.matrizB):
            for entry in lista:
                entry.delete(0, "end")
        self.resultado_label.delete("1.0", "end")

    def calcular(self):
        op = self.operacion_matriz.get()
        A = validar_numeros(self.matrizA)
        if A is None:
            return

        # Validación para operaciones que requieren matriz cuadrada
        if not validar_cuadrada(A, op):
            return

        if op in ["Suma", "Resta", "Multiplicación"]:
            B = validar_numeros(self.matrizB)
            if B is None:
                return
        else:
            B = None

        try:
            if op == "Suma":
                resultado = sumar_matrices(A, B)
            elif op == "Resta":
                resultado = restar_matrices(A, B)
            elif op == "Multiplicación":
                resultado = multiplicar_matrices(A, B)
            elif op == "Determinante":
                resultado = determinante(A)
            elif op == "Inversa":
                resultado = inversa(A)
            elif op == "Cofactores":
                resultado = cofactores(A)
            elif op == "Gauss-Jordan":
                resultado = gauss_jordan(A)
            else:
                resultado = "Operación no reconocida."

            self.mostrar_resultado(resultado)

        except Exception as e:
            mostrar_mensaje_error(e)

    def mostrar_resultado(self, resultado):
        self.resultado_label.delete("1.0", "end")
        if isinstance(resultado, np.ndarray):
            texto = np.array2string(resultado, precision=3, separator=", ")
        else:
            texto = str(round(resultado, 3)) if isinstance(resultado, float) else str(resultado)
        self.resultado_label.insert("1.0", texto)