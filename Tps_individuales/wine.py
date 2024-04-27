# Entregable TP 5 AyEd 3
# Tobias Llop
# LU:871/22
# Vjudge: tobiasllop

def Gergovia(n, l):
    comp = 0
    vend = 0
    res = 0
    while (comp < n and vend < n):
        while l[comp] <= 0:
            comp += 1
            if comp == n:
                return res
        while l[vend] >= 0:
            vend +=1
            if vend == n:
                return res
        if abs(l[comp]) >= abs(l[vend]):
            res += abs(comp - vend) * abs(l[vend])
            l[comp] += l[vend]
            l[vend] = 0
        else:
            res += abs(vend-comp) * (l[comp])
            l[vend] += l[comp]
            l[comp] = 0
    return res

def main():
    while True:
        cases = []
        n = int(input())
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