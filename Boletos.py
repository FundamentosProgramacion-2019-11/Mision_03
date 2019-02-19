#Mariana Coria Rodríguez A01374765
#Compra de boletos

def calcularPago(A, B , C): #Se marcan las tres variables)
    total = (A*3250) + (B*1730) + (C*850)
    return total #Se regresa el valor

def main():
    A = int(input("Número de boletos en zona A: "))
    B = int(input("Número de boletos en zona B: "))
    C = int(input("Número de boletos en zona C: "))
    calcularPago(A, B, C) #marcar que esta variable existe en main
    print("El costo total de los boletos es: $ %.2f " %calcularPago(A , B, C))


main()