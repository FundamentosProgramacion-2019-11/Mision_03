# Autor: Jose Luis Mata Lomeli
# Objetivo: Escribir un programa que pregunte al usuario cuantos boletos quiere comprar por zona y que imprima el total a pagar

#Costo de los Asientos por zona: zona A= $3250, zona B= $1730, zona C= $850

# Calcular el total a pagar
def calcularPago(boletosA, boletosB, boletosC):
    totalPago= (boletosA*3250)+ (boletosB*1730) + (boletosC*850) # Regla de 3
    return totalPago  #Regresar resultado


# Funcion principal
def main():
    #Preguntar la cantidad de boletos que quiere por zona
    numBoletosA = int(input("Numero de boletos clase A: "))
    numBoletosB = int(input("Numero de boletos clase B: "))
    numBoletosC = int(input("Numero de boletos clase C: "))

    # Llamar la funcion para calcular total(con los parametros dados)
    costoTotal = calcularPago(numBoletosA,numBoletosB,numBoletosC)

    print("El costo total es de: $%.2f" %(costoTotal))  # Imprimir el resultado

main()