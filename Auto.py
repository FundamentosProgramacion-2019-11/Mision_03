#Mariana Coria Rodriguez A01374765
#Rendimiento de un coche

def km (recorridos, lit):
    rendimientoKM = recorridos/lit
    return rendimientoKM


def mill (recorridos, lit):
    millas = recorridos / 1.6093
    galones = lit/ 0.264
    rendimientoMILL = millas/galones
    return rendimientoMILL

def rendimiento (aRecorrer, kms):
    recorrerRendimiento = aRecorrer /kms
    return recorrerRendimiento


def main():
    recorridos = int(input("Teclea el número de km recorridos: "))
    lit = int(input("Teclea el número de litros de gasolina usados: "))
    print("Si recorres",recorridos, "kms con", lit, "litros de gasolina, el rendimiento es:",rendimiento)
    km = int(input("Cuántos kilometros vas a recorrer? "))
    print("Para recorrer", km, "necesitas",lit,"litros de gasolina")


main()