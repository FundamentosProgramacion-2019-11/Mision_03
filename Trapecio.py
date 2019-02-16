#Autor: María Fernanda García Gastélum A01376181
#Calcular el área y perímetro de un trapecio


def calcularArea(baseMayor, baseMenor, altura):
    area= ((baseMayor+baseMenor)/2)* altura
    return area

def calcularPerimetro(baseMayor, baseMenor, altura):
    hipotenusa= ((((baseMayor-baseMenor)/2)*((baseMayor-baseMenor)/2))+(altura*altura))**0.5
    perimetro= baseMenor+ baseMayor + hipotenusa + hipotenusa
    return perimetro

def main():
   baseMayor= float(input("Escribe la longitud de la base mayor: "))
   baseMenor = float(input("Escribe la longitud de la base menor: "))
   altura= float(input("Escribe la altura: "))
   calcularArea(baseMayor, baseMenor, altura)
   calcularPerimetro(baseMayor, baseMenor, altura)
   print("Área: %0.2f"% (calcularArea(baseMayor, baseMenor, altura)))
   print("Perímetro: %0.2f"% (calcularPerimetro(baseMayor, baseMenor, altura)))

main()