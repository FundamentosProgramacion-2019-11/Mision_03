# Autor: Luis Renteria
# Calcular rendimiento del auto

def calcularRendimientoenKmL(kilometros, litros):
    rend=(kilometros/litros)
    miGal=(kilometros*0.6213)/(litros*0.264)
    print("El rendimiento de tu carro en kilometros por litro es:",rend)
    print("El rendimiento de tu carro en millas por galon es:",miGal)
    return rend

def calcularLitros(rend):
    kilometros=int(input("Cuantos kilomentros recorriste"))
    litros=(kilometros/rend)
    return litros

def main ():
    kilometros=int(input("Introduce el numero de kilometros recorridos:"))
    litros=int(input("introduce la cantidad de gazolina utilizada:"))
    rend = calcularRendimientoenKmL(kilometros, litros)
    litros2 = calcularLitros(rend)
    print ("La cantidad de litros ocupados es:",litros2)

main()



