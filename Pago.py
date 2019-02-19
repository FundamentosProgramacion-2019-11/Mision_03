#FRANCISCO JAVIER GONZALEZ MOLINA A01748636
#PROGRAMA QUE CALCULA EL PAGO DE UN TRABAJADOR

#esta funcion calculara el pago que se le dara al trabajador por
#sus horas laborales normales y regresara el pago total por el horario normal.
def calcularPago (hrsTrabajadas,pagoxHora):
    pagolaboral=hrsTrabajadas*pagoxHora
    return pagolaboral

#Esta funcion calculara el pago extra, y se le aplicara un aumento del 65% que el pago comun
#al final regresara el total del pago extra.
def calcularPagoExtra (hrsextras,pagoxHora):
    pagoextra=hrsextras*((pagoxHora*.65)+pagoxHora)
    return pagoextra

#En esta funcion le pedira al usuario el valor de horas normales trabajadas, extra
#y el pago por hora. Se le imprimira el pago normal, el pago extra y el total que se le debera pagar.
def main ():
    hrsTrabajadas=int (input("Teclea las horas normales Trabajadas: "))
    hrsextras=int (input("Teclea las horas extra trabajadas: "))
    pagoxHora= int(input("Teclea el pago por hora: "))
    pagoNormal=calcularPago(hrsTrabajadas,pagoxHora)
    pagoExtra= calcularPagoExtra(hrsextras,pagoxHora)
    pagoTotal= pagoNormal+pagoExtra
    print ("""
    Pago Normal: $%.2f
    Pago Extra: $%.2f
    --------------------------
    Pago Total: $%.2f"""%(pagoNormal,pagoExtra,pagoTotal))

#llama a la funcion "main()"
main()
