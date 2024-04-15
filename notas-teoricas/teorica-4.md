# Algoritmos Golosos
## Heuristicas
Una heurística es un procedimiento computacional que intenta obtener soluciones de buena calidad para un problema, intentando que su comportamiento sea lo más preciso posible.

 Por ejemplo, para un problema de optimización,
una heurística obtendría una solución con un valor cercano al óptimo.

Decimos que A es un algoritmo $\epsilon$-aproximado ($\epsilon$ > 0) para un
problema si:

$$
| \frac{X_A - X_{OPT}}{X_{OPT}}|  \leq \epsilon
$$

donde $X_A$ es el resultado del algoritmo y $X_{OPT}$ es el valor óptimo.

## Algoritmos golosos
Idea: Construir una solución seleccionando en cada paso la mejor alternativa, sin considerar (o haciéndolo débilmente) las implicancias de esta selección.

* Habitualmente, proporcionan heurísticas sencillas para
problemas de optimizaci´on.
* En general permiten construir soluciones razonables (pero
sub-´optimas) en tiempos eficientes.
* Sin embargo, en ocasiones nos pueden dar interesantes
sorpresas!