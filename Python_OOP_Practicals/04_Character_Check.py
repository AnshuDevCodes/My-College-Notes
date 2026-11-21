ch = input("Enter a character: ")

if ch.isalpha():
    print("It is a Letter")

    if ch.isupper():
        print("Uppercase Letter")
    else:
        print("Lowercase Letter")

elif ch.isdigit():
    print("It is a Numeric Digit")

    digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR",
              "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

    print("Number in words:", digits[int(ch)])

else:
    print("It is a Special Character")
