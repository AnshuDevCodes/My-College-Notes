text = input("Enter a string: ")
ch = input("Enter a character: ")

# a. Frequency of character
print("Frequency:", text.count(ch))

# b. Replace character
new_ch = input("Enter replacement character: ")
print("After replacement:", text.replace(ch, new_ch))

# c. Remove first occurrence
print("After removing first occurrence:", text.replace(ch, "", 1))

# d. Remove all occurrences
print("After removing all occurrences:", text.replace(ch, ""))
