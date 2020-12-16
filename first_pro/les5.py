# #ДЗ
#  Створити клас rectangle
# 1) об'єкт приймає два параметри - дві сторони х у
# 2) описати методи арифметичні
#   + сума площин двок об'єктів
#   - різниця площин
# 3) логічні оператори:
#   == повертає true якщо рівні по площині
#   != якщо не рівні
#   >, < відповідно
# 4) len() - сума сторін

class Rectangle:
    def __init__(self, x, y):
        self.list = [x, y]

    def __add__(self, other):
        return self.list[0] * self.list[1] + other.list[0] * other.list[1]

    def __sub__(self, other):
        return self.list[0] * self.list[1] - other.list[0] * other.list[1]

    def __eq__(self, other):
        return self.list[0] * self.list[1] == other.list[0] * other.list[1]

    def __ne__(self, other):
        return self.list[0] * self.list[1] != other.list[0] * other.list[1]

    def __gt__(self, other):
        return self.list[0] * self.list[1] > other.list[0] * other.list[1]

    def __lt__(self, other):
        return self.list[0] * self.list[1] < other.list[0] * other.list[1]

    def __len__(self):
        return self.list[0] + self.list[1]


rect1 = Rectangle(3, 5)
rect2 = Rectangle(7, 9)
print(rect1 + rect2)
print(rect1 - rect2)
print(rect1 == rect2)
print(rect1 != rect2)
print(len(rect1))




# class Rectangle:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __repr__(self):
#          return f'{self.x} -- {self.y}'
#     def area(self):
#         return self.x * self.y
#     def comparePlus(self, object):
#         return self.area()+object.area()
#     def compareMinus(self, object):
#         return self.area()-object.area()
#     def compareDifference(self, object):
#         return self.area()==object.area()
#     def compareEqually(self, object):
#         return self.area()!=object.area()
#     def compareBig(self, object):
#         if self.area()>object.area():
#             return '>'
#         else:
#             return '<'
#     def len(self):
#         return self.x+self.y
#
#
#
# first=Rectangle(5,7)
# second=Rectangle(3,9)
# print(first.area())
# print(first.comparePlus(second))
# print(first.compareMinus(second))
# print(first.compareDifference(second))
# print(first.compareEqually(second))
# print(first.compareBig(second))
# print(first.len())

#
#
# ######################################################################
#
# 1)Створити пустий list

# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text
list_db = []


class Letter:
    __count = 0

    def __init__(self):
        self.__text = ''
        Letter.__count += 1

    @property
    def my_text(self):
        return self.__text

    @my_text.setter
    def my_text(self, text):
        self.__text = text

    def save(self, list_db):
        list_db.append(self.__text)

    @classmethod
    def show_count(cls):
        print(f'cont: {cls.__count}')


letter = Letter()
letter.my_text = 'Hello'
print(letter.my_text)
letter.save(list_db)
letter.my_text = 'World'
letter.save(list_db)
letter2 = Letter()
Letter.show_count()
print(list_db)
