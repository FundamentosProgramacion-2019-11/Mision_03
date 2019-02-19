#FRANCISCO JAVIER GONZALEZ MOLINA A01748636
#BOLETOS PARA UN CONCIERTO

#esta funcion calcula el total de pago que se realizara
##puse el valor de los boletos como variable para que se entendiera mas
#al final regresa el total que se pagara por los boletos seleccionados.
def calcularPago (nOboletosA, nOboletosB, nOboletosC):
    boletoA= 3250
    boletoB= 1730
    boletoC= 850
    totalpago= ((nOboletosA*boletoA)+(nOboletosB*boletoB)+(nOboletosC*boletoC))
    return totalpago

#Esta funcion realiza las operaciones para saber el valor total de los boletos
#deseados
def main ():
    nOboletosA= int(input("Numero de boletos en zona A: "))
    nOboletosB= int(input("Numero de boletos en zona B: "))
    nOboletosC= int(input("Numero de boletos en zona C: "))
    total= calcularPago(nOboletosA,nOboletosB, nOboletosC)
    print ("""
    Costo total es: $%.2f"""% (total))

#llama la funcion "main ()"
main()