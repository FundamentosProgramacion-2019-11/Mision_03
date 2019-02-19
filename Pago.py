#Autor: Mario Hernández Cárdenas
# Calcular el pago de horas trabajadas y horas extras

def calcularPagoNormales(horasNormales, pagoHora):   #Multiplica las horas normales por el pago por hora
    pagoNormales = horasNormales * pagoHora
    return pagoNormales

def calcularPagoExtras(horasExtras, pagoHora):   #Multiplica las horas extras por el pago por hora
    pagoExtras = horasExtras * pagoHora * 1.65
    return pagoExtras

def calcularPagoTotal(pagoNormales, pagoExtras):     #Suma el pago de horas normales y extras trabajadas
    total = pagoNormales + pagoExtras
    return total

def main():
    horasNormales = int(input("Teclea las horas normales trabajadas: "))
    horasExtras = int(input("Teclea las horas extras trabajadas: "))
    pagoHora = int(input("Teclea el pago por hora: "))
    pagoNormales = calcularPagoNormales(horasNormales, pagoHora)
    pagoExtras = calcularPagoExtras(horasExtras, pagoHora)
    pagoTotal = calcularPagoTotal(pagoNormales, pagoExtras)
    print("Pago normal: $ %.2f"%pagoNormales)
    print("Pago extra: $ %.2f"%pagoExtras)
    print("-----------------------")
    print("Pago total: $ %.2f"%pagoTotal)

main()