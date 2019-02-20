# Rosalía Serrano Herrera
# Pregunta al usuario cuántos boletos por cada zona del Auditorio Nacional quiere comprar e imprime el total a pagar

def calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    totalPago = (numeroBoletosA * 3250) + (numeroBoletosB * 1730) + (numeroBoletosC * 850)
    return totalPago

def main():
    numeroBoletosA = int(input("Número de boletos en zona A: "))
    numeroBoletosB = int(input("Número de boletos en zona B: "))
    numeroBoletosC = int(input("Número de boletos en zona C: "))
    totalPago = calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.2f" % (totalPago))

main()
