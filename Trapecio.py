#Martha Margarita Dorantes Cordero
#Calcular el área de un trapecio


import math

def calcularArea(baseMayor, baseMenor, altura) :
	#Función que realiza la operación requerida para calcular el área de un trapecio.
	area = ((baseMayor + baseMenor) * altura) / 2
	return area

def calcularPerimetro(baseMayor, baseMenor, altura) :
	#Función que realiza la operación requerida para calcular el perímetro de un trapecio.
	perimetro = math.sqrt(((baseMayor - baseMenor) / 2)**2 + altura**2) * 2 + (baseMayor + baseMenor)
	return perimetro

def main() :
	#Función principal que pide al usuario los datos necesarios para calcular el área y el perímetro de
	#un trapecio, cuyas medidas son ingresadas por el usuario y pasadas a las funciones correspondientes.
	#Se imprime en pantalla el resultado con el área y perímetro del trapecio con las medidas ingresadas.
	lB = float(input("Escribe la longitud de la base mayor: "))
	lb = float(input("Escribe la longitud de la base menor: "))
	h = float(input("Escribe la altura: "))
	print('Área: %.2f'%(calcularArea(lB, lb, h)))
	print('Perímetro: %.2f'%(calcularPerimetro(lB, lb, h)))

main()