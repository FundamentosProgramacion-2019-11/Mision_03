#Autor: Eric Jardón Chao
#Boletos para un concierto: calcula el costo total de los boletos de tres diferentes zonas a diferente precio.

#La función main recibe los datos de entrada, corre las funciones e imprime los datos de salida.
def main():
    boletosA=int(input("Boletos Zona A:"))
    boletosB = int(input("Boletos Zona B:"))
    boletosC = int(input("Boletos Zona C:"))
    costo=calcularPago(boletosA,boletosB,boletosC)
    print("El costo total de los boletos es de $%.2f" % (costo))

def calcularPago(a,b,c): #Esta función calcula el costo al multiplicar el número de boletos por su precio y sumar los tres tipos de boleto
    a=a*3250
    b=b*1730
    c=c*850
    total=a+b+c
    return total
main()
#Fin del programa