# Divide and conqueer
* Consiste en dividir un problema en problemas similares.. pero más chicos. Luego resolvemos los problemas menores y combinamos las soluciones de los problemas menores para obtener la solución del problema original.

        Algoritmo DC(X):
            Si X es suficientemente chico:
                ADHOC(X)
            En caso contrario:
                Descomponer X en X_1, X_2, ... X_k
                Para i desde 1 hasta k:
                    Y = DC(X_i)
                Combinar las soluciones Yi, para construir una solución para X.
**Un ejemplo: El algoritmo de Karatsuba**
* Queremos multiplicar dos enteros de n cifras en base b, X e Y.
* Algoritmo tradicional requiere O(n^2) operaciones.
* Pero:

    Sea 
    * **X** = X<sub>1</sub> * b<sup>(n/2)</sup> + X<sub>0</sub> 
    * **Y** = Y<sub>1</sub> * b<sup>(n/2)</sup> + Y<sub>0</sub>

    Entonces:

    * **XY** = X<sub>1</sub>Y<sub>1</sub>b<sup>n</sup> + (X<sub>0</sub>Y<sub>1</sub> + X<sub>1</sub>Y<sub>0</sub>) b<sup>(n/2)</sup> + X<sub>0</sub>Y<sub>0</sub>

Utilizando este método también nos da O(n^2). Pero..

**Algoritmo de Karatsuba(II)**
m<sub>1</sub> = X<sub>0</sub>Y<sub>0</sub>, m<sub>2</sub> = X<sub>1</sub>Y<sub>1</sub>, m<sub>3</sub> = (X<sub>0</sub> - X<sub>1</sub>)(Y<sub>1</sub> - Y<sub>0</sub>)

Resulta que 
XY = m<sub>2</sub> b<sup>n</sup> + (m<sub>1</sub> + m<sub>2</sub>+ m<sub>3</sub>) b<sup>n/2</sup> + m<sub>1</sub>

O sea tenemos 3 subproblemas de tamaño n/2, lo que mejora la complejidad del algoritmo llevandola a O(n<sup>log<sub>2</sub> 3</sup>) ≈ O(n<sup>1.59</sup>)

## Teorema Maestro

Se usa para resolver recurrencias del tipo:

 $$
 T(n) = a * T(n/b) + f(n),
 $$

donde $a ≥ 1$ y $b > 1$ son constantes positivas y $f(n)$ es una función asintóticamente positiva. Este tipo de recurrencias describen algoritmos que dividen a un problema de tamaño $n$ en a subproblemas de tamaño $n/b$ que se resuelven en tiempo $T(n/b)$. La función $f(n)$ engloba todos los costos asociados a la división y combinación de los resultados de los subproblemas.

1. Si $f(n) ∈ O(n^{\log_b(a)- \epsilon})$ para alguna constante $\epsilon > 0$ Entonces $T(n) \in \Theta(n^{\log _b(a)})$
2. Si $f(n) \in \Theta(n^{\log _b(a)})$ entonces $T(n)\in \Theta(n^{\log _b(a)} \cdot \log n)$
3.  Si $f(n) ∈ \Omega(n^{\log_b(a) + \epsilon})$ para alguna constante $\epsilon > 0$,  y si para todo $n$ suficientemente grande vale que $a \cdot f(n/b) ≤ c \cdot f(n)$ para alguna constante $c < 1$. Entonces $T(n) \in \Theta(f(n))$