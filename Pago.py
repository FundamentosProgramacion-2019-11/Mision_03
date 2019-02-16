# Autor: Alan Giovanni Rodriguez Camacho A01748185
# Descripcion: Calcula el pago normal y el pago de horas extra de un trabajador.

def calcularPagoNormal(horasN,pagoPerH):#CAlcula el pago de horas normales de un trabajador.
    pagoNormal=horasN*pagoPerH

    return pagoNormal



def calcularPagoExtra(horasE,pagoPerH):#Calcula el pago de horas extras de un trabajador.
    pagoExtra=(pagoPerH*1.65)*horasE

    return pagoExtra


def main():
    horasN=int(input("Teclea las horas normales trabajadas: "))
    horasE=int(input("Teclea las horas extras trabajadas: "))
    pagoPerH=int(input("Teclea el pago por hora: "))
    n=calcularPagoNormal(horasN,pagoPerH)
    e=calcularPagoExtra(horasE,pagoPerH)
    Total=n+e
    print("Pago normal: $%.2f"% n)
    print("Pago extra: $%.2f" % e)
    print("--------------------")
    print("Pago total: $%.2f" % Total)

main()