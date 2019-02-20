#José Isidro Sánchez Vázquez
#Boleos para un concierto
def calcularPagoDeBoletosA(numeroBoletosA):
    costoDelBoletoA=numeroBoletosA*3250
    return costoDelBoletoA
def calcularPagoDeBoletosB(numeroBoletosB):
    costoDelBoletoB=numeroBoletosB*1730
    return costoDelBoletoB
def calcularPagoDeBoletosC(numeroBoletosC):
    costoDelBoletoC=numeroBoletosC*850
    return costoDelBoletoC
def calculoTotalDePrecio(costoDelBoletoA,costoDelBoletoB,costoDelBoletoC):
    costoTotal=costoDelBoletoA+costoDelBoletoB+costoDelBoletoC
    return costoTotal

def main():
    numeroBoletosA = int(input("¿Cuantos boletos en la zona A quieres?:"))
    numeroBoletosB = int(input("¿Cuantos boletos en la zona B quieres?:"))
    numeroBoletosC = int(input("¿Cuantos boletos en la zona C quieres?:"))
    costoDelBoletoA=calcularPagoDeBoletosA(numeroBoletosA)
    costoDelBoletoB=calcularPagoDeBoletosB(numeroBoletosB)
    costoDelBoletoC=calcularPagoDeBoletosC(numeroBoletosC)
    costoTotal=calculoTotalDePrecio(costoDelBoletoA,costoDelBoletoB,costoDelBoletoC)
    print("Numero de boletos en la zona A:",numeroBoletosA)
    print("Numero de boletos en la zona B:",numeroBoletosB)
    print("Numero de boletos en la zona C:",numeroBoletosC)
    print("El costo total es: $%.2f"% (costoTotal))
main()