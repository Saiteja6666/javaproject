def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_strong_number(num):
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10
    return total == num

# Input from user
number = int(input("Enter a number: "))

if is_strong_number(number):
    print(f"{number} is a Strong Number.")
else:
    print(f"{number} is not a Strong Number.")
