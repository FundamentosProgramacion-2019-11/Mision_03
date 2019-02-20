# Karimn Daniel Hernández Castorena
# Programa que ayuda a un usuario a conocer el rendimiento de la gasolina en km/l y mi/gal

def calcularRendimientokm(kmr, l):
    renk = kmr / l
    return renk


def calcularRendimientomi(kmr, l):
    mi = kmr / 1.6093
    gal = l * .264
    renm = mi / gal
    return renm


def calcularkm(km, renk):
    lnec = km / renk
    return lnec


def main():
    kmr = int(input("Teclea el número de km recorridos "))
    l = int(input("Teclea el número de litros de gasolina usados "))
    renk = calcularRendimientokm(kmr, l)
    renm = calcularRendimientomi(kmr, l)
    print("Si recorres ", kmr, " kms con ", l, "litros de gasolina, el rendimiento es: ")
    print("%.2f" % renk, " km/l")
    print("%.2f" % renm, " mi/gal")
    km = int(input("¿Cuántos kilómetros va a recorrer? "))
    lnec = calcularkm(km, renk)
    print("Para recorrer ", km, " km. necesitas %.2f" % lnec, " litros de gasolina")


main()