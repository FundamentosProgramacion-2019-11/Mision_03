#Bruno Omar Jiméenz Mancilla
#Programa que calcula csotos de boletos

def calcularPago(boletosA, boletosB, boletosC) :
    A = boletosA*3250.00
    B = boletosB*1730.00
    C = boletosC*850.00
    totalPago = A+B+C
    return totalPago
def main() :
    ba = int(input("¿Cuántos boletos quieres para la zona A?: "))
    bb = int(input("¿Cuántos boletos quieres para la zona B?: "))
    bc = int(input("¿Cuántos boletos quieres para la zona C?: "))
    x = calcularPago(ba,bb,bc)
    print("El total a pagar por los boletos es:  $",round(x,2))


main()
