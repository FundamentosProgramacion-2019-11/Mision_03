#Martha Margarita Dorantes Cordero
#calcula pagos



def calcularPagoNormal(horasNormales, pagoHora) :
	#Función que realiza la operación requerida para calcular el pago correspondiente por las horas normales trabajadas.
	pagoNormal = horasNormales * pagoHora
	return pagoNormal

def calcularPagoExtra(horasExtra, pagoHora) :
	#Función que realiza la operación requerida para calcular el pago correspondiente por las horas extras trabajadas.
	pagoExtra = horasExtra * (pagoHora * 1.65)
	return pagoExtra

def main() :
	#Función principal que pide al usuario los datos necesarios para calcular el pago normal y el pago extra
	#por las horas trabajadas que son ingresadas por el usuario y pasadas a las funciones correspondientes.
	#Se imprime en pantalla el resultado con el pago correspondiente a las horas normales, horas extras y el pago total.
	hn = int(input("Teclea las horas normales trabajadas: "))
	he = int(input("Teclea las horas extras trabajadas: "))
	ph = float(input("Teclea el pago por hora: "))
	pN = calcularPagoNormal(hn, ph)
	pE = calcularPagoExtra(he, ph)
	print('Pago normal: $%.2f'%(pN))
	print('Pago extra: $%.2f'%(pE))
	print('-----------------------')
	print('Pago total: $%.2f'%(pN + pE))

main()	