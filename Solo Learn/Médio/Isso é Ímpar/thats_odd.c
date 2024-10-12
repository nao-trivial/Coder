#include <stdio.h>

int main() {
    int N, num, sum = 0;

    // Read the length of the list
    scanf("%d", &N);

    // Iterate through the list elements
    for (int i = 0; i < N; i++) {
        // Read each element
        scanf("%d", &num);

        // Check if the number is even
        if (num % 2 == 0) {
            // Add to the sum if even
            sum += num;
        }
    }

    // Print the result
    printf("%d\n", sum);

    return 0;
}
