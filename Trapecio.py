#Mariana Coria Rodríguez A01374765
# Área y perimetro de un trapecio


def area(bm, bn, a):
    areatotal = ((bm+bn)/2)*a
    return areatotal

def hipotenusa(bm, bn, a):
    base = (bm - bn)/2
    hipo = (base**2 + a**2)**0.5
    return hipo


def perimetro(bm, bn, hipo):
    perimetroTotal = bm + bn + hipo*2
    return perimetroTotal

def main():
    bm = int(input("Escribe la longitud de la base mayor: "))
    bn = int(input("Escribe la longitud de la base menor: "))
    a = int(input("Escribe la altura: "))
    area (bm, bn, a)
    perimetro (bm, bn, a)
    hipotenusa (bm, bn, a)
    print("Área: %.2f "%area(bm, bn, a))
    print("Perímetro: %.2f "%perimetro(bm, bn, a))


main()
