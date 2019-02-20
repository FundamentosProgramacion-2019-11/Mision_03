#Karimn Daniel Hernández Castorena
#Programa que calcula el pago de un trabajador


def calcularPrecioNormal(hn,ph):
    pn = hn * ph
    return pn

def calcularPagoExtra(he,ph):
    pe = he * (ph * 1.65)
    return pe

def main():
    hn=int(input("Teclea las horas normales trabajadas "))
    he=int(input("Teclea las horas extras trabajadas "))
    ph=int(input("Teclea el pago por hora "))

    pn=calcularPrecioNormal(hn,ph)
    pe=calcularPagoExtra(he,ph)
    pt=pn + pe

    print ()
    print("Pago normal:$ %.2f " % pn)
    print("Pago extra:$ %.2f " % pe)
    print("----------------------")
    print("Pago total:$ %.2f " % pt)
main()



