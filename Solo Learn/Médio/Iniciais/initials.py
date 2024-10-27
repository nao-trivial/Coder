# Function to get initials from names
def get_initials(names):
    initials = []
    for name in names:
        first, last = name.split()  # Assuming each name has two parts
        initials.append(first[0] + last[0])
    return " ".join(initials)

# Taking input
N = int(input("Enter the number of names: "))
names = [input() for _ in range(N)]

# Getting and printing initials
print(get_initials(names))