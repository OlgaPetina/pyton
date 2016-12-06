#16

accumulator = 0
for i in range(ord('e'), ord('g')+1):
    accumulator = accumulator + i
print(accumulator)

#17

a = int(input("17. Введите число = "))


def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a - 1)
print(factorial(a))

#18

import random

random_num = random.randint(100000000000, 1000000000000)
print("18.", random_num)


def upper_from_random(n):
    max_num = 0
    while (n > 0):
        digit = n % 10
        n = n // 10
        if max_num < digit:
            max_num = digit
    return max_num

print(upper_from_random(random_num))




