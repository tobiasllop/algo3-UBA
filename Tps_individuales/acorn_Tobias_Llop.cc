#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int max_acorns(int t, int h, int costo, vector<vector<int>>& bellotas) {
    vector<vector<int>> memo(h, vector<int>(t, 0)); //matriz de h x t (altura por numero de arboles)
    vector<int> maxPrev(t, 0); // contiene para cada árbol el máximo número de bellotas que Jayjay puede recoger terminando su recorrido en ese árbol, considerando todas las alturas posibles.

    for (int j = 0; j < h; ++j) {
        vector<int> maxCurr(t, 0);  // vector que almacena el máximo número de bellotas que se pueden recoger hasta cierta altura para cada árbol.
        for (int i = 0; i < t; ++i) {
            int opcion1 = maxPrev[i] + bellotas[j][i]; //numero de bellotas si me quedo en el arbol actual
            if (costo <= j) { //si la altura es suficiente para volar a otro arbol
                for (int k = 0; k < t; ++k) {
                    if (k != i) {  // Considerar volar hacia un árbol diferente
                        int bellotas_en_salto = memo[j - costo][k] + bellotas[j][i];
                        opcion1 = max(opcion1, bellotas_en_salto); // Elige el máximo entre quedarse y volar.
                    }
                }
            }
            memo[j][i] = opcion1; //Actualizamos valores en PD
            maxCurr[i] = opcion1;
        }
        maxPrev = maxCurr;
    }

    return *max_element(maxPrev.begin(), maxPrev.end());
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> output;
    int casos;
    cin >> casos;

    for (int c = 0; c < casos; ++c) {
        int t, h, costo;
        cin >> t >> h >> costo;
        vector<vector<int>> bellotas(h, vector<int>(t, 0)); //matriz de bellotas

        for (int j = 0; j < t; ++j) { //armamos matriz de bellotas
            int arbol;
            cin >> arbol;
            for (int i = 0; i < arbol; ++i) {
                int indice;
                cin >> indice;
                bellotas[indice - 1][j] += 1;
            }
        }

        int max_bellotas = max_acorns(t, h, costo, bellotas);
        output.push_back(max_bellotas);
    }

    for (int resultado : output) {
        cout << resultado << endl;
    }

    return 0;
}
