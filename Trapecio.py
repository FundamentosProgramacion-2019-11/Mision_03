# Autor: Alan Giovanni Rodriguez Camacho A01748185
# Descripcion: lee la base mayor, la base menor y la altura de un trapecio isósceles y te imprime el area y el perimetro

def calcularArea(B,b,h):#calcula el area del trapecio.
    area=((B+b)/2)*h
    return area


def calcularPerimetro(B,b,h):#Calcula el perimetro del trapecio
    lado=((((B-b)/2)**2)+(h**2))**.5
    perimetro=B+b+(lado*2)
    return perimetro

def main():
    B=int(input("Indica la base mayor de tu trapecio: "))
    b=int(input("Indica la base menor de tu trapecio: "))
    h=int(input("Indica la altura de tu trapecio: "))
    area=calcularArea(B, b, h)
    perimetro=calcularPerimetro(B, b, h)
    print("Area: %.2f"% area)
    print("Perimetro: %.2f"% perimetro)

main()