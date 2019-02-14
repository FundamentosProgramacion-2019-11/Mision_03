# Autor: Juan Carlos Flores García A01376511. Grupo 02.
# Programa que pregunta al usuario cuántos boletos quiere para cada zona y calcula el total a pagar.

# Esta función calcula la cantidad a pagar de boletos de cada zona y lo suma para obtener el total.
def calcularPago(boletosA, boletosB, boletosC):
    totalPago = (boletosA * 3250) + (boletosB * 1730) + (boletosC * 850)
    return totalPago

# Función principal.
def main():
    boletosA = int(input("Número de boletos en zona A: "))
    boletosB = int(input("Número de boletos en zona B: "))
    boletosC = int(input("Número de boletos en zona C: "))
    totalPago = calcularPago(boletosA, boletosB, boletosC)
    print("El costo total es: $%.2f" % (totalPago))

# Llamada a la función principal.
main()

