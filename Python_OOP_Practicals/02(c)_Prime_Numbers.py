def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


n = int(input("Enter how many prime numbers: "))

count = 0
num = 2

print("First", n, "prime numbers are:")

while count < n:
    if is_prime(num):
        print(num, end=" ")
        count += 1

    num += 1
