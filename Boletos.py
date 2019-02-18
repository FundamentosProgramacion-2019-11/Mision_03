# Roberto Emmanuel González Muñoz A01376803
# Hay 3 zonas diferentes en el Auditorio Nacional. Se están vendiendo
# boletos para el próximo concierto de Maroma 5.
# Cada boleto para la zona A cuesta $3250, para la zona B cuesta $1730
# y para la zona C cuesta $850. Escribe un programa
# que pregunte al usuario cuántos boletos
# quiere comprar para cada zona y que imprima el total a pagar.


def calcularPago(boletoA, boletoB, boletoC):
    costoboletosA = 3250 * boletoA
    costoboletosB = 1730 * boletoB
    costoboletosC = 850 * boletoC

    totalaPagar =  costoboletosA + costoboletosB + costoboletosC

    return totalaPagar


def main():
    # Pregunta los datos al usuario.
    boletoA = int(input("Número de boletos en la zona A: "))
    boletoB = int(input("Número de boletos en la zona B: "))
    boletoC = int(input("Número de boletos en la zona C: "))

    # Calcula el total a pagar.
    totalPago = calcularPago(boletoA, boletoB, boletoC)

    # Imprime el total a pagar.
    print("El costo total es de: %.2f" % totalPago)

main()