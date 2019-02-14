#Autor: Mariana Teyssier Cervantes
# Calcular el rendimiento de un auto en km/litros y millas/galones.


#calcular el rendimiento del auto dividiendo los kilometros recorridos sobre los litros usados.
def calcularKL(km, litros):
    kl = float(km)/float (litros)
    return kl

#imprimir el rendimiento en kilometros sobre litros.
def ImprimirKL(km, litros):
    kl = calcularKL(km, litros)
    print"\nSi recorres",(km),"kilometros con",(litros),"litros de gasolina, el rendimiento es: "
    print("%.2f km/l" % (kl))

#calcular con conversiones cuantas millas sobre galones representan los kilometros sobre litros.
def calcularMG(km, litros):
    milla = float(km / 1.6093)
    galones = float(litros * .264)
    mg = float(milla / galones)
    return mg

#imprimir el rendimiento en millas sobre galones.
def ImprimirMG(km, litros):
    mg = calcularMG(km, litros)
    print ("%.2f mi/gal" % (mg))

#calcular cuantos litros son necesarios para recorrer los kms deseados
#multiplicando los kms deseados por el rendimiento.
def calcularLitrosNecesarios(km, litros, kmPorRecorrer):
    kl = float (km) / float(litros)
    recorrer = kmPorRecorrer / kl
    return recorrer

#imprimir los litros necesarios para recorrer la distancia querida.
def ImprimirLitrosNecesarios(km, litros, kmPorRecorrer):
    recorrer = calcularLitrosNecesarios(km, litros, kmPorRecorrer)
    print"\nPara recorrer", (kmPorRecorrer), "km. necesitas %.2f" % (recorrer), "litros de gasolina."

#preguntarle al usuario cuantos kms ha recorrido, cuantos litros a utilizado
#preguntarle al usuario cuantos kilometros va a recorrer.
def main():
    km = int(input("Teclea el numero de kms recorridos: "))
    litros = int(input("Teclea el numero de litros de gasolina utilizados: "))
    ImprimirKL(km, litros)
    ImprimirMG(km, litros)
    kmPorRecorrer = int(input("\nCuantos kilometros vas a recorrer: "))
    ImprimirLitrosNecesarios(km, litros, kmPorRecorrer)

#Llamar la funcion -main-
main()
