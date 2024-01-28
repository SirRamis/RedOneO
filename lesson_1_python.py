# 2
print("Hello world!")

# 3
user_name = input("Введите имя : ")
print(f'Hellow {user_name}')

# 4
nam1 = input("Введите первое число : ")
nam2 = input("Введите второе число : ")
rez = int(nam1) + int(nam2)
print(f"Результат = {rez}")

# 1.2
a = "*"
print(a * 9, end='\n')
print(a, ' ' * 6, end='*''\n')
print(a, ' ' * 6, end='*''\n')
print(a * 9, end='\n')

# 1.3
a = int(input('Напишите четырёхзначное число: '))
b = a % 10
c = a % 100 // 10
d = a % 1000 // 100
e = a % 10000 // 1000
print("Тысячи -", e)
print("Сотни -", d)
print("Десятки -", c)
print("Единицы -", b)

# 1.4
a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))
c = (a + b) ** 2
d = a ** 2 + b ** 2
print("Квадрат суммы", a, "и", b, "равен", c)
print("Сумма квадратов", a, "и", b, "равна", d)
