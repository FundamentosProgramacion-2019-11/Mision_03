#Luis Adrian Carmona Villalobos
#A01748395

#Luis Adrian Carmona Villalobos
#A01748395
def calcularPago(boletosA, boletosB, boletosC):
    precioA = boletosA * 3250
    precioB = boletosB*1730
    precioC = boletosC*850
    totalPago = precioA+precioB+precioC
    return  totalPago

def main():
    boletosA = int(input("Cuantos boletos quiere para zona A? "))
    boletosB = int(input("CUantos boletos quiere para zona B? "))
    boletosC = int(input("Cuantos boletos quiere para zona C"))

    pago = calcularPago(boletosA, boletosB, boletosC)
    print("Numero de boletos en zona A: {0} ".format(boletosA))
    print("Numero de boletos en zona B: {0} ".format(boletosB))
    print("Numero de boletos en zona C: {0} ".format(boletosC))
    print("Su costo es de:$ %.2f" %pago)
main()
