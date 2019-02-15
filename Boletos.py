#Autor: Luis Alberto Zepeda Hernandez, A01328616
#Descripcion: crea programa  programa que pregunte al usuario cuántos boletos quiere comprar para cada zona y que imprima el total a pagar.


#Esta función se encarga de calcular el pago total, con la información que se recolectó al incio

def calcularPago(boletosZonaA, boletosZonaB, boletosZonaC):
    costoBoletosZonaA = boletosZonaA * 3250
    costoBoletosZonaB = boletosZonaB * 1730
    costoBoletosZonaC = boletosZonaC * 850
    totalPago = costoBoletosZonaA + costoBoletosZonaB +costoBoletosZonaC
    return totalPago

#Esta función llama pide información al usuario, llama a una funcion para calcular el pago y tambien imprime el resultado

def main():
    boletosZonaA = int(input("Número de boletos en zona A: "))
    boletosZonaB = int(input("Número de boletos en zona B: "))
    boletosZonaC = int(input("Número de boletos en zona C: "))
    pago = calcularPago(boletosZonaA, boletosZonaB, boletosZonaC)
    print("El costo total es:", "$" "{0:.2f}".format(pago))


main()