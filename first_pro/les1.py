# 1)Дан лист:
l = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
#  # - найти min число в листе
# l.sort()
# print(l[0])
#
# # - удалить все одинаковые значения
# newL=set(l)
# print(newL)
#
# # - заменить каждое четвертое значение на "Х"
# mas=[]
# i=1
# for  list in l:
#      if i%4 == 0 :
#          list='X'
#      i+=1
#      mas.append(list)
# print(mas)
#
#
# # - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
#
# new=[]
# for list in l:
#    new.append(abs(list-sum(l)/ len(l)))
# ind =new.index(min(new))
# print(l[ind])
#
# # пример:
# # [1, 2, 3, 4, 5, 6, 7, 8, 9] = > 5
# # [-1, -2, 3, 4, 555] = > 4
# # [5, 5, 5, 5] = > 5
# # [-10, 5, 5] = > 5
# # P.S.Функция len() также используется для листов
#
#
# #
# #
# # # 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:
# hight=5
# width=10
#
# for i in range(hight):
#     if i==0 or i==hight-1:
#         for j in range(width):
#             print('*',end=" ")
#     else:
#         print('*', end=" ")
#         for j in range(1, width-1):
#             print(' ', end=" ")
#         print('*', end=" ")
#     print()
# #
# # 3) переделать первое задание под меню с помощью цикла
#

m = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

while True:
    num = input("Выберите номер: \n 1.найти min число в листе \n 2.удалить все одинаковые значения "
                "\n 3.заменить каждое четвертое значение на 'Х' \n 4.вывести элемент листа, значение которого ближе всего к среднему арифметическому"
                " \n 5.Выход \n Ввод: ")

    if num =='1':
        m.sort()
        print(m[0])

    if num == '2':
        newL = set(l)
        print(newL)
    if num == '3':
        mas = []
        i=1
        for  list in l:
             if i%4 == 0 :
                 list='X'
             i+=1
             mas.append(list)
        print(mas)
    if num == '4':
        new = []
        for list in l:
           new.append(abs(list-sum(l)/ len(l)))
        ind =new.index(min(new))
        print(l[ind])
    if num =='5':
        break




# # 4) вывести табличку умножения с помощью цикла while
#
# a =1
# while a<=10:
#     b=1
#     while b<=10:
#         rez=a*b
#         print(rez, end=" ")
#         b+=1
#     print(' ')
#     a+=1
