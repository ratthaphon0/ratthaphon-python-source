# Empty list
empty_list = []
another_empty_list = list()

# List with initial values
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]

# List from range
numbers_range = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List from string
letters = list("hello")  # ['h', 'e', 'l', 'l', 'o']
fruits = tuple(fruits)
print(f"Fruits: {type(list(fruits))}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed_list}")