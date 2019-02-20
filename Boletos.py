# Autor: Paulina Guerrero Ruiz
# Calcular el total a pagar de los boletos de un concierto





def calcularPago (boletosA, boletosB, boletosC):
    zonaA = boletosA*3250
    zonaB = boletosB*1730
    zonaC = boletosC*850

    totalPago = zonaA+zonaB+zonaC
    print "Numero de boletos en zona A: ", boletosA
    print "Numero de boletos en zona B: ", boletosB
    print "Numero de boletos en zona C: ", boletosC
    print ("El costo total es: %2.f $" % (totalPago))


def main():

    boletosA = int(input("Numero de boletos en zona A: "))
    boletosB = int(input("Numero de boletos en zona B: "))
    boletosC = int(input("Numero de boletos en zona C: "))
    calcularPago(boletosA,boletosB,boletosC)

main ()
