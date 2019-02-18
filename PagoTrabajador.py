#Autor: Ivana Olvera Mérida A01746744
#Escribir un programa que lea las horas normales, las horas extras y el pago por hora de un trabajador.

def calcularPagoTotal (pagoNormal, pagoExtra):
    pagoTotal = pagoNormal + pagoExtra
    return pagoTotal

def calcularPagoExtra (horaExtra, pagoHora):
    pagoExtra = (horaExtra*pagoHora)*1.65
    return pagoExtra

def  calcularPagoNormal (horaNormal, pagoHora):
    pagoNormal = horaNormal * pagoHora
    return pagoNormal

def main ():
    horaNormal= int(input("Teclea las horas normales trabajadas: "))
    horaExtra= int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    pagoNormal = calcularPagoNormal(horaNormal, pagoHora)
    pagoExtra = calcularPagoExtra(horaExtra, pagoHora)
    pagoTotal = calcularPagoTotal(pagoNormal, pagoExtra)

    print("Pago normal: $%.2f" % (pagoNormal))
    print("Pago extra: $%.2f" % (pagoExtra))
    print("El pago total es: $%.2f" %(pagoTotal))

main ()
