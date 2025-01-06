# import helper #or
from helper import print_hello 

# function and assignment

print_hello("Hello, World!")

# def sum(a, b):
#     return a + b

# print(sum(1, 2))

# # user input
# def circle_area(r):
#     pi = 3.14
#     return pi * r * r

# r = int(input("Enter the radius of the circle: ")) # int is used to convert the input to integer or casting

# print(circle_area(r))


# # conditional
# def even_odd(n):
#     if n % 2 == 0:
#         print("even")
#     elif n == 0:
#         print("zero")
#     else:
#         print("odd")

# even_odd(5)

# # try except

# try:
#     number = int(input("Enter a number: "))  # Might raise ValueError
#     print(f"Your number is: {number}")
# except ValueError as error_details:
#     print(f"That's not a valid number")
#     print(f"Error details: {error_details}")
    
# # loop while loop

# count = 0
# while count < 5:
#     print(f"Count is: {count}")
#     count += 1  # Increment count to avoid infinite loop

# user_input = ""
# while user_input != "quit":
#     user_input = input("Enter something: ")
#     print(user_input)
    
# # scanf array with loop in python

# # Initialize an empty list
# array = []

# # Loop to input 10 elements
# print("Enter 10 elements for the array:")
# for i in range(10):
#     element = int(input(f"Element {i+1}: "))  # Convert input to integer
#     array.append(element)

# # Display the array
# print("The array you entered is:", array)

# # Input all 10 elements in one line
# array = list(map(int, input("Enter 10 elements separated by spaces: ").split()))

# # Ensure the input has exactly 10 elements
# if len(array) != 10:
#     print("Please enter exactly 10 elements.")
# else:
#     print("The array you entered is:", array)


# n = int(input("Berapa banyak angka yang ingin dimasukkan? "))
# numbers = []

# for i in range(n):
#     num = int(input(f"Masukkan angka ke-{i+1}: "))
#     numbers.append(num)

# print(numbers)  # Output: [angka1, angka2, ...]
