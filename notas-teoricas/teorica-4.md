# Algoritmos Golosos
## Heuristicas
Una heurística es un procedimiento computacional que intenta obtener soluciones de buena calidad para un problema, intentando que su comportamiento sea lo más preciso posible.

Por ejemplo, para un problema de optimización, una heurística obtendría una solución con un valor cercano al óptimo.

Decimos que A es un algoritmo $\epsilon$-aproximado ($\epsilon$ > 0) para un
problema si:

$$
| \frac{X_A - X_{OPT}}{X_{OPT}}|  \leq \epsilon
$$

donde $X_A$ es el resultado del algoritmo y $X_{OPT}$ es el valor óptimo.

## Algoritmos golosos
Idea: Construir una solución seleccionando en cada paso la mejor alternativa, sin considerar (o haciéndolo débilmente) las implicancias de esta selección.

* Habitualmente, proporcionan heurísticas sencillas para
problemas de optimización.
* En general permiten construir soluciones razonables (pero
sub-óptimas) en tiempos eficientes.
* Sin embargo, en ocasiones nos pueden dar interesantes
sorpresas!

#### Ejemplo: Problema del cambio
Problema:
Dado un monto $m$ y un conjunto de denominaciones $d_1, ..., d_k$, encontrar la mínima cantidad de monedas necesarias para obtener el valor $m$.

Para encontrar soluciones (no necesariamente óptimas) de este problema, se puede emplear un algoritmo goloso simple: en cada paso, seleccionar la moneda de mayor valor que no exceda el monto restante

    Dar-Cambio(D, m)
        suma = 0
        M = {}
        while suma < m
            proxima = max{d | d ∈ D, d ≤ m}
            M = M ∪ {proxima}
            suma = suma + proxima
        return M
Para ciertos conjuntos de denominaciones, como el tradicional ({1, 5, 10, 25, 50}), este algoritmo siempre devuelve soluciones óptimas, mientras que para otros no (en D = {1, 5, 10, 12}, m = 21, el algoritmo devuelve un conjunto de 6 monedas cuando la solución óptima tiene 3).

El algoritmo es goloso porque en cada paso selecciona la moneda de mayor valor posible, sin preocuparse que esto puede llevar a una mala solución, y nunca modifica una decisión tomada

## Principio de optimalidad
**Las partes de una solución óptima a un problema, deben ser soluciones óptimas de los correspondientes subproblemas.**

i.e $O_1 \npoints O_n$ es óptima $\iff O_1 \npoints O_j$ con $j < n$ también es óptima.

Permite obtener una solución óptima al problema original a partir de soluciones óptimas de los subproblemas.


En general hay dos formas de ver que un algoritmo goloso es optimo

▶ Demostrar que nuestro algoritmo siempre se mantiene ”adelante” de cualquier otra solución óptima (Greedy stays ahead).

▶ Mostrar que podemos agarrar una solución óptima y modificarla sin incrementar su costo y llevarla a la de nuestro algoritmo goloso (Exchange argument).

## Prueba de correctitud de un algoritmo greedy
Para probar que un algoritmo goloso es correcto tenemos que ver que: 

* La solución que obtuvimos es válida
* (En general) es óptima.


