#Luis Fernando Duran Castillo
#Calcular cuanto gana una persona con los datos que nos brimda

def pagonormal(normal, pago):
    pagonormal = normal * pago
    return pagonormal

def pagoextra(extra, pago):
    pagoextra= extra *((pago*.65)+pago)
    return pagoextra

def totaldepago(normal, extra, pago):
    pagon= pagonormal(normal,pago)
    pagox= pagoextra(extra, pago)
    total= pagon+pagox
    return total

def imprimir(normal, extra, pago):
    print("El pago Normal es de: %.2f " % pagonormal(normal, pago))
    print("El pago extra es de: %.2f " % pagoextra(extra, pago))
    print("El pago total es de: %.2f " % totaldepago(normal, extra, pago))

def main():
    normal= int(input("cuantas horas normales trabajas? "))
    extra= int(input("cuantas horas extras trabajas? "))
    pago= int(input("Cuanto ganas por hora? "))
    pagonormal(normal, pago)
    pagoextra(extra, pago)
    totaldepago(normal, extra, pago)
    imprimir(normal, extra, pago)

main()