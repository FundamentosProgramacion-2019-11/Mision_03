#Autor: César Guzmán Guadarrama
#Descripción: Este programa te dira el redimiento de tu vehiculo y tmabién te dira los litro de gasolina que necesitaras

def calcularRendimento(km,litros):         #función para darte el rendimento en km/l
    Rendimiento = km / litros
    return Rendimiento

def calcularRendimiento2(km,litros):       #función para darte el rendimiento en mi/gal
    milla = km / 1.6093
    galon = litros * 0.264
    Rend2 = milla / galon
    return Rend2

def calcularGas (Kmc,km,litros):  #esta funcion te dice cuanta gasolina necesitas para recorrer los kilometros dados en base al rendimiento
    Kmc1 = Kmc / calcularRendimento(km,litros)
    return Kmc1



def main():              #función principal pide datos para resolver el problema
    km = float(input("Teclea el numero de km recorridos"))
    litros = float(input("Teclea el numero de litros que utilizaste"))
    print("si recorres ",km, "km con",litros, "litros de gasolina, el rendimiento es :\n",
          round(calcularRendimento(km,litros),2),"km/l\n",
          round(calcularRendimiento2(km,litros),2), "mi/gal")
    Kmc = float(input("Cuantos kilometros recorreras?"))
    print("Para recorrer ",Kmc, "km. necesitas ",round(calcularGas(Kmc,km,litros),2), "litros de gasolina")


main()