################
# Matías Locatti - @goldenx86
# Rodrigo Locatti - @ReinUsesLisp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from tp6ej1 import es_anagrama

def principal():
    lineas = None
    with open("anagramas.txt", "r", encoding="utf8") as file:
        lineas = file.readlines()
    for linea in lineas:
        linea = linea.replace("\n", "")
        if linea == "":
            continue
        (palabra_a, palabra_b) = linea.split("–", 1)
        resultado = "" if es_anagrama(palabra_a, palabra_b) else "no "
        print(f"Las palabras \"{palabra_a.strip()}\" y \"{palabra_b.strip()}\" {resultado}son anagramas")

if __name__ == "__main__":
    principal()

