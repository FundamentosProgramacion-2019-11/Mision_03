#Autor: Daniela Estrella Tovar
# Descripción: Dadas las horas trabajadas, las horas extra, y el pago por hora, calcular el pago normal, el pago extra y el pago total.

def calcularPagoNormal(horasTrabajo, pago):
    pagoNormal= horasTrabajo*pago
    return pagoNormal
def imprimirPagoNormal(horasTrabajo, pago):
    pagoNormal= calcularPagoNormal(horasTrabajo, pago)
    print(""" 
Pago Normal: $%.2f""" % (pagoNormal))

def calcularPagoExtra(horasExtra,pago):
    pagoExtra= horasExtra* pago *1.85
    return pagoExtra

def imprimirPagoExtra(horasExtra, pago):
    pagoExtra= calcularPagoExtra(horasExtra,pago)
    print("""Pago Extra: $%.2f"""% (pagoExtra))

def calcularPagoTotal(horasExtra,horasTrabajo,pago):
    pagoExtra=calcularPagoExtra(horasExtra, pago)
    pagoNormal=calcularPagoNormal(horasTrabajo, pago)
    pagoTotal= pagoNormal + pagoExtra
    return pagoTotal

def imprimirPagoTotal(horasExtra,horasTrabajo,pago):
    pagoTotal= calcularPagoTotal(horasExtra,horasTrabajo,pago)
    print("""
Pago Total= $%.2f """%(pagoTotal))


def main():
    horasTrabajo= int(input("Teclea las horas normales trabajadas: "))
    horasExtra= int(input("Teclea las horas extra trabajadas: "))
    pago= int(input("Teclea el pago por hora: "))
    imprimirPagoNormal(horasTrabajo, pago)
    imprimirPagoExtra(horasExtra,pago)
    imprimirPagoTotal(horasExtra,horasTrabajo,pago)

main()