#include <stdio.h>

int main() {

    int pesos;
    int dollars;
    
    scanf("%d", &pesos);
    scanf("%d", &dollars);
    
    int exchange = 0.02 * pesos;
    
    if (exchange > dollars) {
        printf("Dollars");
    } else {
        printf("Pesos");
    }
    
    return 0;
}