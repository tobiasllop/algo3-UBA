#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

const int MAX_N = 10000;
int dist[MAX_N][MAX_N];

long long dantzig(int n) {
    int energia = 0;
    std::vector<bool> visited(n, false);

    for (int k = 0; k < n; k++) {
        visited[k] = true;
        std::vector<int> updated(n, INT_MAX);

        for (int i = 0; i < k; i++) {
            if (visited[i]) {
                for (int j = 0; j < n; j++) {
                    if (!visited[j]) {
                        updated[j] = std::min(updated[j], dist[i][j]);
                    }
                }
            }
        }

        for (int j = 0; j < n; j++) {
            if (!visited[j]) {
                for (int i = 0; i <= k; i++) {
                    if (visited[i]) {
                        dist[i][j] = std::min(dist[i][j], dist[i][k] + updated[j]);
                    }
                }
            }
        }

        int sum = 0;
        for (int i = 0; i <= k; i++) {
            for (int j = 0; j <= k; j++) {
                sum += dist[i][j];
            }
        }
        energia += sum;
    }
    return energia;
}

int main() {
    int tests;
    std::cin >> tests;
    for (int t = 0; t < tests; t++) {
        int n;
        std::cin >> n;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                std::cin >> dist[i][j];
            }
        }
        std::vector<int> orden(n);
        for (int i = 0; i < n; i++) {
            std::cin >> orden[i];
        }
        std::reverse(orden.begin(), orden.end());
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = dist[orden[i] - 1][orden[j] - 1];
            }
        }
        std::cout << dantzig(n) << std::endl;
    }
    return 0;
}