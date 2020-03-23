#Autor: Brandon Julien Celaya Torres
#Descripción: Calcula la el pago de un trabajador, con base a sus horas trabajadas.

def pagoNormal (horasTrabajadas, pagoxHora):
    pagoNormal = horasTrabajadas * pagoxHora
    
    return pagoNormal

def pagoExtra (horasExtra, pagoxHora):
    
    pagoExtra = (pagoxHora + pagoxHora*0.65) * horasExtra
    
    return pagoExtra

def main ():
    
    pN = int(input("Introduce tus horas normales trabajadas: "))
    pE = int(input("Introduce tus horas extra trabjadas: "))
    pago = int(input("Introduce el pago por hora: "))
    
    pagoN = pagoNormal (pN, pago)
    pagoE = pagoExtra (pE, pago)
    
    pagoTotal = pagoN + pagoE
    
    
    print ("""
                Horas normales trabajadas: %d
                Horas extra trabajadas: %d
                Pago por hora: %d
                
                Pago normal: $%.2f
                Pago extra: $%.2f
                ---------------------------------
                Pago total: $%.2f """ % (pN, pE, pago, pagoN, pagoE, pagoTotal))
    
    
main ()
    