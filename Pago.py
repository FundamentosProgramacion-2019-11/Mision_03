#El pago semanal de un trabajador se calcula multiplicando las horas normales trabajadas por la cantidad que se paga por
#hora. Las horas extras se pagan 65% más que las normales.
#Escribe un programa que lea las horas normales, las horas extras y el pago por hora de un trabajador. Calcula e imprime
#los datos de pago semanal. Formatea correctamente las cantidades.
#Usa una función para calcular el pago normal y otra función para calcular el pago extra

def calcularPagoSemanal(horasnormales, pagoxhora):
    sueldo = horasnormales*pagoxhora
    return sueldo

def calcularHorasExtra(pagoxhora, horasextra):
    bonus = ((pagoxhora*0.65)+pagoxhora)*horasextra
    return bonus

def calcularSueldo(semana, bonus):
    T = semana+bonus
    return T

def main():
    pagoxhora = float(input("Introduce el pago por hora:"))
    horasnormales = int(input("Introduce las horas normales trabajadas:"))
    horasextra = int(input("Introduce las horas extra trabajadas:"))
    semana = calcularPagoSemanal(horasnormales, pagoxhora)
    bonus = calcularHorasExtra(pagoxhora, horasextra)
    total = calcularSueldo(semana, bonus)
    print("Pago Semanal:", semana)
    print("Pago Extra:", bonus)
    print("Pago Total:", total)

main()