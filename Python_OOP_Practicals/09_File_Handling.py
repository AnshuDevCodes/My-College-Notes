filename = input("Enter file name: ")

with open(filename, "r") as file:
    data = file.read()

# a. Count characters, words and lines
characters = len(data)
words = len(data.split())
lines = len(data.splitlines())

print("Total characters:", characters)
print("Total words:", words)
print("Total lines:", lines)

# b. Frequency of each character
frequency = {}

for ch in data:
    frequency[ch] = frequency.get(ch, 0) + 1

print("Character frequency:")
print(frequency)

# c. Print words in reverse order
word_list = data.split()
print("Words in reverse order:", word_list[::-1])

# d. Copy even and odd lines into separate files
with open(filename, "r") as file:
    all_lines = file.readlines()

with open("File1", "w") as even_file:
    for i, line in enumerate(all_lines, start=1):
        if i % 2 == 0:
            even_file.write(line)

with open("File2", "w") as odd_file:
    for i, line in enumerate(all_lines, start=1):
        if i % 2 != 0:
            odd_file.write(line)

print("Even lines copied to File1")
print("Odd lines copied to File2")
