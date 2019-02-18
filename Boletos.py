# Autor David Yair Fernández Salas
# Este programa te dice cual boletos quieres y te dice el costo.

"""Escribe la función calcularPago que recibe como parámetros el número de boletos que quiere comprar para cada zona y regresa el
total a pagar."""

def CalcularPago(boletosA, boletosB, boletosC):
    TotalBoletoA = boletosA* 3250
    TotalBoletoB = boletosB* 1730
    TotalBoletoC = boletosC* 850
    Pago = TotalBoletoA+ TotalBoletoB+ TotalBoletoC
    return Pago

"""Función main, sirve para que cuando el usuario indica el número de boletos que quiere, está envia los datos a la
funcion def CalcularPago y al final se imprime el resultado deseado"""

def main():
    numeroBoletosA = float(input("Número de boletos de clase A: "))
    numeroBoletosB = float(input("Número de boletos de clase B: "))
    numeroBoletosC = float(input("Número de boletos de clase C: "))
    TotalPago = CalcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $ %.2f" % (TotalPago))
main()
