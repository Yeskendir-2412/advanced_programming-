def div(number):
    temp = number
    while temp > 0:
        digit = temp % 10
        if digit == 0 or number % digit != 0:
            return False
        temp //= 10
    return True

n = int(input("Enter n: "))

for num in range(1, n + 1):
    if div(num):
        print(num, end=" ")
