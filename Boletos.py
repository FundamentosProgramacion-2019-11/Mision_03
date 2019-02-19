#Martha Margarita Dorantes Cordero
#calcular el pago total



def calcularPago(boletosA, boletosB, boletosC) :
	#Función que realiza la operación requerida para calcular el pago total por los boletos comprados.
	totalPago = (boletosA * 3250) + (boletosB * 1730) + (boletosC * 850)
	return totalPago

def main() :
	#Función principal que pide al usuario los datos necesarios para calcular el pago total por
	#los boletos mediante la llamada a función calcularPago(). Al pasar como parámetros los datos recibidos,
	#se imprime en pantalla el resultado con el pago total de los boletos.
	numeroBoletosA = int(input("Número de boletos en zona A: "))
	numeroBoletosB = int(input("Número de boletos en zona B: "))
	numeroBoletosC = int(input("Número de boletos en zona C: "))
	print('El costo total es: $%.2f'%(calcularPago(numeroBoletosA, numeroBoletosB, numeroBoletosC)))

main()