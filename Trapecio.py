# Autor: Jose Luis Mata Lomeli
# Objetivo: Dadas la altura, la base mayor y menor de un trapecio isoceles, calcular e imprimir el area y perimetro

# Calcular Area
def area(baseMayor, baseMenor, altura):

    # Formula del Area
    area=((baseMayor+baseMenor)/2)*altura
    return area #Regresar resultado

#Calcular Perimetro
def perimetro(baseMayor, baseMenor, altura):

    # Como necesitamos sumar todos los lados para sacar el perimetro y nos faltan dos (los lados oblicuos son iguales)
    catetoAdyacente=(baseMayor-baseMenor)/2
    hipotenusa = (catetoAdyacente**2+altura**2)**(1/2)

    # Calcular perimetro
    perimetroTotal = hipotenusa+hipotenusa+baseMayor+baseMenor
    return perimetroTotal #Regresar el resultado


# Funcion Principal
def main():

    #Leer los datos dados por el usuario
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))

    #Llamar a las funciones que calculen el Area y el Perimetro (con los parametros dados)
    areaFigura = area(baseMayor, baseMenor, altura)
    perimetroFigura=perimetro(baseMayor,baseMenor,altura)

    #Imprimir los resultados
    print("Area: %.2f" % (areaFigura))
    print("Perimetro: %.2f" % (perimetroFigura))

main()