# Autor: Elizabeth Citlalli Zapata Cortes
# Descripción: Programa que calcule el precio final de los boletos que el usuario quiera comprar.

def calculaPago(numeroBoletosA, numeroBoletosB, numeroBoletosC):
    totalPago = (numeroBoletosA * 3250) + (numeroBoletosB * 1730) + (numeroBoletosC * 850)
    return totalPago

def main():
    numeroBoletosA = int(input("Número de boletos en zona A: "))
    numeroBoletosB = int(input("Número de boletos en zona B: "))
    numeroBoletosC = int(input("Número de boletos en zona C: "))
    resultado = calculaPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)
    print("El costo total es: $%.2f" % (resultado))

main()