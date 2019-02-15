#Autor: Luis Alberto Zepeda Hernandez, A01328616
#Descripcion: Escribe un programa que lea la base mayor, la base menor y la altura de un trapecio isósceles y que imprima: - Área. - Perímetro.



#Esta función se encarga de calcular el perimetro, llamando a otra función que calculó el lado del trapecio,
#y con esto realiza una operación para sacar un resultado y regresarlo.

def calcularPerimetro(baseMayor, baseMenor, altura):
    perimetro = (calcularLadoTrapecio(baseMayor, baseMenor, altura) * 2) + baseMenor + baseMayor
    return perimetro

#Esta función calcula un lado del trapecio, regresa el valor, para poder calcular el perímetro.

def calcularLadoTrapecio(baseMayor, baseMenor, altura):
    x = (baseMayor - baseMenor) / 2
    lado = ((x) ** 2 + (altura) ** 2) ** .5
    return lado

#Esta función calcula el área, con los datos recolectados en la función main, y los regresa.

def calcularArea(baseMayor, baseMenor, altura):
    area =  ((baseMayor + baseMenor) / 2) * altura
    return area

#Esta función pide información al usuario, llama funciones para calcular área y perímetro, al final imprime resultados.

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calcularArea(baseMayor,baseMenor,altura)
    perimetro = calcularPerimetro(baseMayor,baseMenor, altura)
    print("Área: ""{0:.2f}".format(area))
    print("Perímetro: ""{0:.2f}".format(perimetro))


main()