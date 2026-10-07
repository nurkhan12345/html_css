#def calculate(a, op, b):
#    if op == "+":
#        return a + b
#    elif op == "-":
#        return a - b
#    elif op == "*":
#        return a * b
#    elif op == "/":
#        if b != 0:
#            return a / b
#        else:
#            return "Ошибка: деление на ноль"
#    else:
#        return "Ошибка: неизвестная операция"
#while True:
#    first = input("первре число:")
#    if first == "Выход":
#        print("bye")
#        break
#
#    a = float(first)
#    op =input("Ваше действие (+,-,*,/):")
#    b = float(input("второе число:"))
#    result = calculate(a, op, b)
#    print(f"Результат: {result}")



class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def sound(self):
        return "Издает звук"

class Dog(Animal):
    def sound(self):
        return "Гав-гав"

animal = Animal("Животное", 5, "dog")
print(animal.name)  # Вывод: Животное
dog = Dog("Бобик", 3, "dog")
print(dog.name)  # Вывод: Бобик
print(dog.sound())  # Вывод: Гав-гав

#def show_tasks():
#    print("Список задач пуст.")