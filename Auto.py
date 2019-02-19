#Autor: Victor Manuel Ceron Navarrete
#Decripcion: Calcula el rendimiento del auto y gasolina necesaria para completar viaje

def rendimientoK(variableKilometros, variableLitros):
    rendimientoKilometros = variableKilometros/variableLitros
    return rendimientoKilometros



def rendimientoM(variableKilometros, variableLitros):
    variableMillas = variableKilometros / 1.6093
    variableGalones = variableLitros * 0.264
    rendimientoMillas = variableMillas/variableGalones
    return rendimientoMillas


def obtenerRendimiento(kilometrosFuturos, kilometros):
    rendimientoKmXRecorrer = kilometrosFuturos / kilometros
    return rendimientoKmXRecorrer




def main():
    variableKilometros = int(input("km viajados: "))
    variableLitros = int(input("litros de gasolina gastados: "))
    kilometros = rendimientoK(variableKilometros, variableLitros)
    millas = rendimientoM(variableKilometros, variableLitros)
    print("Si viajas", variableKilometros, "kms con", variableLitros, "L de gasolina, el rendimiento  de tu auto es de:")
    print("%.2f"%kilometros, "km/l")
    print("%.2f"%millas, "mi/gal")
    print(" ")
    kilometrosProximos = int(input("kilometros por recorrer: "))
    rendimientoKmXRecorrer = obtenerRendimiento(kilometrosProximos, kilometros)
    print("Para recorrer", kilometrosProximos,'km. necesitas %.2f'%rendimientoKmXRecorrer, "litros de gasolina")

main()