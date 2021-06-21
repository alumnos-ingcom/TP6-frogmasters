################
# Matías Locatti - @goldenx86
# Rodrigo Locatti - @ReinUsesLisp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def palabra_a_hex(palabra):
    return list(map(ord, palabra))

def codigo_anagrama(palabra):
    palabra = palabra.lower()
    for caracter in " ,":
        palabra = palabra.replace(caracter, "")
    for (caracter, remplazo) in zip("áíúéó", "aiueo"):
        palabra = palabra.replace(caracter, remplazo)
    codigo = palabra_a_hex(palabra)
    codigo.sort()
    return codigo

def es_anagrama(palabra_a, palabra_b):
    return codigo_anagrama(palabra_a) == codigo_anagrama(palabra_b)


def principal():
    palabra_a = input("Inserte palabra: ")
    palabra_b = input("Inserte palabra: ")
    if es_anagrama(palabra_a, palabra_b):
        print("Las palabras son anagramas")
    else:
        print("Las palabras no son anagramas")

if __name__ == "__main__":
    principal()

