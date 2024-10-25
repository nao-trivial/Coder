def carrot_distribution(total_carrots, number_of_boxes):
    # Calculate leftover carrots after even distribution
    leftover_carrots = total_carrots % number_of_boxes
    
    # Check if the leftover carrots are enough for the cake
    if leftover_carrots >= 7:
        return 'Cake Time'
    else:
        # Calculate how many more carrots are needed
        needed_carrots = 7 - leftover_carrots
        return f'I need to buy {needed_carrots} more'

# Sample Input
total_carrots = int(input())
number_of_boxes = int(input())

# Calculate and print the output
print(carrot_distribution(total_carrots, number_of_boxes))
