#Emiliano Tartarini
#boletos

def calcularPago(boletosZonaA, boletosZonaB, boletosZonaC):

    TotalPago= (boletosZonaA * 3250)+(boletosZonaB * 1730)+(boletosZonaC * 850)
    return TotalPago


def main():

    boletosZonaA= int(input("Número en zona A:"))
    boletosZonaB= int(input("Número en zona B:"))
    boletosZonaC= int(input("Número en zona C:"))

    TotalPago = calcularPago(boletosZonaA, boletosZonaB, boletosZonaC)

    print("El costo total es: $%.2f" % (TotalPago))

main()