#Rafael Romero Bello A01747730
#Este programa calcula las entradas
def calcularEntradas(zonaA, zonaB, zonaC):
    A=3250*zonaA
    B=1730*zonaB
    C=850*zonaC
    zonaT=A+B+C
    return zonaT

def main():
    AT=int(input("insete el totalA:"))
    BT=int(input("inserte el totalB:"))
    CT=int(input("inserte el totalC:"))
    total=calcularEntradas(AT,BT,CT)
    print("numero de boletos en zonaA:",AT)
    print("numero de boletos en zona B:",BT)
    print("numero de boletos en zonaC:",CT)
    print("el costo total es:%.2f"%(total))

main()