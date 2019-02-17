def pagoHoras(cantidadXHora,horas):
    Tp = cantidadXHora*horas
    return Tp
def HorasExtr(cantidadXHora,horasExtra):
    cp = cantidadXHora*.65
    ct = cp+cantidadXHora
    pt = ct*horasExtra
    return pt
def main ():
    CantH = float(input("¿Cuánto se paga por hora?"))
    HoraN = float(input("¿Cuántas horas normales trabajó?"))
    HoraE = float(input("¿Cuantas horas extra trabajó?"))
    x = pagoHoras(CantH,HoraN)
    y = HorasExtr(CantH,HoraE)
    z = x+y
    print("Pago normal: ",round(x,2),"$")
    print("Pago extra: ", round(y, 2), "$")
    print("Pago total: ", round(z, 2), "$")
main()