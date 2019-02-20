#Karimn Daniel Hernández Castorena
#Programa que pregunte al usuario cuantos boletos quiere comprar para cada zona y que imprima un total a pagar.

def calcularPago(ba,bb,bc):
    totalpago= (ba*3250)+(bb*1730)+(bc*850)
    return totalpago

def main():
    ba= int(input("Número de boletos de la zona A: "))
    bb= int(input("Número de boletos de la zona B: "))
    bc= int(input("Número de boletos de la zona C: "))
    totalpago= calcularPago(ba,bb,bc)
    print("El costo total es:$ %.2f " % totalpago)
main()
