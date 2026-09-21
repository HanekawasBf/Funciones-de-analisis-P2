"""
Nombre: Ortega Plaza Diego 
Matricula: 2403230009
Asignatura: Ciencia de Datos
Fecha: 21/09/26

Responsabilidad: evaluar la funcion lineal f(x) = mx + b para uno
o varios valores de x.
"""


def evaluar_funcion(pendiente, ordenada_origen, valor_x):
    """Calcula y = m * x + b para un unico valor de x.

    Args:
        pendiente (float): Valor de m.
        ordenada_origen (float): Valor de b.
        valor_x (float): Valor de x a evaluar.

    Returns:
        float: Resultado de evaluar la funcion lineal en valor_x.
    """
    return (pendiente * valor_x) + ordenada_origen


def evaluar_lista_valores(pendiente, ordenada_origen, valores_x):
    """Evalua la funcion lineal para una lista de valores de x.

    Args:
        pendiente (float): Valor de m.
        ordenada_origen (float): Valor de b.
        valores_x (list[float]): Lista de valores de x a evaluar.

    Returns:
        list[tuple(float, float)]: Lista de pares (x, y) con los
        resultados de la evaluacion, en el mismo orden que valores_x.
    """
    resultados = []

    for valor_x in valores_x:
        valor_y = evaluar_funcion(pendiente, ordenada_origen, valor_x)
        resultados.append((valor_x, valor_y))

    return resultados