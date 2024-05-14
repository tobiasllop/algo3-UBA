# Arboles

* Un **arbol** es un grafo conexo sin circuitos simples.
* Una arista e de G es **puente**  $\iff$ G − e tiene mas componentes
conexas que G.
* Un vértice v de G es **punto de articulacion** $\iff$ G − v tiene más componentes conexas que G.

**Teorema**: Dado un grafo G = (V, X) son equivalentes:

1. G es un árbol. (grafo Conexo y sin circ simples)
2. Existe exactamente un camino entre todo par de nodos.
3. Si se quita cualquier arista a G queda un grafo no conexo (toda arista es puente).
4. Si se agrega una arista e a G resulta un grafo con exactamente un circuito simple *C*, y e $\subset$ *C*

## Lemas y corolarios

**Lema 1**: Sea G = (V, X) un grafo conexo y e ∈ X. 

G − e es conexo $\iff$ e pertenece a un circuito simple de G.

**Def**: una *Hoja* es un nodo de grado 1.

**Lema 2**: Todo árbol no trivial tiene al menos dos hojas.

**Lema 3**: Sea G = (V, X) árbol. Entonces m(cant aristas) = n − 1.

**Corolario 1**: Sea G = (V, X) sin circuitos simples y c componentes conexas. Entonces m = n − c.

**Corolario 2**: Sea G = (V, X) con c componentes conexas.
Entonces m ≥ n − c.

## Arboles enraizados

* Un **árbol enraizado** es un árbol que tiene un vértice distinguido que llamamos **raíz**.
* Explícitamente queda definido un árbol dirigido.
* El **nivel** de un vértice es la distancia de la raíz a ese vértice.
* La **altura** h de un árbol enraizado es el máximo nivel de sus vertices.
* Los **vértices internos** de un árbol enraizado son aquellos que no son ni hojas ni la raíz.
* Un árbol enraizado se dice **m-ario** $\iff$ todos sus vértices internos tienen grado $\leq$ m + 1 y su raíz a tiene grado $\leq$ m.
* Un árbol enraizado se dice **exactamente m-ario** si todos sus vértices internos tienen grado m + 1 y su raíz m.
* Un árbol se dice balanceado si todas sus hojas están a nivel h
o h − 1.
* Un árbol se dice balanceado completo si todas sus hojas están
a nivel h.
* Decimos que dos vértices adyacentes tienen relación padre-hijo, siendo el padre el vértice de menor nivel.


**Teorema**:

* #(Hojas de un árbol m-ario de altura h) $\leq$ m<sup>h</sup> hojas. 
* Un árbol m-ario con l hojas tiene h ≥ [log<sub>m</sub> l].
* Si T es un árbol exactamente m-ario balanceado no trivial
entonces h = [log<sub>m</sub>l].

## Arboles generadores

 Un **árbol generador (AG)** de un grafo G es un subgrafo
generador (que tiene el mismo conjunto de vértices) de G que es árbol.

**Teorema**:

* Todo grafo conexo tiene (al menos) un árbol generador.
* G conexo. G tiene un único árbol generador $\iff$ G es árbol.
* Sea $T = (V, X_T )$ un AG de $G = (V, X)$ y $e ∈ X \backslash X_T$ .  Entonces $T' = T + e − f = (V, X_T ∪ \{e\} \backslash {f })$, con $f$ una arista del único circuito de T + e, T' es árbol generador de G.

## Recorrido de árboles, grafos o digrafos.

* **BFS**: se comienza por el nivel 0 (la raíz) y se visita cada vértice en un nivel antes de pasar al siguiente nivel.
* **DFS**: se comienza por la raíz y se explora cada rama lo más profundo posible antes de retroceder.

**Aplicaciones generales**

* para encontrar todas las componentes conexas de un grafo,
* para encontrar todas las componentes fuertemente conexas de
un digrafo,
* los puntos de corte (y las aristas puentes) de un grafo conexo,
* determinar si un grafo o digrafo tiene ciclos,
* en el problema de flujo maximo,
* camino mínimo de un grafo o digrafo no pesado,
* encontrar vertices que estan a distancia menor que k.

**Aplicaciones BFS**

* Encontrar la distancia a un vértice

**Aplicaciones DFS**

* Detección de ciclos

**Teorema**: Dado un grafo (digrafo) $G$.

$G$ tiene un ciclo  $\iff$ existe un backward edge en $G$.

* Sort topológico
* Ordenar los nodos de acuerdo a su valor en el arreglo hasta de mayor a menor. 
* Determinar las componentes fuertemente conexas de un
digrafo
* Determinar los puntos de cortes y las aristas puentes de un
grafo.

## Tipos de aristas en DFS

Si aplicamos DFS para enumerar todos los vértices de un digrafo,
se pueden clasificar sus arcos en 4 tipos:

* **Tree edges**: las usadas para descubrir nuevos vértices.
* **Backward edges**: las que van de un vértice a un ancestro.
* **Forward edges**: las que van de un vértice a un descendiente que no sea un hijo.
* **Cross edges**: las que van de un vertice a otro vertice ya
visitado que no es ni descendiente ni ancestro.

**Para grafos, solamente existen aristas tree edges y back edges**


## Algunas observaciones sobre tree edges y back edges en DFS
**Def**: Decimos que una backward edge $b$ cubre a una tree edge $(u, v)$ de un árbol DFS $T$ con $u$ padre de $v$ si $b$ conecta un descendiente de $u$ con un ancestro de $v$ en $T$.

Ej:

        a #(ancestro de v)
          \
            u #(ancestro de v)
              \
                v #(descendiente de u)
                  \
                    b #(descendiente de u)

Para el siguiente caso, las back edges ``(b --> a)`` y ``(v --> u)`` cubrirían al tree-edge ``(u --> v)``.

                    
* **Observación 1**: Una backward edge no puede ser un puente.
*  
