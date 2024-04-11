"""
Entregable 3 para la materia AyEd III - LCD UBA
Tobias Llop
Link al enunciado: https://vjudge.net/problem/UVA-1231
"""
def max_acorns(t, h, costo, bellotas):
    memo = [[0] * t for _ in range(h)]
    memo[0] = bellotas[0]

    for j in range(1, h):
        for i in range(t):
            opcion1 = memo[j-1][i] + bellotas[j][i]
            opciones = [opcion1]
            if costo <= j:
                for k in range(t):
                    if k != i:  # Considerar volar hacia un árbol diferente
                        bellotas_en_salto = memo[j-costo][k] + bellotas[j][i]
                        opciones.append(bellotas_en_salto)
            memo[j][i] = max(opciones)

    max_bellotas = max(memo[h-1])
    return max_bellotas

matriz = [[1, 0, 0], [0, 0, 0], [0, 1, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1], [0, 1, 0], [0, 1, 0], [0, 2, 1], [1, 0, 0]]
max_acorns(3,10,2,matriz)

def main():
    output = []
    casos = int(input())

    for _ in range(casos):
        t, h, costo = map(int, input().split())
        bellotas = [[0] * t for _ in range(h)]

        for j in range(t):
            arbol = list(map(int, input().split()))
            for i in arbol[1:]:
                bellotas[i-1][j] += 1

        max_bellotas = max_acorns(t, h, costo, bellotas)
        output.append(max_bellotas)

    linea = input()
    if linea == "0":
        pass  

    for resultado in output:
        print(resultado)

if __name__ == "__main__":
    main()
