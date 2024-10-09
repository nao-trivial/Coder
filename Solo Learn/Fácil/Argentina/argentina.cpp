#include <iostream>
using namespace std;

int main() {
    
    int pesos;
    int dollars;
    
    cin >> pesos;
    cin >> dollars;
    
    int exchange = 0.02 * pesos;
    
    if (exchange > dollars) {
        cout << "Dollars";
    } else {
        cout << "Pesos";
    }
    return 0;
}