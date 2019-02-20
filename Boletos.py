#Autor: Karla Ximena Rueda Ruiz
#Aplicar la técnica Top-Down para calcular precio total de boletos de acuerdo a una zona en específico.

def main():

    boletosA = 3250
    boletosB = 1730
    boletosC = 850

    boletosA= int(input("Número de boletos en zona A : "))
    boletosB= int(input("Número de boletos en zona B : "))
    boletosC= int(input("Número de boletos en zona C : "))

    totalpago=calcularPago(boletosA, boletosB, boletosC)
    print("Total a pagar=", format(totalpago, ".2f"))


def calcularPago(boletosA, boletosB, boletosC):
        totalpago = (boletosA * 3250) + (boletosB * 1730) + (boletosC * 850)
        return totalpago


main()