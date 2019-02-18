#Rafael Romero Bello
#A01747730
#Este programa:Escribe un programa que lea la base mayor, la base menor y la altura de un trapecio isósceles y que imprima el area y su perimetro
def calcularArea(mayor, menor, altura):
    Area=((mayor+menor)*altura)/2
    return Area
def calcularPerimetro(mayor, menor,altura):
    perimetro=(mayor+menor)+(2*altura)
    return perimetro
def main():
    B=float(input("inserta la base mayor:"))
    b=float(input("inserta la base menor:"))
    h=float(input("inserta la altura:"))
    AT=calcularArea(B,b,h)
    PT=calcularPerimetro(B,b,h)
    print("tu area es:%.2f"%(AT))
    print("tu perimetro es:%.2f"%(PT))


main()



