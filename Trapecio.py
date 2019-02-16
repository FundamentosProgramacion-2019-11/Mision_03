# Guillermo De Anda Casas , A01375892
# Programa que calcula el area y el perimetro de un trapecio.

def calcularPerimetro(B,b,h):
    r = ((B-b)/2)
    P = ((B + b) + (((r**2)+(h**2))**0.5)*2)
    return P

def calcularArea(B,b,h):
    A = ((B + b) / 2) * h
    return A

def main():
    B = int(input("Valor de la base mayor: "))
    b = int(input("Valor de la base menor: "))
    h = int(input("Valor de la altura del trapecio: "))
    calcularArea(B,b,h)
    calcularPerimetro(B,b,h)
    print("Área: %.2f "%calcularArea(B,b,h))
    print("Perímetro: %.2f "%calcularPerimetro(B,b,h))

main()