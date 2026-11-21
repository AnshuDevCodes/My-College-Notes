my_list = [1, 2, 3, 4, 5, 6, "Hello", 8]

result = []

for x in my_list:
    if type(x) == int and x % 2 == 0:
        result.append(x ** 3)

print("Cubes of even numbers:", result)
