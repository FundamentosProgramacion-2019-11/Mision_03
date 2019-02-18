#Autor: David Yair Fernández Salas
# Este programa te imprime el área y el perímetro de un trapecio.


"""La función que usamos en este problema nos sirve para recibir los datos(parametros) de la base menor,
    la base mayor y la altura, y nos va a regresar el valor de la area """
def CalcularArea(bmenor, bmayor,h):
    area =((bmayor+bmenor)*h)/2
    return area

"En este caso usamos tambien otra función que se llamará CalcularPerimetro en donde asignamos los parametros"
"de base menor, de base mayor y de altura, y nos devuelven el valor del perimetro  "
def CalcularPerimetro(bmenor, bmayor,h):
    basef= ( bmayor-bmenor)/2
    hipotenusa = ((h**2) +(basef **2))**0.5
    perimetro= bmayor + bmenor +(2*hipotenusa)
    return perimetro

"""La función main le pide al usuario introducir los datos de la figura, base mayor, base menor, altura
Registra estos datos y se los envia al area y el perimetro, para que imprima los datos deseados """


def main():
    bMayor = float(input("Escribe la longitud de la base mayor: "))
    bMenor = float(input("Escribe la longitud de la base menor: "))
    h = float(input("Escribe la altura: "))
    area = CalcularArea(bMayor, bMenor, h)
    perimetro = CalcularPerimetro(bMayor, bMenor, h)
    print("Área: %.2f " % (area))
    print("Perímetro: %.2f"%(perimetro))
main()