#Escribe la longitud de la base mayor: 2
#Escribe la longitud de la base menor: 1
#Escribe la altura: 1
#Área: 1.50
#Perímetro: 5.24

def calcularArea(baseM, basem, altura):
    area = ((baseM+basem)/2)*altura
    return area

def calcularHipotenusa(basem, baseM, altura):
    n = baseM-basem
    h = ((altura**2)+(n**2))**0.5
    return h

def calcularPerimetro(h, basem, baseM):
    P = h + h + basem + baseM
    return P

def main():
    baseM = int(input("Introduce la longitud de la base mayor:"))
    basem = int(input("Introduce la longitud de la base menor:"))
    altura = int(input("Introduce la altura:"))
    area = calcularArea(baseM, basem, altura)
    h = calcularHipotenusa(basem, baseM, altura)
    perimetro = calcularPerimetro(h, basem, baseM)
    print("Área igual a:", area)
    print("Perímetro igual a:", perimetro)

main()