#include <stdio.h>

int main() {
    int cores;
    double valor;

    scanf("%d", &cores);

    valor = 40 + 5 * cores;
    valor += valor * 0.1;

    printf("%d\n", (int)(valor + 0.5)); // Arredondamento

    return 0;
}
