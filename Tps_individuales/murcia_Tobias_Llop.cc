#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

string solve(const vector<int>& h, const vector<int>& w) {
    int n = h.size();
    vector<int> max_inc(n, 0);
    vector<int> max_dec(n, 0);

    // Calculamos los máximos incrementos
    for (int i = 0; i < n; ++i) {
        max_inc[i] = w[i]; // Inicializamos con el ancho del edificio actual
        for (int j = 0; j < i; ++j) {
            if (h[i] > h[j]) {
                max_inc[i] = max(max_inc[i], max_inc[j] + w[i]); // Actualizamos si encontramos un incremento mayor
            }
        }
    }

    // Calculamos los máximos decrementos
    for (int i = n - 1; i >= 0; --i) {
        max_dec[i] = w[i]; // Inicializamos con el ancho del edificio actual
        for (int j = n - 1; j > i; --j) {
            if (h[i] > h[j]) {
                max_dec[i] = max(max_dec[i], max_dec[j] + w[i]); // Actualizamos si encontramos un decremento mayor
            }
        }
    }

    int max_inc_global = *max_element(max_inc.begin(), max_inc.end()); // Encontramos el máximo global de incremento
    int max_dec_global = *max_element(max_dec.begin(), max_dec.end()); // Encontramos el máximo global de decremento

    // Determinamos cuál es mayor
    if (max_inc_global >= max_dec_global) {
        return "Increasing (" + to_string(max_inc_global) + "). Decreasing (" + to_string(max_dec_global) + ").";
    } else {
        return "Decreasing (" + to_string(max_dec_global) + "). Increasing (" + to_string(max_inc_global) + ").";
    }
}

int main() {
    int casos;
    cin >> casos;

    for (int caso = 1; caso <= casos; ++caso) {
        int cant_edificios;
        cin >> cant_edificios;
        vector<int> altura(cant_edificios);
        vector<int> ancho(cant_edificios);

        for (int i = 0; i < cant_edificios; ++i) {
            cin >> altura[i];
        }

        for (int i = 0; i < cant_edificios; ++i) {
            cin >> ancho[i];
        }

        string resultado = solve(altura, ancho);
        cout << "Case " << caso << ". " << resultado << endl;
    }

    return 0;
}