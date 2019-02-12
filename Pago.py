#Eric Jardón Chao
#Cálculo del pago de un trabajador. Recibe el número de horas normales y extras trabajadas, así como la tarifa pagada por hora. Devuelve el pago normal, extra y total.

def main(): #Esta función recibe los datos de entrada, declara los pagos normal y extra cuyos valores están dados por una función y posteriormente imprime los datos de salida.
    hNorm=int(input("Teclea las horas normales trabajadas:"))
    hExtra=int(input("Teclea las horas extra trabajadas:"))
    tarifa = float(input("Teclea la tarifa por hora del trabajador:"))
    pagoN=calcularNormal(tarifa,hNorm)
    pagoX=calcularExtra(tarifa,hExtra)
    print("Pago normal: $%.2f" %(pagoN))
    print("Pago por horas extra: $%.2f" % (pagoX),"\n""----------------------")
    print("Pago total: $%.2f" % (pagoN+pagoX))

def calcularNormal(t,h): #Realiza el cálculo del pago por horas normales. Multiplica la tarifa por las horas.
    pago=t*h
    return pago
def calcularExtra(t,h): #Realiza el cálculo del pago por horas extra. Multiplica la tarifa por un factor 1.65 por las horas extra.
    pago=t*h*1.65 #en el primer ejemplo de salida en el documento pdf, el pago Extra posiblemente sea erróneo
    return pago
main()
#Fin del Programa
