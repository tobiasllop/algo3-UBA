def hallar_equipos(jugadores):
    mejores_atacantes = []
    mejores_defensores = []
    suma_maxima_ataque = 0
    suma_maxima_defensa = 0

    def busqueda_exhaustiva(indice_inicial, atacantes, defensores, suma_ataque, suma_defensa):
        nonlocal suma_maxima_ataque, suma_maxima_defensa, mejores_atacantes, mejores_defensores

        if len(atacantes) == 5:
            if suma_ataque > suma_maxima_ataque or (suma_ataque == suma_maxima_ataque and suma_defensa > suma_maxima_defensa):
                suma_maxima_ataque = suma_ataque
                suma_maxima_defensa = suma_defensa
                mejores_atacantes = sorted(atacantes)
                mejores_defensores = sorted(defensores)
            elif suma_ataque == suma_maxima_ataque and suma_defensa == suma_maxima_defensa:
                atacantes_actuales = sorted(atacantes)
                if atacantes_actuales < mejores_atacantes:
                    mejores_atacantes = atacantes_actuales
                    mejores_defensores = sorted(defensores)
            return

        for i in range(indice_inicial, len(jugadores)):
            jugador = jugadores[i]
            atacantes.append(jugador[0])
            defensores.remove(jugador[0])
            busqueda_exhaustiva(i + 1, atacantes, defensores, suma_ataque + jugador[1], suma_defensa - jugador[2])
            atacantes.pop()
            defensores.append(jugador[0])

    busqueda_exhaustiva(0, [], [j[0] for j in jugadores], 0, sum(j[2] for j in jugadores))
    return (f"({', '.join(mejores_atacantes)})"),(f"({', '.join(mejores_defensores)})")

def main():
    casos = int(input())
    output = []
    for caso in range(1, casos + 1):
        jugadores = []
        for _ in range(10):
            nombre, ataque, defensa = input().split()
            jugadores.append((nombre, int(ataque), int(defensa)))
        
        output.append(hallar_equipos(jugadores))
    for i in range(len(output)):
        print(f"Case {i+1}:")
        print(output[i][0])
        print(output[i][1])

if __name__ == "__main__":
    main()