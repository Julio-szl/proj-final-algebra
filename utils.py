import numpy as np
from tkinter import messagebox


def validar_cuadrada(A):
    """Valida si la matriz es cuadrada."""
    if A.shape[0] != A.shape[1]:
        raise ValueError("La matriz debe ser cuadrada para esta operación.")
    return True


def validar_numeros(entries):
    """Convierte los valores ingresados a una matriz NumPy validando que sean números."""
    try:
        return np.array([[float(e.get()) for e in fila] for fila in entries])
    except ValueError:
        messagebox.showerror("Error", "Todos los campos deben contener números válidos.")
        return None


def mostrar_mensaje_error(e):
    messagebox.showerror("Error", str(e))
