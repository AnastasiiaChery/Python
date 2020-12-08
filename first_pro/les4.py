# создать класс Human и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и  метод который принимает лист золушек и выводит какой золушки подошла туфелька

class Human:
    def __init__(self, age, name):
         self.age = age
         self.name = name

class Prince(Human):
    def __init__(self, age, name, size):
          super().__init__(age, name)
          self.size = size
    def __repr__(self):
         return f'{self.age} -- {self.name}--{self.size}  '

    def choseCind(self):
        for i in instances:

            if i.sizeFood == self.size:
                return 'you chose 'f'{i.name}'



instances = []
def decor(cls):
    def wrap(*args, **kwargs):
        obj = cls(*args, **kwargs)
        instances.append(obj)
        return obj
    return wrap

@decor
class Cinderella(Human):

    def __init__(self, age, name, sizeFood):
        super().__init__(age, name)
        self.sizeFood = sizeFood
    def __repr__(self):
         return f'{self.age} -- {self.name}--{self.sizeFood}  '





cind1=Cinderella(18, 'Sharlota', 36)
cind2=Cinderella(15, 'Luiza', 35)
cind3=Cinderella(16, 'Emily', 41)
cind4=Cinderella(17, 'Anna', 38)
cind5=Cinderella(17, 'Anastasia', 36)
cind6=Cinderella(18, 'Lily', 38)

prince=Prince(22,'Charming', 35)



# print(instances[1].name)
print(prince.choseCind())