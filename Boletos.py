# Autor: Victor Manuel Ceron Navarrete
# Descripcion: Este programa ayuda a calcular el total del costo de numeros de boletos

def calcularBoletos(variable1, variable2, variable3):  #Descripcion de esta funcion
    pago = (variable1*3250) + (variable2*1730) + (variable3*850)
    return pago

def main():
    variable1 = int(input("Cuantos boletos en zona A: "))
    variable2 = int(input("Cuantos boletos en zona B: "))
    variable3 = int(input("Cuantos boletos en zona C: "))
    calcularPago(variable1, variable2, variable3)
    print("El total a pagar es: $ %.2f"%calcularBoletos(variable1, variable2, variable3))

main()