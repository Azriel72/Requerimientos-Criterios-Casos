""""
    Autor: Juan Manuel Abréu
    Fecha: 15/05/2024
    Propósito: Convertir un número decimal entero a un número romano.
"""

import os

def convertirNumeroRomano(entrada):
    try:
        numeroDecimal = int(entrada)
        if numeroDecimal > 0 and numeroDecimal < 4000:
            simbolosRomanos = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
            valoresRomanos = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
            numeroRomano = ""

            indice = len(valoresRomanos) - 1
            while numeroDecimal > 0:
                if valoresRomanos[indice] <= numeroDecimal:
                    numeroRomano += simbolosRomanos[indice]
                    numeroDecimal -= valoresRomanos[indice]
                else:
                    indice -= 1

            return numeroRomano
        else:
            raise ValueError("Error: El número debe ser mayor que 0 y menor que 4000.")

    except ValueError as e:
        raise e

    except Exception as exc:
        raise ValueError("Error: Debe introducir un número decimal entero.") from exc

entrada = input("Introduzca un número decimal entero: ")
numeroRomano = convertirNumeroRomano(entrada)
if numeroRomano != None:
    print(f"El número romano equivalente a {entrada} es: {numeroRomano}")
