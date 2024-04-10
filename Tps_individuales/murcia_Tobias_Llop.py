"""
Entregable 2 para la materia AyEd III - LCD UBA
Tobias Llop
Link al enunciado: https://vjudge.net/problem/UVA-11790
"""

def max_creciente(h, w, n):
    dp = [0] * n
    for i in range(n):
        dp[i] = w[i]
        for j in range(i):
            if h[i] > h[j]:
                dp[i] = max(dp[i], dp[j] + w[i])
    return max(dp)

def max_decrec(h, w, n):
    dp = [0] * n
    for i in range(n):
        dp[i] = w[i]
        for j in range(i):
            if h[i] < h[j]:
                dp[i] = max(dp[i], dp[j] + w[i])
    return max(dp)

def solve(h, w, n):
    inc_dp = [w[i] for i in range(n)]  # Lista para el caso de aumento
    dec_dp = [w[i] for i in range(n)]  # Lista para el caso de disminución

    max_inc = w[0]  # Inicializar con el primer edificio para el caso de aumento
    max_dec = w[0]  # Inicializar con el primer edificio para el caso de disminución

    for i in range(1, n):
        for j in range(i):
            if h[i] > h[j]:
                inc_dp[i] = max(inc_dp[i], inc_dp[j] + w[i])
                max_inc = max(max_inc, inc_dp[i])
            elif h[i] < h[j]:
                dec_dp[i] = max(dec_dp[i], dec_dp[j] + w[i])
                max_dec = max(max_dec, dec_dp[i])

    # Determinar cuál es mayor
    if max_inc >= max_dec:
        return f"Increasing ({max_inc}). Decreasing ({max_dec})."
    else:
        return f"Decreasing ({max_dec}). Increasing ({max_inc})."

def main():
    casos = int(input())
    output = [None] * casos

    for caso in range(casos):
        cant_edificios = int(input())
        altura = list(map(int, input().split()))
        ancho = list(map(int, input().split()))
        output[caso] = solve(altura, ancho, cant_edificios)

    for caso, resultado in enumerate(output, start=1):
        print(f"Case {caso}. {resultado}")

if __name__ == "__main__":
    main()
