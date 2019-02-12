#Autor: Eric Jardón Chao
#Datos de un trapecio. Provee el área y perímetro de un trapecio isóceles dadas su base mayor, base menor y altura.

#Escogí realizar la tercera función main solamente por convención y dar mayor orden.

def imprimirArea(B,b,h): #Esta función calcula e imprime el área dados los tres parámetros, base mayor, menor y altura
    Area=(B+b)*h/2
    print("El área del trapecio es %.2f unidades cuadradas" %(Area))
def imprimirPerim(B,b,h): #Esta función calcula e imprime el perímetro dados los tres parámetros, base mayor, menor y altura. Para lograrlo, calcula la longitud de la diagonal del trapecio, denominada hipotenusa.
    hipotenusa= (((B-b)/2)**2+(h**2))**(1/2)
    Perim=B+b+2*hipotenusa
    print("El perímetro del trapecio es %.2f unidades." %(Perim))

def main(): #Esta función recibe datos de entrada y corre funciones que imprimen los datos de salida.
    B=float(input("Teclea la magnitud de la base Mayor:"))
    b=float(input("Teclea la magnitud de la base menor:"))
    h=float(input("Teclea la altura del trapecio:"))
    imprimirArea(B,b,h)
    imprimirPerim(B,b,h)

main()
#Fin del programa