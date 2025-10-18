import numpy as np
from tkinter import messagebox


def validar_numeros(entries):
    """
    Convierte los valores ingresados a una matriz NumPy validando que sean números.
    Devuelve None si hay error y muestra un mensaje.
    """
    try:
        return np.array([[float(e.get()) for e in fila] for fila in entries])
    except ValueError:
        messagebox.showerror("Error", "Todos los campos deben contener números válidos.")
        return None


def validar_cuadrada(A, operacion=None):
    """
    Valida si la matriz es cuadrada. Si operacion es una de las que requiere cuadrada,
    muestra un mensaje de advertencia si no cumple.
    """
    filas = A.shape[0]
    columnas = A.shape[1]

    if operacion in ["Determinante", "Inversa", "Cofactores"]:
        if filas != columnas:
            messagebox.showwarning(
                "Error de operación",
                f"La operación '{operacion}' requiere una matriz cuadrada ({filas}x{columnas} no es cuadrada)."
            )
            return False
    return True


def mostrar_mensaje_error(e):
    """Muestra un mensaje de error en ventana."""
    messagebox.showerror("Error", str(e))
