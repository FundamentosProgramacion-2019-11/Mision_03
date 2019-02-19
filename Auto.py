#Autor: Aline Paulette Villegas Berdejo, A01375818
#Calcula el rendimiento de un automovil y cuanto mas puede recorrer de acuerdo al mismo.

#Calcula en rendimiento en km/l
def calcularrendimientoKm(kmrecorridos, lusados):
    ren=kmrecorridos/lusados
    return ren

#Calcula el rendimiento de km/l a mi/gal
def calcularconversionMi(kmrecorridos, lusados):
    gal= lusados*0.264
    mi= kmrecorridos*0.6214
    migal= mi/gal
    return migal

#Calcula cuantos litros de gasolina se necesitan para recorrer cierta distancia
def calcularcuantoslitros(kmrecorridos, lusados, cuantoskm):
    cl= (cuantoskm*lusados)/kmrecorridos
    return cl

#Indica las funciones que se van a correr al llamar a la funición "main()"  (Lee datos, imprime datos)
def main():
    kmrecorridos= int(input("Teclea el número de km recorridos: "))
    lusados= int(input("Teclea el número de litros de gasolina usados: "))
    ckm= calcularrendimientoKm(kmrecorridos, lusados)
    cmi= calcularconversionMi(kmrecorridos, lusados)
    print("\nSi recorres ", kmrecorridos, "kms con ", lusados, "litros de gasolina, el rendimiento es:\n%.2f" % ckm, "km/l")
    print("%.2f" % cmi, "mi/gal\n")
    cuantoskm=int(input("¿Cuántos kilómetros vas a recorrer? "))
    cl= calcularcuantoslitros(kmrecorridos, lusados, cuantoskm)
    print("\nPara recorrer", cuantoskm, "km. necesitas %.2f" % cl, "litros de gasolina")

main()