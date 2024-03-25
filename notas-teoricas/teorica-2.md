# Teorica 2 - Programación Dinámica.
  * **Superposición de estados** : El árbol de llamadas recursivas resuelve el mismo problema varias veces.

* Un algoritmo de programación dinámica evita estas repeticiones con alguno de estos dos esquemas:
  1. **Enfoque top-down**: se implementa recursivamente, pero se guarda el resultado de cada llamada recursiva en una estructura de datos (memorización). Si una llamada recursiva se repite, se toma el resultado de esta estructura.
  2. Resolvemos primero los subproblemas más pequeños y guardamos (habitualmente en una tabla) todos los resultados.
