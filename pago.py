#Rafael Romero Bello
#A01747730
#Escribe un programa que lea las horas normales, las horas extras y el pago por hora de un trabajador. Calcula e imprime
#os datos de pago semanal.
def calcularpagonormal(horasNormales, horasExtras, pagohora):
    pagoNormal=horasNormales*pagohora
    return pagoNormal
def calcularpagoextra(horasNormales, horasExtras, pagohora):
    pagoExtra=((pagohora*horasExtras)/65)*100
    return pagoExtra
def main():
    hn=float(input("Teclea las horas normales trabajadas:"))
    he=float(input("Teclea las horas extras trabajadas:"))
    ph=float(input("Teclea el pago por hora:"))
    TN=calcularpagonormal(hn,0,ph)
    TE=calcularpagoextra(0,he,ph)
    total=TN+TE
    print("pago Normal:%.2f"%(TN))
    print("pago extra:%.2f"%(TE))
    print("Pago Total:%.2f"%(total))

main()

