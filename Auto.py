#Martha Margarita Dorantes Cordero
#calcula rendimiento, kilometros recorrridos y litros usados.



def calcularRendimientoKM(kmRecorridos, litrosUsados) :
	#Función que realiza la operación requerida para calcular el rendimiento correspondiente por los kilómetros recorridos con el número de listros gastados.
	rendimientoKM = kmRecorridos / litrosUsados
	return rendimientoKM

def calcularRendimientoMI(kmRecorridos, litrosUsados) :
	#Función que realiza la operación requerida para calcular el rendimiento correspondiente por las millas recorridas con el número de galones gastados.
	rendimientoMI = (kmRecorridos / 1.6093) / (litrosUsados * 0.264)
	return rendimientoMI

def main() :
	#Función principal que pide al usuario los datos necesarios para calcular el rendimiento de su auto y hace
	#una estimación de los litros necesarios para recorrer cierta cantidad de kilómetros, a partir del rendimiento previamente calculado.
	#Se imprime en pantalla el resultado con el rendimiento en km/l y en mi/gal, así como los litros estimados que se necesitan para recorrer la cantidad de kms ingresados.
	kms = int(input("Teclea el número de km recorridos: "))
	litros = int(input("Teclea el número de litros de gasolina usados: "))
	print('\nSi recorres %d kms con %d litros de gasolina, el rendimiento es:'%(kms,litros),
		  '\n%.2f km/l'%(calcularRendimientoKM(kms, litros)),
		  '\n%.2f mi/gal'%(calcularRendimientoMI(kms, litros)))
	kmsRecorrer = int(input("\n¿Cuántos kilómetros vas a recorrer? "))
	print('\nPara recorrer %d km. necesitas %.2f litros de gasolina'%(kmsRecorrer, kmsRecorrer / calcularRendimientoKM(kms, litros)))

main()