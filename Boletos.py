#Autor: María Fernanda García Gastélum A01376181
#Calcular el precio de boletos para un concierto

def calcularPago(boletosA, boletosB, boletosC):
    totalPago= (boletosA * 3250)+(boletosB * 1730)+(boletosC * 850)
    return totalPago

def main():
    boletosA= int(input("Numero de boletos en zona A: "))
    boletosB= int(input("Numero de boletos en zona B: "))
    boletosC= int(input("Numero de boletos en zona C: "))
    calcularPago(boletosA, boletosB, boletosC)
    print("El costo total es: $ %.2f" % calcularPago(boletosA, boletosB, boletosC))

main()
