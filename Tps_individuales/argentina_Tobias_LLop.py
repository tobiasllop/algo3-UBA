def hallar_equipos(jugadores):
    mejores_atacantes = [] 
    mejores_defensores = []
    suma_maxima_ataque = 0
    suma_maxima_defensa = 0

    def busqueda_exhaustiva(indice_inicial , atacantes, defensores, suma_ataque, suma_defensa):
        nonlocal suma_maxima_ataque, suma_maxima_defensa, mejores_atacantes, mejores_defensores
        # Explicacion de variables
        # indice_inicial: El índice desde el cual se comienza la búsqueda.
        # atacantes: Lista de jugadores seleccionados como atacantes.
        # defensores: Lista de jugadores restantes que pueden ser seleccionados como defensores.
        # suma_ataque: La suma de las habilidades de ataque de los atacantes seleccionados hasta el momento.
        # suma_defensa: La suma de las habilidades de defensa de los defensores restantes.

        if len(atacantes) == 5:
            if suma_ataque > suma_maxima_ataque or (suma_ataque == suma_maxima_ataque and suma_defensa > suma_maxima_defensa):
                suma_maxima_ataque = suma_ataque
                suma_maxima_defensa = suma_defensa
                mejores_atacantes = sorted(atacantes) #Ordenamos por orden lexicografico
                mejores_defensores = sorted(defensores)
            elif suma_ataque == suma_maxima_ataque and suma_defensa == suma_maxima_defensa:
                atacantes_actuales = sorted(atacantes)
                if atacantes_actuales < mejores_atacantes: #Esto chequea que el orden lexicografico sea el minimo
                    mejores_atacantes = atacantes_actuales
                    mejores_defensores = sorted(defensores)
            return

        for i in range(indice_inicial, len(jugadores)):
            jugador = jugadores[i]
            atacantes.append(jugador[0])
            defensores.remove(jugador[0])
            busqueda_exhaustiva(i + 1, atacantes, defensores, suma_ataque + jugador[1], suma_defensa - jugador[2]) #hacemos la busqueda exhautiva con el jugador como atacante
            atacantes.pop() #Eliminamos al jugador de los atacantes
            defensores.append(jugador[0]) #Agregamos al jugador como defensor

    busqueda_exhaustiva(0, [], [j[0] for j in jugadores], 0, sum(j[2] for j in jugadores)) #Llamada que resuelve el problema
   # Se llama a la función busqueda_exhaustiva con los valores iniciales apropiados: 
   # índice inicial 0, listas vacías de atacantes. Lista de todos los jugadores como defensores, suma de ataque 0 y suma de defensa igual a la suma de las habilidades de defensa de todos los jugadores.
    return (f"({', '.join(mejores_atacantes)})"),(f"({', '.join(mejores_defensores)})")
    # Devolvemos los valores de la funcion recursiva

def main():
    casos = int(input())
    output = []
    for caso in range(1, casos + 1):
        jugadores = [] #Lista de triplas. 1.Nombre, 2. ataque 3. Defensa
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