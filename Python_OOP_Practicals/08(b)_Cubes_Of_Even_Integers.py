my_list = [1, 2, 3, 4, 5, 6, "Hello", 8]

result = [x ** 3 for x in my_list
          if type(x) == int and x % 2 == 0]

print("Original List:", my_list)
print("Cubes of Even Integers:", result)
