# Задача 2:
# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3) 100 -> 1 (1 + 0 + 0)

# number = int(input("Введите трехзначное число: "))
# sum = number//100 + number//10%10 + number%10
# print(sum)

number = input('Введите число n: ')
sum = 0
for i in number:
    sum += int(i)
print(sum)
