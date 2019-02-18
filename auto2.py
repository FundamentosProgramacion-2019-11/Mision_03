#RafaelRomeroBello
#A01747730
#18/02/2019
#Este programa realiza conversiones de km entre l a millas entre galones igual calcula cuanta gasolina necesitas para recorrer una distancia
def calcularKM(km, l):
    conversionkml=km/l
    return conversionkml
def calcularMG(km, l):
    conversionMg=(km/l)*2.352
    return conversionMg
def calcularRecorrido(dis, l2):
    liusados=dis/l2
    return liusados
def main ():
    km1=float(input("inserte los kilometros:"))
    lit=float(input("inserte los litros:"))
    kmL=calcularKM(km1,lit)
    mg1=calcularMG(km1,lit)
    print("si recorres:%.2f"%(km1),"kms con:%.2f"%(lit),"litros de gasolina, tu rendimiento va a ser de:")
    print("%.2f"%(kmL),"km/l")
    print("%.2f"%(mg1),"mi/gal")
    kmNuevos=float(input("¿Cuantos kilometros vas a recorrer?"))
    litrosUsados=calcularRecorrido(kmNuevos, kmL)
    print("para recorrer:%.2f"%(kmNuevos),"necesistas:%.2f"%(litrosUsados),"litros de gasolina")


main()





