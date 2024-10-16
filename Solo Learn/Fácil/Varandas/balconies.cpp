#include <stdio.h>
#include <stdlib.h>

int main() {
    // Variables to store dimensions and areas
    int heightA, widthA, heightB, widthB, areaA, areaB;

    // Input dimensions for apartment A
    scanf("%d,%d", &heightA, &widthA);

    // Input dimensions for apartment B
    scanf("%d,%d", &heightB, &widthB);

    // Calculate areas
    areaA = heightA * widthA;
    areaB = heightB * widthB;

    // Compare areas and output result
    if (areaA > areaB) {
        printf("Apartment A\n");
    } else if (areaB > areaA) {
        printf("Apartment B\n");
    } else {
        printf("Both apartments have balconies of the same size.\n");
    }

    return 0;
}
