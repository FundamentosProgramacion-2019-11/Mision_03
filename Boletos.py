# Autor: Mario Hernández Cárdenas
# Calcular el total de precio en unos boletos de un concierto

def calcularPago(costoBoletosA, costoBoletosB, costoBoletosC):  #Lee los boletos y multiplica por su costo respectivamente, y suma el total.
    total = (costoBoletosA*3250) + (costoBoletosB*1730) + (costoBoletosC*850)
    return total

def main():
    boletosA = int(input("Número de boletos en zona A: "))
    boletosB = int(input("Número de boletos en zona B: "))
    boletosC = int(input("Número de boletos en zona C: "))
    calcularPago(boletosA, boletosB, boletosC)
    print("El costo total es: $ %.2f"%calcularPago(boletosA, boletosB, boletosC))

main()