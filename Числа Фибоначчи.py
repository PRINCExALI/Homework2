# числа Фибоначчи # 0,1,1,2,3,5,8,13,21,34,55,89
# 1 способ через while

n = int(input('Введите длину ряда: '))
f1 = 0
f2 = 1
print(f1, f2, end=' ')

i = 2  # так как первые два числа уже будут выведены
while i < n:
    f1, f2 = f2, f1 + f2  # f1 приравнивается к f2, f2 приравнивается к f1 + f2
    print(f2, end=' ')  # Выводится f2
    i += 1
print()

# 2 способ через for

n = int(input('Введите длину ряда: ')) - 2  # так как первые два числа уже будут выведены
f3 = 0
f4 = 1
print(f3, f4, end=' ')

for i in range(1, n + 1):
    f3, f4 = f4, f3 + f4
    print(f4, end=' ')
print()


# 3 способ через функцию-рекурсию

def fibonacci(x):
    if x <= 1:
        return x
    return fibonacci(x - 1) + fibonacci(x - 2)


x = int(input('Введите длину ряда: '))
# print(fibonacci(x)) - вывод одного  числа из ряда Фибоначчи
# для вывода ряда чисел Фибоначчи:
for i in range(x):
    print(fibonacci(i), end=' ')
