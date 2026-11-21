class DigitError(Exception):
    pass


class SpecialCharacterError(Exception):
    pass


try:
    name = input("Enter your name: ")

    if not name.strip():
        raise ValueError("Name cannot be empty")

    for ch in name:
        if ch.isdigit():
            raise DigitError("Name cannot contain digits")

        elif not ch.isalpha() and ch != " ":
            raise SpecialCharacterError(
                "Name cannot contain special characters"
            )

    print("Valid Name:", name)

except DigitError as e:
    print("Error:", e)

except SpecialCharacterError as e:
    print("Error:", e)

except ValueError as e:
    print("Error:", e)
