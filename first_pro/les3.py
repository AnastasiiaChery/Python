# - створити функцію  яка  виводить  ліст - створити функцію  яка приймає три числа та виводить  та  повертає  найменьше.
def funcNumMin(a, b, c):
    print(min(a,b, c))
    return min(a,b, c)
print(funcNumMin(2, -7, 12))

# - створити  функцію яка приймає три  числа та виводить та повертає найбільше.
def funcNumMax(a, b, c):
    print(max(a,b, c))
    return max(a,b, c)
print(funcNumMax(2, -7, 12))

# - створити функцію яка приймає будь - яку кількість чисел, повертає найменьше, а виводить найбільше
def funcNumMaxMin(*args):
    print(max(*args))
    return min(args)
print(funcNumMaxMin(2, -7, 12, 8, 65, -32))
# - створити функцію яка виводить ліст
list=[12, 5,-3, 7, 34, 9,-4, 7, -6, 90,6]
def funcList ():
    print( *list)
funcList()
# - створити функцію яка повертає найбільше число  з ліста
def funcMax ():
    return max(*list)
print(funcMax())
# - створити функцію яка повертає найменьше число з ліста
def funcMin ():
    return min(*list)
print(funcMin())
# - створити функцію  яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def funcSum(l):
    numbers_sum = sum(l)
    return numbers_sum
print(funcSum(list))
# - створити функцію яка приймає ліст чисел  та повертає середнє арифметичне його значень.
def funcAvg(l):
    numbers_avg = sum(l)/len(l)
    return numbers_avg
print(funcAvg(list))
# - є  функція: написати декоратор до цієї функції, який замінює нижні підчеркування  на пробіли  і повертає це значення

def decor(func):
    def wrap():
        return func().replace('_', ' ')

    return wrap

@decor
def pr():
    return 'Hello_boss_!!!'

print(pr())
