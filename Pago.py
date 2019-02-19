#Autor Sofía Trujillo Vargas
#Hacer un programa que resuelva el total de horas que trabaja junto con su apgo y horas extras

def pagoTotal(horasTrabajadas,pagohora):
    pt=pagohora*horasTrabajadas
    return pt

def pagoExtra(horasEx,pagohora):
    he=pagohora*.65
    eh=pagohora+he
    tot=eh*horasEx
    return tot

def main():
    hh=float(input("Dame el total de horas trabajadas: "))
    ee=float(input("Dame tu total de horas extras: "))
    cc=float(input("¿Cuánto te pagan por hora: "))
    ht=pagoTotal(hh,cc)
    he=pagoExtra(ee,cc)
    pto=ht+he
    print("Pago normal: ",ht)
    print("Pago Extra: ",he)
    print("-------------------")
    print("Pago Total: ",pto)
main()