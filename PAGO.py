#Autor: Karla Ximena Rueda Ruiz
#Aplicar la técnica Top-Down para calcular el total de un salario dependiendo las horas de trabajo, ya sean normales o extras.

def main():


    Hn=int(input("Teclea las horas normales trabajadas: "))
    He=int(input("Teclea las horas extras trabajadas: "))
    Ph=int(input("Teclea el pago por hora: "))

    pagonormal=calcularPagonormal(Hn,Ph)
    print("Pago normal=", format(pagonormal, ".2f"))

    pagoextra=calcularPagoextra(He,Ph)
    print("Pago extra=", format(pagoextra, ".2f"))

    pagototal=calcularPagototal(pagonormal,pagoextra)
    print("Pago total=", format(pagototal, ".2f"))

def calcularPagonormal(Hn,Ph):
    pagonormal= Hn*Ph
    return pagonormal

def calcularPagoextra(He,Ph):
    pagoextra=(He*(1.65*Ph))
    return pagoextra

def calcularPagototal(pagonormal,pagoextra):
    pagototal= pagonormal+pagoextra
    return pagototal

main()

