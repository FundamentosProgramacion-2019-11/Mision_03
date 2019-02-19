#Autor Sofía Trujillo Vargas
#Rendimiento de un coche con su kilometraje y sus litros de gasolina

def cocheRendimiento(kilome,litros):
    ra=kilome/litros
    return ra

def converMil(kilomet,litros):
    mil=kilomet/1.6093
    gal=litros*0.264
    milg=mil/gal
    return milg

def litrosKilometros(kilome,rendimiento):
    ln=kilome/rendimiento
    return ln

def main():
    k=float(input("¿Cuantos Kilometros recorriste: "))
    l=float(input("¿Cuantos litros gastaste: "))
    kf=float(input("¿Cuantos kilometros quieres recorrer: "))
    ren=cocheRendimiento(k,l)
    mill=converMil(k,l)
    lit=litrosKilometros(kf,ren)
    print("Este es tu rendimiento km/l: ",round(ren,2))
    print(round(mill,2))
    print("Estos son los km que quieres recorrer",kf,"y estos son los litros que necesitas",round(lit,2))

main()