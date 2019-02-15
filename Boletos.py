# Autor: Cesar Guzman Guadarrama, A01748918
# este programa preguntara cuantos boletos quieres comprar y te dara el total a pagar

def calcularPago(Ca,Cb,Cc):       #funcion secundaria realiza las operaciones para completar la tarea
    A = Ca * 3250
    B = Cb * 1730
    C = Cc * 850

    P = A + B + C
    return P




def main():                    #Funcion principal pide valores necesarios para completar la tarea
    numeroBoletosA = int(input("Número de boletos en zona A"))
    numeroBoletosB = int(input("Número de boletos en zona B"))
    numeroBoletosC = int(input("Número de boletos en zona C"))

    print("el costo total es de $",calcularPago(numeroBoletosA,numeroBoletosB,numeroBoletosC))
main()

