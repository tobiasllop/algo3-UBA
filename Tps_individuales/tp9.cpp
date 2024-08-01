//Entregable 9 TDA
// Tobias Llop
// LU: 871/22

#include <iostream>
#include <vector>
#include <unordered_map>
#include <utility>
#include <algorithm>

using namespace std;

// Calcula el costo (número de giros) para cambiar de una combinación a otra
int funcion_de_costo(string a, string b) {
    int c = 0;
    for (int i = 0; i < 4; i++) {
        c += min(abs(a[i] - b[i]), 10 - abs(a[i] - b[i])); //Calcula el costo mínimo para cambiar de una combinación a otra considerando la envoltura de los dígitos (0-9 y 9-0).
    }
    return c;
}

typedef pair<int, int> Edge;

// Implementación del algoritmo de Kruskal para encontrar el MST
int findParent(vector<int>& parent, int i) {
    if (parent[i] == i)
        return i;
    return parent[i] = findParent(parent, parent[i]);
}

void unionSets(vector<int>& parent, vector<int>& rank, int x, int y) {
    int xRoot = findParent(parent, x);
    int yRoot = findParent(parent, y);

    if (rank[xRoot] < rank[yRoot])
        parent[xRoot] = yRoot;
    else if (rank[xRoot] > rank[yRoot])
        parent[yRoot] = xRoot;
    else {
        parent[yRoot] = xRoot;
        rank[xRoot]++;
    }
}

int kruskal(unordered_map<int, vector<Edge>>& graph) {
    vector<Edge> edges;
    for (auto& pair : graph) {
        int u = pair.first;
        for (auto& neighbor : pair.second) {
            int v = neighbor.first;
            int weight = neighbor.second;
            edges.push_back(make_pair(weight, u * graph.size() + v));
        }
    }

    sort(edges.begin(), edges.end());

    int n = graph.size();
    vector<int> parent(n);
    vector<int> rank(n, 0);
    for (int i = 0; i < n; i++)
        parent[i] = i;

    int mstCost = 0;
    for (auto& edge : edges) {
        int weight = edge.first;
        int u = edge.second / n;
        int v = edge.second % n;
         
        // Si u y v no están en el mismo conjunto, únelos y añade el peso al costo del MST
        if (findParent(parent, u) != findParent(parent, v)) {
            mstCost += weight;
            unionSets(parent, rank, u, v);
        }
    }

    return mstCost;
}

int main() {
    int T;
    cin >> T; // Lee el número de casos de prueba

    string initialState = "0000"; // Estado inicial de la combinación o nodo fantasma

    for (int t = 0; t < T; t++) {
        int n;
        cin >> n; // Lee el número de llaves

        vector<string> keys(n);
        for (int i = 0; i < n; i++)
            cin >> keys[i]; // Lee cada llave

        int initial = 10000;
        for (string& key : keys)
            initial = min(initial, funcion_de_costo(key, initialState)); // Calcula el costo mínimo para la primera llave desde "0000"

        unordered_map<int, vector<Edge>> graph; //Me armo el grafo completo donde cada nodo representa una combinación de llave. 
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int w = funcion_de_costo(keys[i], keys[j]); //Cada arista entre nodos tiene un peso que representa el costo de cambiar de una combinación a otra, calculado nuevamente con funcion_de_costo.
                graph[i].push_back(make_pair(j, w));
                graph[j].push_back(make_pair(i, w)); 
            }
        }

        int mstCost = kruskal(graph); // Corro kruskal sobre el grafo
        cout << mstCost + initial << endl; // Imprime el costo total (MST + costo inicial)
    }

    return 0;
}