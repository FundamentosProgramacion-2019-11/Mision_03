#Autor: Brandon Julien Celaya Torres - A01745762
#Descripción: calcula el costo de boletos introducidos por área(s) escogida e imprime el total

def costoAreas (boletosA, boletosB, boletosC):
    zonaA = boletosA * 3250
    zonaB = boletosB * 1730
    zonaC = boletosC * 850
    
    totalPago = zonaA + zonaB + zonaC
    
    return totalPago
    
def main ():
    bA = int(input("¿Cuántos boletos en zona A quieres? "))
    bB = int(input("¿Cuántos boletos en zona B quieres? "))
    bC = int(input("¿Cuántos boletos en zona C quieres? "))
    
    totalPago = costoAreas(bA, bB, bC)
    
    print("""              Número de boletos en zona A: %d
              Número de boletos en zona B: %d
              Número de boletos en zona C: %d
              El costo total es: %.2f """ % (bA, bB, bC, totalPago))  #estos van cada uno a cada parámetro de la otra función
    
main ()
