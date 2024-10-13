#include <iostream>
using namespace std;

int main() {

    int contador = 1;
    int soma = 0;
    int numero;
    
    cin >> numero;
    
    while (contador < numero) // Testando a condição
  {
    if (contador % 3 == 0 || contador % 5 == 0) {
        soma += contador; //atualizando a var soma
    } contador++; //atualizando a var contador
  }   
  
    cout << soma << "\n";
    
    return 0;
}