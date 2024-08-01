// TP 12 - AED III
// Tobias Llop LU: 871/22


#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

// Función para calcular la suma de una submatriz
long long sum_submatrix(const std::vector<std::vector<int>>& matrix, int k) {
    long long sum = 0;
    for (int i = 0; i <= k; ++i) {
        for (int j = 0; j <= k; ++j) {
            sum += matrix[i][j];
        }
    }
    return sum;
}

long long dantzig(std::vector<std::vector<int>>& dist, int n) {
    long long energia = 0;
    for (int k = 0; k < n; ++k) {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (dist[i][j] > dist[i][k] + dist[k][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
        energia += sum_submatrix(dist, k); // Destruimos la torre k, y sumamos la suma de todas sus distancias 
    }
    return energia;
}

int main() {
    int tests;
    std::cin >> tests;

    for (int t = 0; t < tests; ++t) {
        int n;
        std::cin >> n;

        std::vector<std::vector<int>> L(n, std::vector<int>(n)); //Matriz de pesos
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                std::cin >> L[i][j];
            }
        }

        std::vector<int> orden(n);
        for (int i = 0; i < n; ++i) {
            std::cin >> orden[i]; //Leemos el orden en el que queremos que sean destruidas las torres
        }
        std::reverse(orden.begin(), orden.end());

        std::vector<std::vector<int>> L_reordered(n, std::vector<int>(n)); //Inicializamos nuestra matriz reordenada
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                L_reordered[i][j] = L[orden[i]][orden[j]];
            }
        }

        std::cout << dantzig(L_reordered, n) << std::endl; //Llamamos al algo de dantzig
    }

    return 0;
}
