#Karimn Daniel Hernández Castorena
#Programa que imprima el area y el perimetro de un trapecio.

def calcularArea(bmayor, bmenor, alt):
    area=((bmayor+bmenor)/2) * (alt)
    print ("Area= %.2f " % area)

def calcularPerimetro(bmayor,bmenor,alt):
    hip= ((((bmenor-bmayor)/2)**2) + (alt**2))**.5
    peri= bmayor + bmenor + (hip*2)
    print("Perímetro= %.2f " % peri)

def main():
    bmayor = int(input("Escribe la longitud de la base mayor: "))
    bmenor = int(input("Escribe la longitud de la base menor "))
    alt = int(input("Escribe la altura "))
    calcularArea(bmayor, bmenor, alt)
    calcularPerimetro(bmayor, bmenor, alt)
main()