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
    """Muestra un mensaje de error genérico."""
    messagebox.showerror("Error", str(e))


# 💠 NUEVO: función para mostrar matrices con formato bonito
def formatear_matriz(matriz):
    """Devuelve una representación visual centrada y limpia de una matriz."""
    if not isinstance(matriz, np.ndarray):
        return str(matriz)

    # Convertir a formato alineado con 3 decimales
    filas = ["  ".join(f"{v:8.3f}" for v in fila) for fila in matriz]
    return "[\n" + "\n".join(filas) + "\n]"