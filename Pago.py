#Autor: César Guzmán Guadarrama
#Descripción: Este programa calculará e imprimirá los datos de pago semanal a un empleado

def calcularHnormales(pagoHora,horasNormales):            #esta función calcula el pago de las horas normales de trabajo
    horasN = pagoHora * horasNormales
    return horasN

def calcularHextras(pagoHora,horasExtras):           #Esta función calcula el pago de las horas extras
    horasE = ((pagoHora*.65) + pagoHora) * horasExtras
    return horasE


def main():         #función principal pide datos para resolver el problema
    pagoHora = float(input("Cuanto le pagas a un trabajador por hora?"))
    horasNormales = float(input("Cuantas horas trabajo?"))
    horasExtras = float(input("Cuantas horas extra trabajo?"))
    print("el pago normal es de $",calcularHnormales(pagoHora,horasNormales))
    print("el pago extra es de $",calcularHextras(pagoHora,horasExtras))
    pt = calcularHnormales(pagoHora,horasNormales)+calcularHextras(pagoHora,horasExtras)
    print("el pago total es de $",pt)

main()