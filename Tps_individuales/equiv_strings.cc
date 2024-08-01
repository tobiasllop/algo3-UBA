// Entregable nro 4 para la materia Algoritmos y Estructuras de datos III.
//Autor: Tobias Llop
//LU: 871/22
//Usuario de Vjudge: tobiasllop

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

string ordenar_y_concatenar(const string& pal) {
    if (pal.length() <= 1) { //casos bases donde no se puede subdividir la cadena
        return pal;
    }

    if (pal.length() % 2 != 0) {
        return pal;
    }

    int mitad = pal.length() / 2;
    string s1 = ordenar_y_concatenar(pal.substr(0, mitad));
    string s2 = ordenar_y_concatenar(pal.substr(mitad));

    if (s1 > s2) { //ordenamos lexicograficamente la cadena
        return s2 + s1;
    } else {
        return s1 + s2;
    }
}

bool son_iguales(const string& a, const string& b) {
    return ordenar_y_concatenar(a) == ordenar_y_concatenar(b);
}

int main() {
    string a, b;
    cin >> a;
    cin >> b;
    if (son_iguales(a, b)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }
    return 0;
}