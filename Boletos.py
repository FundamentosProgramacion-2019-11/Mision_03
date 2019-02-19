#Autor: Daniela Estrella Tovar
# Descripción: Imprimir el pago total según los boletos comprados

def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    pagoTotal= numeroBoletosA*3250 + numeroBoletosB*1730 +numeroBoletosC *850
    return pagoTotal


def main():
    numeroBoletosA = int(input("Número de boletos en zona A: "))
    numeroBoletosB = int(input("Número de boletos en zona B: "))
    numeroBoletosC = int(input("Número de boletos en zona C: "))
    pagoTotal= calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El Costo total es:  $ %.2f" % (pagoTotal))

main()