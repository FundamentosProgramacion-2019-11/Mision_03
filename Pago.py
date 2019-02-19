#Autor: Victor Manuel Ceron Navarrete
#Descripcion: Calcula el pago semanal de acuerdo a horas, horas extra de cada trabajador

def PagaNormal(Normal, Hora):
    pagoNormales = Normal*Hora
    return pagoNormales

def PagoTExtra(Extras, Hora):
    pagoExtras = Extras*1.65*Hora
    return pagoExtras

def Total(pagoNormales, pagoExtras):
    pagoTotal = pagoNormales + pagoExtras
    return pagoTotal

def main():
    Normal = int(input("horas normales trabajadas: "))
    Extras = int(input("horas extras trabajadas: "))
    Hora = int(input("pago por hora: "))
    pagoHorasNormales = PagaNormal(Normal, Hora)
    pagoHorasExtras = PagoTExtra(Extras, Hora)
    pagoHorasTotales = Total(pagoHorasNormales, pagoHorasExtras)
    print("Pago normal: $ %.2f"%pagoHorasNormales)
    print("Pago extra: $ %.2f"%pagoHorasExtras)
    print("-----------------------------")
    print("Pago total: $ %.2f"%pagoHorasTotales)

main()