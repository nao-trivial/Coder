#include <stdio.h>
#include <string.h>

int find_item_time(char boxes[], char target_item[]) {
    char *token;
    int time_taken = 0;
    
    // Split the string by commas
    token = strtok(boxes, ",");
    
    while (token != NULL) {
        time_taken += 5;
        if (strcmp(token, target_item) == 0) {
            return time_taken;
        }
        token = strtok(NULL, ",");
    }
    
    // If the item is not found
    return -1;  // Return -1 to indicate the item was not found
}

int main() {
    char boxes[100], target_item[100];
    
    // Read input for boxes and target item
    fgets(boxes, sizeof(boxes), stdin);
    fgets(target_item, sizeof(target_item), stdin);
    
    // Remove the trailing newline characters if they exist
    boxes[strcspn(boxes, "\n")] = 0;
    target_item[strcspn(target_item, "\n")] = 0;
    
    // Call the function and print the result
    int result = find_item_time(boxes, target_item);
    
    if (result == -1) {
        printf("Item not found in the boxes.\n");
    } else {
        printf("%d\n", result);
    }
    
    return 0;
}