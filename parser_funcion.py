"""
Nombre: Ortega Plaza Diego 
Matricula: 2403230009
Asignatura: Ciencia de Datos
Fecha: 21/09/26

Responsabilidad: extraer los parametros m (pendiente) y b (ordenada
al origen) a partir de una cadena de texto que representa una funcion
lineal con el formato y = mx + b (ejemplo: "2x + 3", "-1.5x - 4", "x + 5").
"""

import re


def normalizar_cadena(cadena_funcion):
    """Limpia y normaliza la cadena de entrada.

    Args:
        cadena_funcion (str): Cadena original ingresada por el usuario.

    Returns:
        str: Cadena normalizada, sin espacios y con signos explicitos.
    """
    cadena_normalizada = cadena_funcion.replace(" ", "").lower()

    if cadena_normalizada and cadena_normalizada[0] not in ("+", "-"):
        cadena_normalizada = "+" + cadena_normalizada

    return cadena_normalizada


def extraer_parametros(cadena_funcion):
    """Extrae la pendiente (m) y la ordenada al origen (b) de la cadena.

    Args:
        cadena_funcion (str): Cadena de texto con la funcion lineal.

    Returns:
        tuple(float, float): Una tupla (m, b) con los parametros
        detectados. Si algun termino no aparece en la cadena, su
        valor por defecto es 0.0.

    Raises:
        ValueError: Si la cadena esta vacia o no contiene ningun
        termino numerico valido.
    """
    cadena_normalizada = normalizar_cadena(cadena_funcion)

    if not cadena_normalizada:
        raise ValueError("La cadena de la funcion no puede estar vacia.")

    terminos = re.findall(r"[+-][^+-]+", cadena_normalizada)

    if not terminos:
        raise ValueError(
            "No se pudo interpretar la funcion. Formato esperado: 'mx + b'."
        )

    pendiente = 0.0
    ordenada_origen = 0.0
    contiene_termino_x = False

    for termino in terminos:
        try:
            if "x" in termino:
                contiene_termino_x = True
                coeficiente_texto = termino.replace("x", "")

                if coeficiente_texto in ("+", ""):
                    coeficiente_texto = "+1"
                elif coeficiente_texto == "-":
                    coeficiente_texto = "-1"

                pendiente = float(coeficiente_texto)
            else:
                ordenada_origen = float(termino)
        except ValueError as error:
            raise ValueError(
                f"El termino '{termino}' no es un numero valido."
            ) from error

    if not contiene_termino_x and ordenada_origen == 0.0:
        raise ValueError(
            "No se detecto un termino en 'x' ni un termino independiente valido."
        )

    return pendiente, ordenada_origen