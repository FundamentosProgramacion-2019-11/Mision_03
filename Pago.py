#Autor: Aline Paulette Villegas Berdejo
# Calcula el pago de un trabajador

#Calcula el pago de las horas normales trabajadas
def calcularhorasNormales(horasNormales, pagoPorHora):
    pagoHorasNormales= pagoPorHora*horasNormales
    return pagoHorasNormales

#Calcula el pago de las horas extra trabajadas
def calcularhorasExtra(horasExtra, pagoPorHora):
    pagoHorasExtra= (horasExtra)*(pagoPorHora*1.65)
    return pagoHorasExtra

#Indica las funciones que se van a correr al llamar a la funición "main()"  (Lee datos, imprime datos)
def main():
    horasNormales= int(input("Teclea las horas normales trabajadas: "))
    horasExtra= int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora= int(input("Teclea el pago por hora: "))
    hn=calcularhorasNormales(horasNormales, pagoPorHora)
    he=calcularhorasExtra(horasExtra, pagoPorHora)
    pt=hn+he #Calcula el pago total
    print("\nPago normal: $%.2f " % hn)
    print("Pago extra: $%.2f " % he)
    print("---------------------\nPago total: $%.2f " % pt)

main()