str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

n = int(input("Enter value of n: "))

new_str1 = str2[:n] + str1[n:]
new_str2 = str1[:n] + str2[n:]

print("First string after swapping:", new_str1)
print("Second string after swapping:", new_str2)
