#Autor: Eric Jardón Chao
#Rendimiento de un Auto. Dados los kilómetros y litros de gasolina utilizados, se calcula el rendimiento en km/l y mi/gal. Después, dada una distancia a recorrer, calcula el número de litros necesarios con base en el rendimiento del auto.

def main(): #Esta función resuelve dos problemas en secuencia. Primero recibe los datos de entrada para imprimir los dos rendimientos calculados por otras funciones. Después recibe la distancia a recorrer para imprimir la gasolina necesaria, calculada por otra función.
    km=int(input("Teclea el número de kilómetros enteros recorridos:"))
    litros=int(input("Teclea el número de litros de gasolina utilizados:"))
    r1=calcularRendimiento(km,litros)
    r2=calcularRendimiento2(km,litros)
    print("Si recorres",km,"kms con",litros,"litros de gasolina, el rendimiento de tu auto es \n %.2f km/l"%(r1),"\n %.2f millas/galón" %(r2))
    kmfuturos=int(input("¿Cuántos kilómetros enteros planeas recorrer?"))
    imprimirGas(kmfuturos,r1) #Aquí esta función utiliza como argumentos un valor ingresado por el usuario y otro calculado por una función anterior (r1). Directamente imprime el valor de salida.

def calcularRendimiento(km,l): #Esta función calcula el rendimiento en km/l dados dos parámetros: kilómetros y litros.
    r=km/l
    return r
def calcularRendimiento2(km,l): #Esta función calcula el rendimiento en mi/gal dados los klómetros y litros, los cuales transforma a millas y galones respectivamente.
    r=(km/1.6093)/(l*0.264)
    return r
def imprimirGas(kf,r): #Esta función calcula e imprime la gasolina necesaria para recorrer una distancia ingresada por el usuario. Los parámetros kf y r son, respectivamente, la distancia ingresada y el rendimiento en km/l ya calculado anteriormente.
    gas=kf/r
    print("Para recorrer",kf,"kilómetros necesitas %.2f" %(gas),"litros de gasolina.")

main()
#Fin del programa