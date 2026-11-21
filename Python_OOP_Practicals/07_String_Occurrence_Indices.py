def find_indices(str1, str2):
    indices = []
    start = 0

    while True:
        index = str1.find(str2, start)

        if index == -1:
            break

        indices.append(index)
        start = index + 1

    if len(indices) == 0:
        return -1

    return indices


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print("Indices:", find_indices(s1, s2))
