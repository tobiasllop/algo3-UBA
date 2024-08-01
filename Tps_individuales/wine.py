# Entregable TP 5 AyEd 3
# Tobias Llop
# LU:871/22
# Vjudge: tobiasllop

def Gergovia(n, l):
    comp = 0 #indice del comprador
    vend = 0 #indice del vendedor
    res = 0 #trabajo total
    while (comp < n and vend < n):
        while l[comp] <= 0: #Si el lugar de la lista es negativo, entonces el puntero de comprador lo saltea
            comp += 1
            if comp == n:
                return res
        while l[vend] >= 0: #Si el lugar de la lista es positivo, entonces el puntero de vendedor lo saltea
            vend +=1
            if vend == n:
                return res
        if abs(l[comp]) >= abs(l[vend]): #Si el comprador actual puede absorber toda la oferta del vendedor actual 
            res += abs(comp - vend) * abs(l[vend]) #se calcula el trabajo necesario
            l[comp] += l[vend] #se actualizan las listas de compradores y vendedores.
            l[vend] = 0
        else: #Si el vendedor tiene más oferta de la que el comprador puede absorber
            res += abs(vend-comp) * (l[comp]) #transacción parcial
            l[vend] += l[comp] #actualizamos listas de compradores y vendedores
            l[comp] = 0
    return res

def main():
    while True:
        cases = []
        n = int(input()) #Tamaño de la lista
        if n != 0:
            l = list(map(int, input().split()))
            cases.append(l)
            for caso in cases:
                res = Gergovia(n, caso)
                print(res)
        else:
            break
        
if __name__ == "__main__":
    main()