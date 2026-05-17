# Task 1: Print all values in [1, 2, 3, 4] one by one
print("Task 1:")
for val in [1, 2, 3, 4]:
    print(val)

# Task 2: Print all values in [1, 2, 3, 4] multiplied by 20
print("\nTask 2:")
for val in [1, 2, 3, 4]:
    print(val * 20)

# Task 3: Return a new list with only the first letter of each name
print("\nTask 3:")
first_letters = [name[0] for name in ["Elie", "Tim", "Matt"]]
print(first_letters)

# Task 4: Return a new list with only the even values from [1, 2, 3, 4, 5, 6]
print("\nTask 4:")
evens = [n for n in [1, 2, 3, 4, 5, 6] if n % 2 == 0]
print(evens)

# Task 5: Return a new list with values present in both [1, 2, 3, 4] and [3, 4, 5, 6]
print("\nTask 5:")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = [n for n in list1 if n in list2]
print(common)

# Task 6: Return a new list with each word reversed and in lowercase
print("\nTask 6:")
reversed_words = [word[::-1].lower() for word in ["Elie", "Tim", "Matt"]]
print(reversed_words)

# Task 7: Return letters present in both "first" and "third"
print("\nTask 7:")
shared_letters = list({letter for letter in "first" if letter in "third"})
print(sorted(shared_letters))

# Task 8: Numbers between 1 and 100 divisible by 12
print("\nTask 8:")
divisible_by_12 = [n for n in range(1, 101) if n % 12 == 0]
print(divisible_by_12)

# Task 9: Remove vowels from "amazing"
print("\nTask 9:")
no_vowels = [ch for ch in "amazing" if ch not in "aeiou"]
print(no_vowels)

# Task 10: Generate [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
print("\nTask 10:")
grid_3x3 = [[i for i in range(3)] for _ in range(3)]
print(grid_3x3)

# Task 11: Generate a 10x10 list where each row is [0..9]
print("\nTask 11:")
grid_10x10 = [[i for i in range(10)] for _ in range(10)]
for row in grid_10x10:
    print(row)
