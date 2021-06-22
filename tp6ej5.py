################
# Matías Locatti - @goldenx86
# Rodrigo Locatti - @ReinUsesLisp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import os
from cesar import decodificar

def principal():
    direccion = input("Archivo a decodificar: ")
    try:
        with open(direccion, "r", encoding="utf8") as entrada:
            datos = entrada.read()
            rotacion = int(input("Rotación: "))
            if rotacion < 0:
                raise ValueError
            direccion_salida = os.path.splitext(direccion)[0] + ".decode"
            with open(direccion_salida, "w", encoding="utf8") as salida:
                salida.write(decodificar(datos, rotacion))
    except FileNotFoundError:
        print(f"Archivo {direccion} no existe")
    except ValueError:
        print("Valor inválido")


if __name__ == "__main__":
    principal()

