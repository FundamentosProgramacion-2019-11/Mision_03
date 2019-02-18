# Autor: YadiraFuentesCalderón, A01745235
# Descripcion: Calcular el costo total de boletos en diferentes zonas.

def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    totalPago = numeroBoletosA*3250+numeroBoletosB*1730+numeroBoletosC*850
    return totalPago

def main():
    numeroBoletosA = int(input("Número de boletos en zona A:"))
    numeroBoletosB = int(input("Número de boletos en zona B:"))
    numeroBoletosC = int(input("Número de boletos en zona C:"))

    totalPago= calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC)

    print("El costo total es: $%.2f"%(totalPago))
main()