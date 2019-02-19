#Autor: Michel Antoine Dionne Gutierrez A0174863, Grupo: 03
#Este programa calculara area y perimetro de un trapecio isoceles

#Esta funcion calcula el area del trapecio
def calcularArea(baseMayor,baseMenor,altura):
    area = ((baseMayor+baseMenor)*altura)/2
    return area

#Esta funcion calculara el perimetro del trapecio
#Prof use la formula del perimetro del siguiente link, pero no me da exactamente el perimetro
#https://www.bing.com/images/search?view=detailV2&id=248F46B7B040C3DA7914E06F079A867F39962864&thid=OIP.Q1YAfk6hgBvcav0FuwgJIwHaFj&mediaurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FBvxuuB5NV5k%2Fhqdefault.jpg&exph=360&expw=480&q=formula+calcular+perimetro+de+un+trapecio+isosceles&selectedindex=2&ajaxhist=0&vt=0&eim=1,2,6
def calcularPerimetro(baseMayor,baseMenor,altura):
    perimetro = 2*((((baseMayor-baseMenor)**2)+(altura**2))**0.5)+baseMayor+baseMenor
    return perimetro

def main():
    baseMayor = int(input("Escribe la longitud de la base mayor"))
    baseMenor = int(input("Escribe la longitud de la base menor"))
    altura = int(input("Escribe la alutra"))
    areaTrapecio = calcularArea(baseMayor,baseMenor,altura)
    perimetroTrapecio = calcularPerimetro(baseMayor,baseMenor,altura)
    print("El area es de %.2f"%areaTrapecio,"y el perimetro es de %.2f"%perimetroTrapecio)

main()