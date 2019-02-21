#numeroBoletosA = Leer el número de boletos en zona A
# numeroBoletosB = Leer el número de boletos en zona B
# numeroBoletosC = Leer el número de boletos en zona C
# Llama a la función calcularPago, envía como argumentos los valores leídos. Guarda el resultado.
# Imprimir el resultado
#     zonaA = 3250
#     zonaB = 1730
#     zonaC = 850

def calcularZonaA(zonaA):
    A = zonaA*3250
    return A

def calcularZonaB(zonaB):
    B = zonaB*1730
    return B

def calcularZonaC(zonaC):
    C = zonaC*850
    return C

def calcularPagoTotal(BoletosA, BoletosB, BoletosC):
    Total = BoletosA+BoletosB+BoletosC
    return Total

def main():
    zonaA = int(input("Teclea número de boletos para la zona a:"))
    zonaB = int(input("Teclea número de boletos para la zona b:"))
    zonaC = int(input("Tecle número de boletos para la zona c:"))
    BoletosA = calcularZonaA(zonaA)
    BoletosB = calcularZonaB(zonaB)
    BoletosC = calcularZonaC(zonaC)
    PagoTotal = calcularPagoTotal(BoletosA, BoletosB, BoletosC)
    print("Boletos en zona A:", zonaA)
    print("Boletos en zona B:", zonaB)
    print("Boletos en zona C:", zonaC)
    print("Total de pago:", PagoTotal)



main()