#Mariana Coria Rodríguez A01374765
#Pago normal y extra de un trabajador

def pagoNormal(normales, porHora):
    pago = normales*porHora
    return pago

def pagoExtra(extras, porHora):
    extra = extras*1.65*porHora
    return extra

def total(pagoNormal, pagoExtra):
    pagoTotal = pagoNormal + pagoExtra
    return pagoTotal


def main():
    normales = int(input("Teclea las horas normales trabajadas: "))
    extras = int(input("Teclea las horas extras trabajadas: "))
    porHora = int(input("Teclea el pago por hora: "))
    horasNormales = pagoNormal(normales, porHora) #definir siempre en cada función y que correpondan los nombres
    horasExtra = pagoExtra(extras, porHora)
    horasTotales = total(horasNormales, horasExtra)
    print("Pago normal: $ %.2f " % horasNormales)
    print("Pago extra: $ %.2f " % horasExtra)
    print("Pago total: $ %.2f " % horasTotales)


main()