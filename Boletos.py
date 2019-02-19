# Roberto Castro Barrios A01748559
# Descripción: Programa que de acuerdo a los tipos de boletos que seleccionas, calcula el pago total.
#Costo por un boleto en zona A = 3250
#Costo por un boleto en zona B = 1730
#Costo por un boleto en zona C = 850

#Esta funcion calcula el costo total en base a la cantidad de boletos comprados
def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC) :
    totalPago = (numeroBoletosA*3250)+(numeroBoletosB*1730)+(numeroBoletosC*850)
    return totalPago

#Esta es la funcion principal; encargada de leer, imprimir y recibir las funciones.
def main () :
    numeroBoletosA = int(input("Número de boletos en zona A: "))
    numeroBoletosB = int(input("Número de boletos en zona B: "))
    numeroBoletosC = int(input("Número de boletos en zona C: "))
    calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El total a pagar es de: $ %.2f"%(totalPago))

#Llama a la función -main-
main ()
