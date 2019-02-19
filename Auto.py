#FRANCISCO JAVIER GONZALEZ MOLINA A01748636
#PROGRAMA QUE CALCULARA EL RENDIMIENTO DEL VEHICULO

# Esta funcion calculara el rendimiento del vehiculo y regresara los km utilizados por litro
def calcularRendimientoKMLts (kmRecorrido,ltsUsados):
    kmlts=kmRecorrido/ltsUsados
    return kmlts

# Esta funcion calculara los litros necesarios que necesitara el vehiculo
# para recorrer una distancia dada, regresara el valor de litrso necesarios.
def calcularLtsnecesarios (rendimiento,kmaRecorrer):
    ltsnecesarios= kmaRecorrer/rendimiento
    return ltsnecesarios

# Esta funcion convertira el rendimiento del coche de km/l a mi/gal
#y regresara el valor de las mi/gal
def calcularDistanciaKMaMI (kmRecorrido,ltsUsados):
    miGal=(kmRecorrido/1.6093)/(ltsUsados*0.265)
    return miGal

# esta funcion realizara todas las operaciones, leera valores e imprimira los
#datos
def main():
    kmRecorrido=int(input("Teclea el numero de km recorridos: "))
    ltsUsados=int (input("Teclea el numero de litros de gasolina usados: "))
    rendimiento=calcularRendimientoKMLts(kmRecorrido,ltsUsados)
    rendiMiGal=calcularDistanciaKMaMI(kmRecorrido,ltsUsados)
    print("""
        Si recorres %d con %d litros de gasolina, el rendimiento es: 
        %.2f km/l
        %.2f mi/gal
        """% (kmRecorrido, ltsUsados, rendimiento, rendiMiGal))
    kmaRecorrer=int (input("¿Cuantos kilometros vas a recorrer? "))
    ltsnecesarios=calcularLtsnecesarios(rendimiento,kmaRecorrer)
    print ("""
    Para recorrer %d km, necesitas %.2f litros de gasolina"""%(kmaRecorrer,ltsnecesarios))

#llama la funcion "main()"
main ()