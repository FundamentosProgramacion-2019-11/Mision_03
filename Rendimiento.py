# Autor: Jose Luis Mata Lomeli
# Objetivo: Crear un programa que lea el numero de km recorridos y la cant. de gasolina utilizada


def rendimiento (distancia, litros):  #kilometros por litro
    rendimiento = distancia/litros
    return rendimiento

def rendimiento2(distancia, galones):  #millas por galones
    distancia = distancia/1.6093  #conversion de kilometros a millas
    volumen = galones*0.264    #conversion de litros a galones
    rendimiento2 = distancia/volumen
    return rendimiento2


# Funcion Principal
def main():

    # Datos dados por el usuario
    distancia=int(input("Teclea el numero de km recorridos: "))
    volumen=int(input("Teclea el numero de litros de gasolina usados: "))

    # Llamar y calcular datos
    primerDato=rendimiento(distancia, volumen)
    segundoDato=rendimiento2(distancia, volumen)

    #Imprimir resultados
    print(
    "Si recorres", distancia,"kms con", volumen,"""litros de gasolina el rendimiento es:
    %.2f"""% (primerDato),"km/l" """
    %.2f"""%(segundoDato),"mi/gal")

    # Dato dado
    tercerDato = int(input("¿Cuántos kilómetros vas a recorrer? "))

    #Llamar funcion
    gasolina= tercerDato/primerDato

    #Imprimir resultado
    print("Para recorrer",tercerDato,"Km. Necesitas %.2f" % (gasolina),"litros de gasolina")#se imprime la gasolina que se necesitara.

main()



