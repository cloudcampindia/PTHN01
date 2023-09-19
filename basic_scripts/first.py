# name = input("Please enter your name: ") # expecting a string
# print(type(name))
# print("Hello, " + name)

# a = input("Enter a number: ")
# b = input("Enter a number: ")
# print(a + b)

# Example list
a = [1, 2, 3, "cloud", True]

# Accessing elements inside a list: +ve indexing
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
# print(a[5]) -> Error: Index out-of-range
print("-----------------")


# Accessing elements inside a list: -ve indexing
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print("-----------------")

# Length of a list
print("Length of a list:", len(a))

print("-----------------")
print(a, len(a))