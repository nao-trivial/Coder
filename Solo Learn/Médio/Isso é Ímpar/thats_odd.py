# Function to find the sum of all even integers in a list
def sum_of_evens(lst):
    return sum(num for num in lst if num % 2 == 0)

# Read the length of the list
N = int(input())

# Read the list elements
numbers = [int(input()) for _ in range(N)]

# Calculate the sum of even numbers
result = sum_of_evens(numbers)

# Print the result
print(result)
