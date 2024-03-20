# Teorica 1: Complejidad computacional
* Llamamos *problema* a a la descripción de los datos de entrada y la respuesta a proporcionar para cada dato de entrada.
* Una instancia de un problema es un juego válido de datos de entrada.
* Ejemplo: 
        1. **Entrada:** Un número n entero no negativo
        2. **Salida:** El numero n es primo?
* Suponemos una *Maquina RAM*
  1. La memoria está dada por una sucesión de celdas numeradas. Cada celda puede almacenar un valor de $b$ bits
  2. Supondremos habitualmente que el tamaño de $b$ en bits de cada celda está fijo, y suponemos que todos los datos individuales que maneja el algoritmo se pueden almacenar con $b$ bits.
  3. Se tiene un programa imperativo no almacenado en memoria, compuesto por asignaciones y las estructuras de control habituales.
  4. Las asignaciones pueden acceder a celdas de memoria y realizar las operaciones estándar sobre los tipos de datos primos habituales.

* Cada instrucción tiene un tiempo de ejecución asociado.
  1. Acceso a cualquier celda/asignaciones/operaciones entre valores logicos: O(1)
  2. Operaciones entre enteros/reales dependen de b: Sumas y restas son O(b), multiplicaciones y divisiones son O(b log b).
$\rightarrow$ Si b esta fijo todas las operaciones son O(1).

* Tiempo de ejecución de un algoritmo A:
  T<sub>A</sub>(*l*) = suma de los tiempos de ejecución de las instrucciones realizadas por el algoritmo con la instancia *l*.
* Dada una instancia *l*, definimos |l| como la cantidad de bits necesarios para almacenar los datos de entrada l.
  1. si b esta fijo y la entrada ocupa n celdas de memoria, entonces |l| = b<sub>n</sub> = O(n)
* Complejidad de un algoritmo A:
* f:A(n) = max<sub>l:|l|=n</sub> T<sub>A</sub>(l)

#### Repaso: Notación O
* dadas dos funciones f, g: $\mathbb{N} \rightarrow \mathbb{R}$, decimos que:
- f(n) = O(g(n)) si existen c $\in \\mathbb{R}_{+}$ y n<sub>0</sub> $\in \mathbb{N}$ tales que f(n) $\leq$ c g(n) para todo n $\geq$ n<sub>0</sub>

 * Si un algoritmo es O(n), se dice *lineal*.
 *  Si un algoritmo es O(n^2), se dice *cuadratico*.
 *   Si un algoritmo es O(n^3), se dice *cubico*.
 *   Si un algoritmo es O(n^k), se dice *polinomial*.
 *   Si un algoritmo es O(log n), se dice l*ogaritmico*.
 *   Si un algoritmo es O(d^n), d $\in \\mathbb{R}_{>1}$, se dice *exponencial*.
* Cualquier función exponencial es peor que cualquier función *polinomial*.
* La función logaritmica es mejor que la funcion lineal (no importa la base)

#### Problemas bien resueltos
* Convención: Los algoritmos polinomiales se consideran satisfactorios (cuanto menor sea el grado, mejor), y los algoritmos supra-polinomiales se consideran no satisfactorios.

#### Problemas de optimización
* Un problema de optimización consiste en encontrar la mejor solución dentro de un conjunto.
* La función f: $S \rightarrow \mathbb{R}$ se denomina función objtivo del problema.
* El conjunto $S$ es la región factible y los elementos x $\in S$ se llaman soluciones factibles.
* El valor z^* $\in \mathbb{R}$ es el valor óptimo del problema y cualquier solución factible x^* $\in S$ tal que f(x^*) = \( z^* \) se llama un óptimo del problema.

#### Problemas de optimización combinatoria
* Un problema de optimización combinatoria es un problema de optimización cuya región factible es un conjunto definido por consideraciones combinatorias (!).
* La combinatoria es la rama de la matemática discreta que estudia la construcción, enumeración y existencia discreta que estudia la construcción, enumeración y existencia de configuraciones de objetos finitos que satisfacen ciertas propiedades.

#### Algoritmos de fuerza bruta
* Un algoritmo de fuerza bruta para un problema de optimización combinatoria consiste en generar todas las soluciones factibles y quedarse con la mejor.
  1. Se trata de una tecnica trivial pero muy general
  2. Suele ser facil de implementar y es un algoritmo exacto. Si hay solución, siempre la encuentra.
* El principal problema de este tipo de algoritmos es su complejidad. Habitualmente, un algoritmo de fuerza bruta tiene una complejidad exponencial.

* **Ejemplo**: Problema de la mochila (ver diapos)

Video: [https://www.youtube.com/watch?v=33k8EPNriTM] 

#### Backtracking
Idea: Recorrer sistematicamente todas las posibles configuraciones del espacio de soluciones de un problema computacional, eliminando las configuraciones parciales que no puedan completarse a una solución.

Habitualmente, utiliza un vector a = (a1, a2, . . . , an) para representar una solución candidata, cada a<sub>i</sub> pertenece un dominio/conjunto ordenado y finito A<sub>i</sub>

▶ En cada paso se extienden las soluciones parciales
a = (a1, a2, . . . , ak ), k < n, agregando un elemento mas,
a<sub>k+1</sub> $\in$ S<sub>k+1</sub> ⊆ A<sub>k+1</sub>, al final del vector a. Las nuevas soluciones parciales son sucesores de la anterior.
▶ Si S<sub>k+1</sub> es vacio, se retrocede a la solución parcial (a1, a2, . . . , ak−1).
▶ Se puede pensar este espacio como un árbol dirigido, donde
cada vértice representa una solución parcial y un vértice x es hijo de y si la solución parcial x se puede extender desde la solución parcial y.
▶ Permite descartar configuraciones antes de explorarlas (podar el árbol).
