#include <stdio.h>

int main() {
    int jardas;
    
    // Input the number of jardas
    scanf("%d", &jardas);
    
    // Check the conditions and print the corresponding output
    if (jardas > 10) {
        printf("High Five\n");
    } else if (jardas >= 1) {
        for (int i = 0; i < jardas; i++) {
            printf("Ra!");
        }
        printf("\n");
    } else if (jardas < 1) {
        printf("shh\n");
    }
    
    return 0;
}
