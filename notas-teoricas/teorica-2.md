# Teorica 2 - Programación Dinámica.
  * **Superposición de estados** : El árbol de llamadas recursivas resuelve el mismo problema varias veces.
* **Superposición de problemas**: Decimos que tenemos superposición de problemas si la cantidad de llamadas recursivas de la función sin memorizar es mucho mayor que la cantidad de estados posibles.

$$
 \Omega(\# llamadasrecursivas) \geq O(\# estados)
$$

* Un algoritmo de programación dinámica evita estas repeticiones con alguno de estos dos esquemas:
  1. **Enfoque top-down**: se implementa recursivamente, pero se guarda el resultado de cada llamada recursiva en una estructura de datos (memorización). Si una llamada recursiva se repite, se toma el resultado de esta estructura.
  2. **Bottom Up**: Resolvemos primero los subproblemas más pequeños y guardamos (habitualmente en una tabla) todos los resultados.
