################
# Matías Locatti - @goldenx86
# Rodrigo Locatti - @ReinUsesLisp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from cesar import codificar

def principal():
    direccion = input("Archivo a codificar: ")
    try:
        with open(direccion, "r", encoding="utf8") as entrada:
            datos = entrada.read()
            rotacion = int(input("Rotación: "))
            if rotacion < 0:
                raise ValueError
            with open(f"{direccion}.cesar", "w", encoding="utf8") as salida:
                salida.write(codificar(datos, rotacion))
    except FileNotFoundError:
        print(f"Archivo {direccion} no existe")
    except ValueError:
        print("Valor inválido")


if __name__ == "__main__":
    principal()

