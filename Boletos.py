# Autor: Ronaldo Estefano Lira Buendia
# Calcular de los boletos seleccionados para cada zona el total

def calcularPago(boletosA, boletosB, boletosC):
    bA = boletosA * 3250
    bB = boletosB * 1730
    bC = boletosC * 850
    total = bA + bB + bC
    return total

def main ():
    boletosA = int(input("Ingrese el numero de boletos para la zona A: "))
    boletosB = int(input("Ingrese el numero de boletos para la zona B: "))
    boletosC = int(input("Ingrese el numero de boletos para la zona C: "))
    print("Numero de boletos en zona A: ", boletosA)
    print("Numero de boletos en zona B: ", boletosB)
    print("Numero de boletos en zona C: ",boletosC)
    total = calcularPago(boletosA, boletosB, boletosC)
    print("El costo total es: ${0:.2f}".format(total))


main ()
