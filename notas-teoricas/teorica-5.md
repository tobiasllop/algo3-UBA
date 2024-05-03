# Teorica 5: Grafos 

Un **grafo** es un par ordenado G = (V, E): el conjunto V , de vértices o nodos , y el de aristas/arcos E, que relacionan a esos nodos.

Ejemplo: 
V: {1,2,3,4,5,6,7,8,9} // Nodos, Vertices
E = {(1,2), (1,9), (2,3), (2,6), (2,7), (3,4), (4,5), (4,6), (5,6), (6,7), (7,8), (8,9)} // Aristas, conexiones

En gral:

$$
n = |V| = \text{ cantidad de nodos}
$$

$$
m = |E| = \text{ cantidad de aristas}
$$

**Nodos adyacentes o vecinos**
Dados $v, w \in V$ , se denominan **adyacentes** cuando $e = (v, w) ∈ E$, y que **$e$ es incidente** a $v$ y $w$. 

Similarmente, la vecindad de $v$, denotada por $N_G(v)$ es el conjunto de vertices adyacentes a $v$, es decir:

$$
N_G(v) = {w ∈ V | (v, w) ∈ E}
$$

Por otro lado, la cantidad de aristas incidentes a un vértice v se llama grado, definida como:

$$
d_G(v) = |N_G(v)|
$$

**Teorema**: Dado un grafo de $G = (V, E)$, la suma de los grados de sus vertices es el doble de la cantidad de aristas. Es decir,

$$
\sum_{v \in V}{d(v)} = 2m
$$

## Tipos de grafos
* **MultiGrafo**: En un multigrafo, E pasa a ser un multiconjunto, es decir, pueden haber varias aristas entre un mismo par de vértices.
* **PseudoGrafo**: Los pseudografos pueden tiene varias aristas entre un mismo par de vértices, y también puede haber aristas que unan a un mismo par de vértices (llamadas *loops*)
* **Grafo Dirigido**: Las aristas están ordenadas e indican la dirección de cada una. Ejemplo E: {(1,2), (1,3)}
  1 --> 2
  1 --> 3
* **Grafo completo**: Todos sus vértices son adyacentes 
entre sí, o tiene todas las aristas posibles. Se nota $\bold{K_n}$

$$
m_{K_n} = \frac{n(n-1)}{2}
$$
* **Grafo complemento**: Tiene el mismo conjunto de vértices, pero si dos vértices son adyacentes en $G$ si y sólo si no lo son en $G^C$. O, visto de otra forma, $G^C$ tiene todas las aristas que no estaban en $G$.

$$
m_{G^C} = \frac{n(n-1)}{2} - m
$$

## Recorridos
* Un **recorrido** en un grafo es una secuencia de vertices $P = v_0, v_1 · · · v_k$ tal que todos los pares consecutivos son adyacentes, es decir, $(v_i, v_i+1) ∈ E,  ∀i = 0, ..., k − 1$. Para multi- y pseudo-grafos, se debe especificar entre qué aristas se pasa. Por ejemplo:
    P= 1→(1,2)→2→(2,3)→3→(3,4)→4→(4,6)→6→(2,6)→2→(1,2)→1→(1,9)
→9
* Un **camino** es un recorrido que no pasa dos veces por el mismo vértice. Por ejemplo:
    P = 1→2→3→4→6→7→8→9
* Una **sección** es un tramo del recorrido $P$, se nota $P_{v_iv_j}$.
* Un **circuito** es un recorrido que empieza y termina en el mismo vértice.
* Un **ciclo o circuito simple** es un circuito (de tres o más vértices) que no repite vértices.
* Dado un recorrido $P$, su **longitud**, $l(P)$ es la cantidad de aristas que tiene.
* La **distancia entre dos vértices** $u$ y $v$ se define como la longitud del recorrido (camino) más corto entre $u$ y $v$, $d(u,v)$.
Si no existe recorrido entre $u$ y $v$ se define la distancia como infinito, $d(u,v) = ∞$.

**Teorema**: Si un recorrido $P$ entre $v$ y $w$ cumple $l(P) = d(v, w)$, entonces es un camino.

**Teorema**: Para cualquier grafo $G = (V, E)$, la función de distancia $d : V × V \rightarrow \N $ es una métrica, es decir, cumple las siguientes propiedades para todo $u, v, w ∈ V$ :
$$
\blacktriangleright d(u, v) = 0 \iff u = v \\
\blacktriangleright d(u, v) = d(v, u) \\
\blacktriangleright d(u, w) ≤ d(u, v) + d(v, w) 
$$

## Subgrafos
Dado un grafo $G = (V_G, E_G)$,
Un **subgrafo** de $G$ es un grafo $H = (V_H, E_H)$ tal que:
  1. $V_H ⊆ V_G$ 
  2. $E_H ⊆ E_G ∩ (V_H × V_H)$.

Los notamos como $H ⊆ G$.

* $H$ es un **subgrafo propio** cuando $H ⊆ G$ y $H \neq G $.
* $H$ es un **subgrafo generador** cuando $H ⊆ G$ y $V_H = V_G$.
* $H$ es un **subgrafo inducido** cuando $(v, w) ∈ E_H \iff v, w ∈ V_H ∧ (v, w) ∈ E_H$. 
  Estos subgrafos pueden definirse únicamente por su conjunto de vértices, y se denota como $G_{[V_H]}$.

## Conectividad
Un grafo se denomina **conexo** cuando existe un camino entre todo par de vértices. 

Una **componente conexa** de un grafo es un subgrafo inducido conexo maximal (no se pueden agregar más vértices y mantenerlo conexo) de G.

## Representacion de Grafos
Existen distintas alternativas para representar grafos en un algoritmo, que proveen ventajas y desventajas a la hora de realizar diversas operaciones.

**Lista de aristas**

 El grafo se almacena como una lista de pares de vertices, que representan sus aristas. Esta
es la forma mas simple de representarlo, y es el formato que se asume que tiene la entrada de cualquier algoritmo de grafos. Debido a su falta de estructura, realizar la mayorıa de las operaciones resulta costoso, con la excepcion de agregar nodos o aristas.

Esta estructura tiene ciertas variaciones. Por ejemplo, se pueden ordenar los vertices dentro de cada lista, lo cual permite usar busqueda binaria para comprobar la pertenencia de un vertice a ellas, pero aumenta la complejidad de construir la estructura y la de agregar vertices (porque
hay que mantener el orden).

**Listas de adyacencia**

Se mantienen n listas, donde cada lista $L_i$ contiene todos los vertices de $N(v_i)$. Esto permite realizar algunas operaciones mas rapidamente, y la estructura se puede construir a partir de la lista de aristas en tiempo lineal.

**Matriz de adyacencia**
En este caso, se tiene una matriz $M ∈ \{0, 1\}^{n×n}$, donde cada posición está determinada por:
$$M_{ij} = 
\begin{cases}
1 & \text{ si } (i, j) \in E \\
0 & \text{en caso contrario}  
\end{cases}
$$
La matriz es simétrica para grafos, pero no necesariamente para digrafos.

La estructura permite comprobar si dos vértices son adyacentes en tiempo constante. Sin embargo, construirla a partir de una lista de adyacencia es una operación de complejidad cuadrática, y la estructura es muy rígida (para agregar un vértice se debe armar una nueva matriz). Además,
la complejidad espacial es también $O(|V|^2)$, lo cual es problemático para guardar grafos con pocas aristas.

**Matriz de incidencia**

Esta estructura es una matriz $I ∈ {0, 1}^{nxn}$ donde las filas representan los vértices y las columnas las aristas. Una posición i, j tiene uno cuando la arista de la columna j es incidente al vértice de la fila i.


Seguir escribiendo en clase practica.
