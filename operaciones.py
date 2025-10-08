import numpy as np
from utils import validar_cuadrada


def sumar_matrices(A, B):
    if A.shape != B.shape:
        raise ValueError("Las matrices deben tener el mismo tamaño para sumarse.")
    return A + B


def restar_matrices(A, B):
    if A.shape != B.shape:
        raise ValueError("Las matrices deben tener el mismo tamaño para restarse.")
    return A - B


def multiplicar_matrices(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("El número de columnas de A debe coincidir con el número de filas de B.")
    return np.dot(A, B)


def determinante(A):
    validar_cuadrada(A)
    return np.linalg.det(A)


def inversa(A):
    validar_cuadrada(A)
    det = np.linalg.det(A)
    if det == 0:
        raise ValueError("La matriz es singular y no tiene inversa.")
    return np.linalg.inv(A)


def cofactores(A):
    validar_cuadrada(A)
    n = A.shape[0]
    C = np.zeros_like(A)
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(A, i, axis=0), j, axis=1)
            C[i, j] = ((-1)**(i+j)) * np.linalg.det(minor)
    return C


def gauss_jordan(A):
    A = np.array(A, dtype=float)
    filas, columnas = A.shape
    if columnas != filas + 1:
        raise ValueError("La matriz aumentada debe tener una columna adicional para Gauss-Jordan.")

    for i in range(filas):
        if A[i, i] == 0:
            for j in range(i+1, filas):
                if A[j, i] != 0:
                    A[[i, j]] = A[[j, i]]
                    break
            else:
                raise ValueError("No se puede realizar Gauss-Jordan, pivote nulo.")
        A[i] = A[i] / A[i, i]
        for j in range(filas):
            if i != j:
                A[j] = A[j] - A[j, i] * A[i]
    return A
