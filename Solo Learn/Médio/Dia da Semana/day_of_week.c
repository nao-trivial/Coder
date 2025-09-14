#define _XOPEN_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <locale.h>

int main() {
    char date_input[100];
    fgets(date_input, sizeof(date_input), stdin);
    date_input[strcspn(date_input, "\n")] = '\0'; // Remove newline

    struct tm tm = {0};
    char *parse_result;

    // Try parsing with "MM/DD/YYYY" format
    parse_result = strptime(date_input, "%m/%d/%Y", &tm);
    if (parse_result != NULL && *parse_result == '\0') {
        // Parsing successful
    } else {
        // Try parsing with "Month Day, Year" format in English
        setlocale(LC_TIME, "en_US.UTF-8");
        parse_result = strptime(date_input, "%B %d, %Y", &tm);
        if (parse_result == NULL || *parse_result != '\0') {
            printf("Invalid date format. Please use 'MM/DD/YYYY' or 'Month Day, Year'.\n");
            exit(0);
        }
    }

    // Format the day of the week
    char day_of_week[20];
    strftime(day_of_week, sizeof(day_of_week), "%A", &tm);
    printf("%s\n", day_of_week);

    return 0;
}