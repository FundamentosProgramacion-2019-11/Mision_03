# Guillermo De Anda Casas , A01375892
# Código que resuelve el primer ejercicio de la Misión 3

def imprimirTotal(A, B, C):
    T = calcularTotal(A, B, C)
    print("El costo total es de: $%.2f "%T)

def calcularTotal(A, B, C):
    a = A * 3250
    b = B * 1730
    c = C * 850
    T = a + b + c
    return T

def main():
    A = int(input("Número de boletos en zona A: "))
    B = int(input("Número de boletos en zona B: "))
    C = int(input("Número de boletos en zona C: "))
    calcularTotal(A, B, C)
    imprimirTotal(A, B, C)


main()