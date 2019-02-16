# Guillermo De Anda Casas, A01375892
# Programa que calcula el salario a pagar por horas extras, el pago normal y el pago total de un trabajador.

def pagoExtra(E,P):
    extra = (E*(1.65*P))
    return extra

def pagoNormal(N,P):
    pago = N * P
    return pago

def main():
    N = int(input("Teclea las horas normales trabajadas: "))
    E = int(input("Teclea las horas extras trabajadas: "))
    P = int(input("Teclea el pago por hora: "))
    pagoNormal(N,P)
    pagoExtra(E,P)
    print("Pago normal: $%.2f"%pagoNormal(N,P))
    print("Pago extra: $%.2f"%pagoExtra(E,P))
    print("Pago total: $%.2f"%(pagoNormal(N,P)+pagoExtra(E,P)))

main()