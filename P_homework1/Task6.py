# Задача 6: 
# Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

ticket = int(input("Шестизначный номер билета: "))

def sum(n):
    return n//100 + n//10%10 + n%10
a = ticket%1000
b = ticket//1000
if sum(a) == sum(b):
    print("Билет счастливый")
else:
    print("Билет не счастливый")



    

