#Autor: Cecilia Daniela Olivares Hernández, a01745727
#Descripción: Calcula el precio total a pagar de los boletos comprados para un concierto.

#Esta funcion calcula el rendimiento del automovil en km/litros
def calcularRendimientoKm(km, litros):
    rendimientoKm = km / litros
    return rendimientoKm

#Esta funcion calcula el rendimiento del automovil en millas/galon
def calcularRendimientoMi(km, litros):
    rendimientoMi = (km / 1.6093) / (litros * 0.264)
    return rendimientoMi

#Esta funcion calcula los km que recorrera el auto
def calcularKmARecorrer(km, litros, kmARecorrer):
    l = kmARecorrer * 0.0358
    return l

#Funcion principal que resuelve el problema
def main():
    km = int(input("Teclea el número de Km recorridos: "))
    litros = int(input("Teclea el número de litros de gasolina usados: "))
    rendimientoKm = calcularRendimientoKm(km, litros)
    rendimientoMi = calcularRendimientoMi(km, litros)
    print(""" \x1b[1;30m 
Si recorres""",(km),"""kms con""", (litros), """litros de gasolina, el rendimiento es:
%.2f""" % (rendimientoKm), """km/l
%.2f""" % (rendimientoMi), """mi/gal
""")
    kmARecorrer = int(input("\x1b[0;m¿Cuántos kilómetros vas a recorrer? "))
    l = calcularKmARecorrer(km, litros, kmARecorrer)
    print(""" \x1b[1;30m 
Para recorrer""", (kmARecorrer),"""km. necesitas %.2f""" % (l), """litros de gasolina""")

main()