def rotar_caracter_rango(caracter, posiciones, base, limite):
    base = ord(base)
    relativo = ord(caracter) - base
    modificado = relativo + posiciones
    rotado = modificado % limite
    return chr(rotado + base)

def rotar_caracter(caracter, posiciones):
    if caracter >= 'a' and caracter <= 'z':
        return rotar_caracter_rango(caracter, posiciones, 'a', 26)
    if caracter >= 'A' and caracter <= 'Z':
        return rotar_caracter_rango(caracter, posiciones, 'A', 26)
    if caracter >= '0' and caracter <= '9':
        return rotar_caracter_rango(caracter, posiciones, '0', 10)
    return caracter

def codificar(cadena, posiciones):
    return "".join(map(lambda caracter : rotar_caracter(caracter, posiciones), cadena))

def decodificar(cadena, posiciones):
    return codificar(cadena, -posiciones)
