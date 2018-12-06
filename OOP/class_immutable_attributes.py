# поля класса доступны через имя класса и одинаковы для всех экземпляров, которые не переопределили его

class Counter:
    counter = 0

    def __init__(self):
        Counter.counter += 1

    def change(self):
        self.counter = 12


first = Counter()
second = Counter()
third = Counter()

print(first.counter) # 3
print(second.counter) # 3
print(third.counter) # 3

first.counter += 1 # поле counter переопределено для экземпляра first, мы не меняем объект, мы присваиваем first.counter новое число
print(first.counter) # 4
print(second.counter) # 3
print(third.counter) # 3
