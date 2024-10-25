#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SALES_TAX 0.07
#define DISCOUNT 0.30

double calculate_savings(const char* prices_str) {
    // Parse the input string into an array of doubles
    double prices[100]; // Assuming a maximum of 100 items
    int count = 0;
    char* token;
    char* prices_str_copy = strdup(prices_str); // Create a modifiable copy of the input string

    token = strtok(prices_str_copy, ",");
    while (token != NULL) {
        prices[count++] = atof(token);
        token = strtok(NULL, ",");
    }

    // Identify the most expensive item
    double max_price = 0.0;
    for (int i = 0; i < count; i++) {
        if (prices[i] > max_price) {
            max_price = prices[i];
        }
    }

    // Calculate the total savings for the discounted items
    double savings = 0.0;
    for (int i = 0; i < count; i++) {
        if (prices[i] != max_price) {
            savings += prices[i] * DISCOUNT;
        }
    }

    // Apply sales tax to the savings
    double savings_with_tax = savings * (1 + SALES_TAX);

    // Calculate the final savings amount, leaving the cents below a dollar as tip
    int savings_int = (int)savings_with_tax;
    double tip = savings_with_tax - savings_int;
    if (tip > 0 && tip < 1) {
        return savings_int;
    } else {
        return savings_int;
    }

    // Free the copied string
    free(prices_str_copy);
}

int main() {
    char prices_str[1000];
    
    // Read input from the user
    fgets(prices_str, sizeof(prices_str), stdin);
    
    // Remove the trailing newline character if present
    prices_str[strcspn(prices_str, "\n")] = '\0';
    
    int savings = (int)calculate_savings(prices_str);
    printf("%d\n", savings);

    return 0;
}
