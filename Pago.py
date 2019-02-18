# Autor David Yair Fernández Salas
# Este programa te dice el pago total de un trabajador

"""En este problema usamos la función CalcularNormal con los parametros de las horas trabajadas normales, y el pago por hora,
para que nos regrese el calculo de las horas normales"""
def CalcularNormal(normales, pago):
    normal= normales*pago
    return normal

"""Se uso la función CalcularExtra con los parametros de las horas extras trabajadas y el pago por hora
para que nos regrese el valor de las horas extras"""
def CalcularExtra(extras, pago):
    Extra= extras*(pago*1.65)
    return Extra

"""En esta función se uso el main que es el responsable que funcione el programa y 
el usuario  ingresa sus datos, para que al final imprima los datos deseados"""
def main():
    Pnormales=float(input(" Teclea las horas normales trabajadas: " ))
    PExtra=float(input(" Teclea las horas extra trabajadas: "))
    pago= float(input(" Teclea el pago por hora: "))

    normal = CalcularNormal(Pnormales,pago)
    extra = CalcularExtra(PExtra,pago)

    print("")
    print("Pago normal: $%.2f"%(normal))
    print("Pago extra:$%.2f"%(extra))
    print("-------------------")
    print("Pago total:$%.2f"%(normal + extra))
main()