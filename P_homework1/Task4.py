# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1 
# 24 -> 4  16  4 
# 60 -> 10  40  10

s = int(input("Количество сделанных журавликов = "))
# s = k+c+p
# p = c
# k = 2*(p+c) = 2*(p+p) = 4*p
# s = k+c+p = 4*p+p+p = 6*p
p = s//6
c = p
k = 4*s//6
print(f'Катя сделала {k}, Петя сделал {p}, Сережа сделал {c}')


