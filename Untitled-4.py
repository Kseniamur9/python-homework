number = int(input("Введите пятизначное целое число: "))

ones = number % 10
tens = (number // 10) % 10
hundreds = (number // 100) % 10
thousands = (number // 1000) % 10
tens_thousands = number // 10000

step = tens ** ones
multiplied = step * hundreds
difference = tens_thousands - thousands
result = multiplied / difference

print("Результат:", float(result))