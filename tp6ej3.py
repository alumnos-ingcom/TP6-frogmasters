################
# Matías Locatti - @goldenx86
# Rodrigo Locatti - @ReinUsesLisp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import shutil
## Se provee emiya.txt como archivo de ejemplo


def copia(entrada, salida):
    """
    Copia el contenido de un archivo existente a uno de salida.
    Si el archivo de salida no existe, será creado.
    """
    try:
        shutil.copyfile(entrada,salida)
    except IOError:
        print("No se puede abrir el archivo", entrada, ".")
    else:
        print("Copia realizada con éxito.")
    return


def principal():
    archivo_entrada = input("Ingrese el nombre del archivo de entrada: ")
    archivo_salida = input("Ingrese el nombre del archivo de salida: ")
    copia(archivo_entrada, archivo_salida)
    

if __name__ == "__main__":
    principal()