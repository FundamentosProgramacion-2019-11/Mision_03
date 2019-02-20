#Autor: Katia Hernández Barrera
#Descripción: programa que calcula el pago total de un trabajador


def main():
    horasNormales = int(input("teclea las horas normales trabajadas"))
    horasExtras = int(input("teclea las horas extras trabajadas"))
    pagoHora = int(input("teclea el pago por hora"))
    normal = calcularNormal (horasNormales, horasExtras, pagoHora)
    print("Pago normal: %.2f" % normal)
    extra = calcularExtra(horasNormales, horasExtras, pagoHora)
    print("Pago extra: %.2f" % extra)
    total = calcularTotal(horasNormales, horasExtras, pagoHora)
    print("Pago total: %.2f" % total)

def calcularNormal(horasNormales, horasExtras, pagoHora):
    normal = horasNormales * pagoHora
    return normal


def calcularExtra(horasNormales, horasExtras, pagoHora):
    extra = horasExtras * (pagoHora * 0.65 + pagoHora)
    return extra

def calcularTotal (horasNormales, horasExtras, pagoHora):
    total = (horasNormales * pagoHora) + (horasExtras * (pagoHora * 0.65 + pagoHora))
    return total
main()