# вычисляем факториал
# 1 способ
import math
a = math.factorial(int(input('Введите число:')))
print(a)

# 2 способ через while
number = int(input('Введите число:'))
b = 1
fact_ = 1
while b <= number:
    fact_ *= b
    b += 1
print(fact_)

# 3 способ через for
n = int(input('Введите число:'))
fact_2 = 1
for i in range(1, n + 1):
    fact_2 = fact_2 * i
print(fact_2)


# 4 способ через функцию-рекурсию
def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)


print(factorial(int(input('Введите число:'))))
