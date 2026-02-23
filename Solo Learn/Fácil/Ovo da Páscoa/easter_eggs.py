def evaluate_eggs(total_eggs, your_eggs, friend_eggs):
    if your_eggs + friend_eggs < total_eggs:
        return 'Keep Hunting'
    else:
        return 'Candy Time'

# Sample Input
total_eggs = int(input())
your_eggs = int(input())
friend_eggs = int(input())

# Evaluate eggs
result = evaluate_eggs(total_eggs, your_eggs, friend_eggs)
print(result)
