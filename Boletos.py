#Autor: Mariana Teyssier Cervantes
# Calcular el numero de boletos por zona y el total a pagar.

#calcular el pago total con el numero de boletos de cada seccion por la cantidad del boleto.
def calcularPago(boletosA, boletosB, boletosC):
    totalPago = float (boletosA * 3250) + (boletosB * 1730) + (boletosC * 850)
    return totalPago


#Calcular el pago e imprimirlo.
def ImprimirPago(boletosA, boletosB, boletosC):
    totalPago = calcularPago(boletosA, boletosB, boletosC)
    print("Total a pagar: $%.2f" % (totalPago))

#Preguntar al usuario el numero de boletos en cada seccion.
def main():
   boletosA = int(input("Numero de boletos en seccion A: "))
   boletosB = int(input("Numero de boletos en seccion B: "))
   boletosC = int(input("Numero de boletos en seccion C: "))
   ImprimirPago(boletosA, boletosB, boletosC)

#Llamar a la funcion -main-
main()
