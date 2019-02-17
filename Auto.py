#Autor: Daniela Estrella Tovar
# Descripción: Dados lo kilómetros y la cantidad de gasolina consumida, imprimir el rendimiento del coche en km/litro y millas/galón, además de
#preguntar la cantidad de kilómetros que se van a recorrer para imprimir la cantidad de gasolina que se utilizará


def calcularRKm(kmRecorridos, gasConsum):
    rKm= kmRecorridos/gasConsum
    return rKm
def calcularRMilla(kmRecorridos, gasConsum):
    convM= kmRecorridos/1.6093
    convL= gasConsum*0.264
    rMill= convM/convL
    return rMill

def imprimirRKmYMilla(kmRecorridos, gasConsum):
    rKm= calcularRKm(kmRecorridos, gasConsum)
    rMill= calcularRMilla(kmRecorridos,gasConsum)
    print("""
Si recorres""",(kmRecorridos),"""km con""", (gasConsum),"""litros de gasolina, el rendimiento es: 
%.2f""" % (rKm),"""Km/l 
%.2f"""%(rMill),"""Mi/gal""")

def calcularkmARecorrer(kmARecorrer,kmRecorridos,gasConsum):
    kmAR= kmARecorrer/(kmRecorridos/gasConsum)
    return kmAR

def imprimirkmARecorrer(kmARecorrer,kmRecorridos, gasConsum):
    kmAR= calcularkmARecorrer(kmARecorrer,kmRecorridos,gasConsum)
    print("""
Para recorrer""",(kmARecorrer),"""km. necesitas  %.2f""" %(kmAR),"""litros de gasolina""")

def main():
    kmRecorridos= int(input("Teclea el número de km/h recorridos: "))
    gasConsum= int(input("Teclea el número de litros de gasolina usados: "))
    imprimirRKmYMilla(kmRecorridos, gasConsum)
    kmARecorrer = int(input("""
¿Cuántos kilómetros va a recorrer? """))
    imprimirkmARecorrer(kmARecorrer,kmRecorridos, gasConsum)

main()