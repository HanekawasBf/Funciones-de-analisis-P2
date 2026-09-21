"""
Nombre: Ortega Plaza Diego 
Matricula: 2403230009
Asignatura: Ciencia de Datos
Fecha: 21/09/26

Responsabilidad: interaccion con el usuario mediante un menu principal
en consola. Captura de la funcion lineal, la cantidad de
muestras y los valores de x, delegando el trabajo de parsing y
evaluacion a los modulos parser_funcion y evaluador.
"""

from parser_funcion import extraer_parametros
from evaluador import evaluar_lista_valores


def mostrar_menu():
    """Menu principal."""
    print("\n----- MENU PRINCIPAL -----")
    print("1. Capturar funcion lineal")
    print("2. Capturar numero de muestras (n)")
    print("3. Capturar valores de x y evaluar")
    print("4. Salir")


def capturar_funcion_lineal(estado):
    """Solicita al usuario la funcion lineal y actualiza el estado.

    Args:
        estado (dict): Diccionario con el estado del programa
            (contiene las claves 'pendiente' y 'ordenada_origen').
    """
    cadena_funcion = input("Ingrese la funcion (ej. '2x + 3'): ").strip()

    try:
        pendiente, ordenada_origen = extraer_parametros(cadena_funcion)
        estado["pendiente"] = pendiente
        estado["ordenada_origen"] = ordenada_origen
        print(f"Funcion detectada: y = {pendiente}x + {ordenada_origen}")
    except ValueError as error:
        print(f"Error al interpretar la funcion: {error}")


def capturar_numero_muestras(estado):
    """Solicita al usuario la cantidad n de muestras (n > 0).

    Args:
        estado (dict): Diccionario con el estado del programa
            (contiene la clave 'numero_muestras').
    """
    entrada = input("Ingrese la cantidad de muestras (n > 0): ").strip()

    try:
        numero_muestras = int(entrada)
        if numero_muestras <= 0:
            print("Error: el numero de muestras debe ser mayor a 0.")
            return
        estado["numero_muestras"] = numero_muestras
        print(f"Numero de muestras registrado: {numero_muestras}")
    except ValueError:
        print("Error: debe ingresar un numero entero valido.")


def capturar_valores_y_evaluar(estado):
    """Solicita los n valores de x, evalua la funcion y muestra la tabla.

    Args:
        estado (dict): Diccionario con el estado del programa. Debe
            contener 'pendiente', 'ordenada_origen' y
            'numero_muestras' ya capturados.
    """
    if estado["pendiente"] is None or estado["ordenada_origen"] is None:
        print("Error: primero debe capturar la funcion lineal (opcion 1).")
        return

    if estado["numero_muestras"] is None:
        print("Error: primero debe capturar el numero de muestras (opcion 2).")
        return

    valores_x = []
    total_muestras = estado["numero_muestras"]

    for indice in range(1, total_muestras + 1):
        while True:
            entrada = input(f"Ingrese el valor de x_{indice}: ").strip()
            try:
                valores_x.append(float(entrada))
                break
            except ValueError:
                print("Error: debe ingresar un numero valido.")

    resultados = evaluar_lista_valores(
        estado["pendiente"], estado["ordenada_origen"], valores_x
    )

    mostrar_resultados(estado["pendiente"], estado["ordenada_origen"], resultados)


def mostrar_resultados(pendiente, ordenada_origen, resultados):
    """Imprime en consola los parametros y la tabla de resultados.

    Args:
        pendiente (float): Valor de m.
        ordenada_origen (float): Valor de b.
        resultados (list[tuple(float, float)]): Lista de pares (x, y).
    """
    print(f"\nParametros detectados: m = {pendiente}, b = {ordenada_origen}")
    print("\n   x        y")
    print("---------------------")

    for valor_x, valor_y in resultados:
        print(f"{valor_x:8.2f} {valor_y:8.2f}")


def inicializar_estado():
    """Crea y devuelve el diccionario de estado inicial del programa.

    Returns:
        dict: Estado inicial con valores por defecto en None.
    """
    return {
        "pendiente": None,
        "ordenada_origen": None,
        "numero_muestras": None,
    }


def ejecutar_programa():
    """Funcion principal: ejecuta el bucle del menu interactivo."""
    estado = inicializar_estado()
    continuar_ejecucion = True

    while continuar_ejecucion:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            capturar_funcion_lineal(estado)
        elif opcion == "2":
            capturar_numero_muestras(estado)
        elif opcion == "3":
            capturar_valores_y_evaluar(estado)
        elif opcion == "4":
            print("Finalizando el programa...")
            continuar_ejecucion = False
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_programa()