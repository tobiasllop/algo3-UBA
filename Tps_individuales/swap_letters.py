#Entregable 6
#Materia: AyEd3
#Lu: 871/22
#Vjudge: tobiasllop

def swap(s,t,n):
    pos_a = []
    pos_b = []
    
    for i in range(n):
        if s[i] == 'a' and t[i] == 'b': #contamos las posiciones en donde s tiene una a y t tiene una b
            pos_a.append(i+1)
        elif s[i] == 'b' and t[i] == 'a': #contamos las posiciones en donde s tiene una b y t tiene una a
            pos_b.append(i+1)
        
    if (len(pos_a) + len(pos_b)) % 2 != 0: #Si la suma de los desajustes es impar es imposible emparejar los dos strings
        return -1
    
    swaps = []
    for i in range(0,len(pos_a)-1,2): #registramos los intercambios
        swaps.append(f"{pos_a[i]} {pos_a[i+1]}")
    for i in range(0,len(pos_b)-1,2):
        swaps.append(f"{pos_b[i]} {pos_b[i+1]}")
    if len(pos_a) % 2:
        swaps.append(f"{pos_a[-1]} {pos_a[-1]}")
        swaps.append(f"{pos_a[-1]} {pos_b[-1]}")
    k = len(swaps) #cantidad de intercambios
    swaps.insert(0,k) #incluimos la cantidad de intercambios al principio de la lista
    return swaps


def main():
    n = int(input())
    s = input()
    t = input()
    res = swap(s,t,n)
    if res != -1:
        for i in res:
            print(i) 
    else:
        print(-1)

if __name__ == "__main__":
    main()

