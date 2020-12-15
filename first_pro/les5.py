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
        self.x = x
        self.y = y
    def __repr__(self):
         return f'{self.x} -- {self.y}'
    def area(self):
        return self.x * self.y
    def comparePlus(self, object):
        return self.area()+object.area()
    def compareMinus(self, object):
        return self.area()-object.area()
    def compareDifference(self, object):
        return self.area()==object.area()
    def compareEqually(self, object):
        return self.area()!=object.area()
    def compareBig(self, object):
        if self.area()>object.area():
            return '>'
        else:
            return '<'
    def len(self):
        return self.x+self.y



first=Rectangle(5,7)
second=Rectangle(3,9)
print(first.area())
print(first.comparePlus(second))
print(first.compareMinus(second))
print(first.compareDifference(second))
print(first.compareEqually(second))
print(first.compareBig(second))
print(first.len())

#
#
# ######################################################################
#
# 1)Створити пустий list
list=[]
# 2)Створити клас Letter
# 3) створити змінну класу __count.
# 4) при створенні об'єкта має створюватись змінна об'єкта(пропертя) __text, для цієї змінної мають бути гетер і сетер
# 5) при створені об'єкта __count має збільшуватися на 1
# 6) має бути метод(метод класу) для виводу __сount
# 7) має бути метод який записує в наш ліст текст з нашої змінної __text

class Letter:
    __count = 0
    def __init__(self, text):
        self.__text = text
        self.__count=self.__count+1

    @property
    def text(self):
        return self.__text
    @text.setter
    def text(self, text):
        self.__text = text
    @text.deleter
    def text(self):
        del self.__text

    def __repr__(self):
         return f'{self.__text}'
    def count(self):
        return self.__count
    def pushInList(self, list):
        list.append(self)


hello=Letter('Hello')
hi=Letter('Hi')
print(hello)
print(hello.count())
hello.pushInList(list)
hi.pushInList(list)
print(list)
