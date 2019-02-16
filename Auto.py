# Guillermo De Anda Casas , A01375892
# Programa que calcula el rendimiento de un auto y los litros que se necesitan para ciertos km.

def calculaK(K,L):
    res1 = K / L
    return res1

def calculaM(K,L):
    mi =  K / 1.6093
    gal = L * 0.264
    res2 = mi / gal
    return res2

def calculaKilom(kilo,K,L):
    litros = ((kilo*L)/K)
    return litros

def main():
    K = int(input("Teclea el núemro de km recorridos: "))
    L = int(input("Teclea el número de litros de gasolina usados: "))
    kilo = int(input("¿Cuántos kilómetros vas a recorrer? "))
    calculaK(K,L)
    calculaM(K,L)
    calculaKilom(kilo,K,L)
    print("Si recorres", K,"kms con", L,"litros de gasolina, el rendimiento es:")
    print("%.2f"%calculaK(K,L),"km/l")
    print("%.2f"%calculaM(K,L),"mi/gal")
    print("Para recorrer",kilo,"km. necesitas %.2f"%calculaKilom(kilo,K,L),"litros de gasolina")

main()