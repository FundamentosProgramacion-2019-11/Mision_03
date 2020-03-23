#Autor: Brandon Julien Celaya Torres - A01745762
#Descripción: calcula el rendimiento de un coche en kilómetros/litros y millas/galón

def kilLitros (kilometros, litros):
    rendKil = kilometros/litros
    
    return rendKil

def milGalon (kilometros, litros):
    rendGal = (kilometros/1.6093) / (litros*0.264)
    
    return rendGal

def main ():
    
    kil = int(input("Teclea el número de kilómetros recorridos: "))
    lit = int(input("Teclea el número de litros de hasolina usados: "))
    
    rKil = kilLitros (kil, lit)
    rGal = milGalon (kil, lit)
    
    print ("""
                Kilómetros recorridos: %d
                Gasolina utilizada: %d
                
                Si recorres %d kilómetros con %d litros de gasolina, el rendimiento es:
                %.2f km/l
                %.2f mi/gal
                """ % (kil, lit, kil, lit, rKil, rGal))
    
    distancia = int(input("Cuántos kilómetros vas a recorrer? "))
    
    litros = distancia/rKil
    
    print ("""
                Para recorrer %d kilómetros, necesitas %.2f litros de gasolina""" % (distancia, litros))
    
main ()
    