#Autor: david Yair Fernández Salas
#Este programa te dice cuantos litros necesita tu carro para avanzar.


"""En este problema se uso la funcion de CalcularRendimiento, con los parametros de km y litros
 la funcion realiza los calculos corrwpondientes y nos regresa Rendimiento"""
def CalcularRendimiento(km, litros):
    Rendimiento=(km/litros)
    return Rendimiento

"""Se uso la función CalcularRendimeintomillas con los parametros de km y litros,
para que realizara los claculos y la conversión a galones y nos diera el resultado en galones 
y nos regresara el valor en CalcularRendimientomillas"""

def CalcularRendimientomillas(km, litros):
    Rendimientomi=(km/ litros)
    gal= (Rendimientomi/1.6093)/0.264
    return gal
"""Se usó la función Calcularlitros con los parametros de km usados que se obtuvo con la función de main y
lo mismo para litrosGas, la función realizó la operación y nos dio el rendimiento en millas, mismo que se regreso
para poder cambiar el valor de Calcularlitros"""
def Calcularlitros(kmusados ,kmR,LitrosGas):
    Rendimientomi=(kmusados/CalcularRendimiento(kmR,LitrosGas))
    return Rendimientomi
"""Se uso la función main, para que el programa pudiera correr bien, y aqui se introdujo todas las variables a preguntar
para que el usuario introdujera los valores, se realizó la operación para calcular los kmusados y los miusados , para 
 las funciones de arriba y nos imprimiera los datos deseadps"""
def main():
    kmR=float(input("Teclea el número de km recorridos: "))
    LitrosGas=float(input("Teclea el número de litros de gasolina usados: "))

    kmusados=CalcularRendimiento(kmR,LitrosGas)
    miusados=CalcularRendimientomillas(kmR,LitrosGas)


    print("")
    print("Si recorres {} kms con {} litros de gasolina, el rendimiento es: ".format(kmR, LitrosGas))
    print("{:0.2f} km/l".format(kmusados))
    print("{:0.2f} mi/gal".format(miusados))
    print("")
    kmusados=float(input(" ¿Cuántos kilometros vas a recorrer? "))
    Litrosnecesarios=Calcularlitros(kmusados,kmR,LitrosGas)
    print('Para recorrer %5.2f' % (kmusados),'km, necesitas %5.2f' % (Litrosnecesarios),'litros de gasolina')

main()