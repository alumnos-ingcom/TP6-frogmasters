################
# Matías Locatti - @goldenx86
# Rodrigo Locatti - @ReinUsesLisp
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def etiqueta(etiqueta, *contenidos):
    resultado = f"<{etiqueta}>"
    for contenido in contenidos:
        resultado += contenido
    resultado += f"</{etiqueta}>"
    return resultado


def principal():
    print(etiqueta("html",
                   etiqueta("body",
                            etiqueta("h1", "Hola HTML"),
                            etiqueta("p", "Esto es un párrafo"))))


if __name__ == "__main__":
    principal()
