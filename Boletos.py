#Autor: Aline Villegas Berdejo
#Pregunta al usuario cuantos boletos quiere comprar para cada zona y cual es su costo total

#calcula el pago total de los boletos deseados
def calcularPago(numeroDeBoletosA, numeroDeBoletosB, numeroDeBoletosC):
    pagoDeBoletosA= numeroDeBoletosA*3250
    pagoDeBoletosB= numeroDeBoletosB*1730
    pagoDeBoletosC= numeroDeBoletosC*850
    totalPago= pagoDeBoletosA+ pagoDeBoletosB+ pagoDeBoletosC
    return totalPago

#Indica las funciones que se van a correr al llamar a la funición "main()"  (Lee datos, imprime datos)
def main():
    numeroDeBoletosA= int(input("Número de boletos en zona A: "))
    numeroDeBoletosB= int(input("Número de boletos en zona B: "))
    numeroDeBoletosC= int(input("Número de boletos en zona C: "))
    totalPago= calcularPago(numeroDeBoletosA, numeroDeBoletosB, numeroDeBoletosC)
    print("El costo total es: $%.2f" % totalPago)

main()
