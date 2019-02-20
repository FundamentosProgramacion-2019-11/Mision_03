#José Isidro Sánchez Vázquez
#Calculo del pago de un trabajador
def calculoDelPagoPorHora(horasNormales,pagoPorHora):
    pagoNormal=horasNormales*pagoPorHora
    return pagoNormal
def calculoDelPagoPorHoraExtra(horasExtras,pagoPorHora):
    costoPorHoraExtra=(pagoPorHora*.65)+pagoPorHora
    pagoExtra=costoPorHoraExtra*horasExtras
    return pagoExtra
def calculoDePagoTotal(calHorasExtra,calPorHora):
    pagoTotal=calHorasExtra+calPorHora
    return pagoTotal

def main():
    horasNormales=int(input("Teclea las horas normales trabajadas: "))
    horasExtras=int(input("Teclea las horas extras trabajadas: "))
    pagoPorHora=float(input("Teclea el pago por hora: "))
    calPorHora = calculoDelPagoPorHora(horasNormales,pagoPorHora)
    calHorasExtra = calculoDelPagoPorHoraExtra(horasExtras,pagoPorHora)
    calTotal=calculoDePagoTotal(calHorasExtra, calPorHora)
    print("Pago normal: $%.2f"%(calPorHora))
    print("Pago extra: $%.2f"%(calHorasExtra))
    print("------------------------------")
    print("Pago total: $%.2f"%(calTotal))

main()