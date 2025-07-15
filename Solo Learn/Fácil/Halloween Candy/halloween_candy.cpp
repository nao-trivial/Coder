#include <iostream>
using namespace std;

int main() {
    int houses;
    float resultado;
    cin >> houses;

    //your code goes here
    
    resultado = (2.0 / houses ) * 100;
    
    int inteiro = resultado;
    
    if (resultado > inteiro) {
        inteiro += 1;
        cout << inteiro;
    } else {
        cout << inteiro;
    }  
    
    return 0;
}