#José Isidro Sánchez Vázquez
#Calculador de area y perimetro
import math
def calculadorDeArea(baseMayor,baseMenor,altura):
    A=((baseMayor + baseMenor)/2)*altura
    return A
def calculadorDelPerimetro(baseMenor,baseMayor,altura,hipotenusaTriangulo):
    p=baseMenor+baseMayor+(hipotenusaTriangulo)*2
    return p
def calculadorDeHipotenusa(baseMayor,baseMenor,altura):
    base=(baseMayor-baseMenor)/2
    h =math.sqrt ((base**2)+(altura**2))
    return h
def main():
    baseMayor = int(input("Escribe la longitud de la base mayor: "))
    baseMenor = int(input("Escribe la longitud de la base menor: "))
    altura = int(input("Escribe la altura: "))
    area = calculadorDeArea(baseMayor,baseMenor,altura)
    hipotenusaTriangulo = calculadorDeHipotenusa(baseMayor,baseMenor,altura)
    perimetro=calculadorDelPerimetro(baseMenor,baseMayor,altura,hipotenusaTriangulo)
    print("Area: %.2f"%(area))
    print("Perimetro: %.2f"%(perimetro))

main()