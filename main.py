import customtkinter as ctk
import numpy as np
from tkinter import messagebox
from operaciones import *
from utils import *


class CalculadoraMatrices:
    def __init__(self, main, tamaño, operacion):
        self.main = main
        self.main.title("Calculadora de Matrices")
        self.main.geometry("1000x700")
        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("blue")

        self.matrizA = []
        self.matrizB = []
        self.size_matriz = ctk.StringVar(value=tamaño)
        self.operacion_matriz = ctk.StringVar(value=operacion)

        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = ctk.CTkLabel(self.main, text="Calculadora de Matrices", font=("Arial", 24, "bold"))
        titulo.pack(pady=20)

        frame_opciones = ctk.CTkFrame(self.main, corner_radius=25)
        frame_opciones.pack(pady=20)

        ctk.CTkLabel(frame_opciones, text="Tamaño actual:", font=("Arial", 16)).grid(row=0, column=0, padx=5)
        ctk.CTkLabel(frame_opciones, textvariable=self.size_matriz, font=("Arial", 16, "bold")).grid(row=0, column=1, padx=5)

        ctk.CTkLabel(frame_opciones, text="Operación:", font=("Arial", 16)).grid(row=0, column=2, padx=5)
        operaciones = ["Suma", "Resta", "Multiplicación", "Determinante", "Inversa", "Cofactores", "Gauss-Jordan"]
        ctk.CTkOptionMenu(frame_opciones, variable=self.operacion_matriz, values=operaciones, command=self.generar_campos).grid(row=0, column=3, padx=5)

        ctk.CTkButton(frame_opciones, text="Calcular", command=self.calcular).grid(row=0, column=4, padx=10)

        self.frame_matrices = ctk.CTkFrame(self.main)
        self.frame_matrices.pack(pady=15)
        self.generar_campos(self.size_matriz.get())

        self.resultado_label = ctk.CTkTextbox(self.main, height=150, width=600, font=("Consolas", 18))
        self.resultado_label.pack(pady=15)

    def generar_campos(self, tamaño):
        for widget in self.frame_matrices.winfo_children():
            widget.destroy()

        filas, columnas = map(int, tamaño.split("x"))
        self.matrizA = []
        self.matrizB = []

        # Matriz A
        ctk.CTkLabel(self.frame_matrices, text="Matriz A", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=5)
        frameA = ctk.CTkFrame(self.frame_matrices)
        frameA.grid(row=1, column=0, padx=15)
        for i in range(filas):
            fila = []
            for j in range(columnas):
                entry = ctk.CTkEntry(frameA, width=60)
                entry.grid(row=i, column=j, padx=3, pady=3)
                fila.append(entry)
            self.matrizA.append(fila)

        # Matriz B (solo si aplica)
        if self.operacion_matriz.get() in ["Suma", "Resta", "Multiplicación"]:
            ctk.CTkLabel(self.frame_matrices, text="Matriz B", font=("Arial", 16, "bold")).grid(row=0, column=1, pady=5)
            frameB = ctk.CTkFrame(self.frame_matrices)
            frameB.grid(row=1, column=1, padx=15)
            for i in range(filas):
                fila = []
                for j in range(columnas):
                    entry = ctk.CTkEntry(frameB, width=60)
                    entry.grid(row=i, column=j, padx=3, pady=3)
                    fila.append(entry)
                self.matrizB.append(fila)

    def calcular(self):
        op = self.operacion_matriz.get()
        A = validar_numeros(self.matrizA)
        if A is None:
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
