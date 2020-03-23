#Autor: Brandon Julien Celaya Torres - A01745762
#Descripición: Calcula el área y perímetro de un trapecio con las bases y la altura.

def area (baseMayor, baseMenor, altura):
    area = ((baseMayor+baseMenor)/2) * altura
    
    return area

def perimetro (baseMayor, baseMenor, altura):
    
    segmento = (baseMayor-baseMenor)/2
    hipotenusa = (segmento**2 + altura**2)**0.5
    
    perimetro = 2*hipotenusa + baseMayor + baseMenor
    
    return perimetro

def main ():
    
    bM = int(input("Introduce la base mayor: "))
    b = int(input("Introduce la base menor: "))
    h = int(input("Introduce la altura: "))
    
    a = area (bM, b, h)
    p = perimetro (bM, b, h)
    
    print ("""
            Base mayor: %d
            Base menor: %d
            Altura: %d
            Área: %.2f
            Perímetro: %.2f """ % (bM, b, h, a, p))
    
    
main ()

    