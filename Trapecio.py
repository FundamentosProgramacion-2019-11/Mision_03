#Autor: Victor Manuel Ceron Navarrete
#Descripcion: Este programa te indica el area y perimetro de un trapecio isoseles

def sacarArea(baseMayor, baseMenor, altura):
    area = ((baseMayor + baseMenor)/2) * altura
    return area
# De aqui sacamos el area


def Hipotenusa(baseMayor, baseMenor, altura):
    base = (baseMayor - baseMenor)/2
    hipotenusa = (base**2 + altura**2)**0.5
    return hipotenusa
# De aqui sacamos la hipotenusa



def Perimetro(baseMayor, baseMenor, hipotenusa):
    perimetro = baseMayor + baseMenor + hipotenusa*2
    return perimetro
# De aqui sacamos el perimetro


def main():
    variableMayor = int(input("cuanto mide la base mayor: "))
    variableMenor = int(input("cuanto mide la base menor: "))
    variableAltura = int(input("cuanto mide la altura: "))
    variableArea = sacarArea(variableMayor, variableMenor, variableAltura)
    variableHipotenusa = Hipotenusa(variableMayor, variableMenor, variableAltura)
    variablePerimetro = Perimetro(variableMayor, variableMenor, variableHipotenusa)
    print("Area: %.2f" %variableArea)
    print("Perimetro: %.2f"%variablePerimetro)

main()