#include <stdio.h>

int main() {
    
    int contador = 1;
    int soma = 0;
    int numero;
    
    scanf( "%d", &numero);
    
    while (contador < numero) // Testando a condição
  {
    if (contador % 3 == 0 || contador % 5 == 0) {
        soma += contador; //atualizando a var soma
    } contador++; //atualizando a var contador
  }   
  
    printf("%d ", soma);
  
    return 0;
}
