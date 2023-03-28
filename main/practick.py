    
# lst_field = []
# for _ in range(3):
#     lst_field.append([-1, -1, -1])

# typet_X = True
# typet_O = False
# attept = False

# which = input('X or O: ').upper()
# if which == 'X' or which == 'O':
#     if which == 'X' or which == 'O':
#         while attept != True:
#             for i in range(3):
#                 for j in range(3):
#                     if lst_field[i][j] == -1:
#                         print('-', end=' ')
#                     elif lst_field[i][j] == 0:
#                         print('O', end=' ')
#                     else:
#                         print('X', end=' ')
#                 print()
#             choice = input('\nEnter ROW and COL: ').split()
            
#             if len(choice) == 2:
#                 for v in choice:
#                     if not(v.isdigit()) or int(v) not in range(3):
#                         print('Invalid number')
#                         break
                    
#                 else:
                    
#                     if which == 'X':
#                         if lst_field[int(choice[0])][int(choice[1])] == -1:
#                             lst_field[int(choice[0])][int(choice[1])] = int(typet_X)
#                             typet_X = not typet_X
#                         else:
#                             print('Its not possible')

#                     elif which == 'O':
#                         if lst_field[int(choice[0])][int(choice[1])] == -1:
#                             lst_field[int(choice[0])][int(choice[1])] = int(typet_O)
#                             typet_O = not typet_O
#                         else:
#                             print('Its not possible')


#                         for i in range(3):
                            
#                             if lst_field[i][0] == lst_field[i][1] == lst_field[i][2] and lst_field[i][2] != -1:
#                                 print('Winn!')

#                                 aiu = input('yes or no: ')
#                                 if aiu == 'yes':
#                                     lst_field = []
#                                     for _ in range(3):
#                                         lst_field.append([-1, -1, -1])
#                                     which = input('X or O: ').upper()
#                                     typet_O = False
#                                     typet_X = True

#                                 else:
#                                     attept = True
                                        

#                             elif lst_field[0][i] == lst_field[1][i] == lst_field[2][i] and lst_field[2][i] != -1:
#                                 print('Winn!')

#                                 aiu = input('yes or no: ')
#                                 if aiu == 'yes':
#                                     lst_field = []
#                                     for _ in range(3):
#                                         lst_field.append([-1, -1, -1])
#                                     which = input('X or O: ').upper()
#                                     typet_O = False
#                                     typet_X = True

#                                 else:
#                                     attept = True

#                         else:
#                             if lst_field[0][0] == lst_field[1][1] == lst_field[2][2] or \
#                                     lst_field[0][2] == lst_field[1][1] == lst_field[2][0] and lst_field[1][1] != -1:
#                                 print('Winn!')

#                                 aiu = input('yes or no: ')
#                                 if aiu == 'yes':
#                                     lst_field = []
#                                     for _ in range(3):
#                                         lst_field.append([-1, -1, -1])
#                                     which = input('X or O: ').upper()
#                                     typet_O = False
#                                     typet_X = True
                                    
#                                 else:
#                                     attept = True
                        
#                             if lst_field[0][0] != -1 and lst_field[1][1] != -1 and lst_field[2][2] != -1 and  \
#                                     lst_field[0][2] != -1 and  lst_field[1][1] != -1 and lst_field[2][0] != -1 and \
#                                         lst_field[0][i] != -1 and lst_field[1][i] != -1 and lst_field[2][i] != -1 and \
#                                             lst_field[i][0] != -1 and lst_field[i][1] != -1 and lst_field[i][2] != -1:
                                
#                                 print('Draw!')

#                                 aiu = input('yes or no: ')
#                                 if aiu == 'yes':
#                                     lst_field = []
#                                     for _ in range(3):
#                                         lst_field.append([-1, -1, -1])
#                                     which = input('X or O: ').upper()
#                                     typet_O = False
#                                     typet_X = True

#                                 else:
#                                     attept = True
#             else:
#                 print('Enter 2 values')
# print('Use X or O')
    
    
    
    
    ########### TUPLES

# name = input('Enter name: ').split()
# for i in name:
#     if 'po' in i and i.islower():
#         all = ' '.join(name)
# print(all)

    #####

# t = ((1, 0, 0, 0, 0),
#     (0, 1, 0, 0, 0),
#     (0, 0, 1, 0, 0), 
#     (0, 0, 0, 1, 0), 
#     (0, 0, 0, 0, 1))

# num = int(input('Enter num: '))
# if num <= 5:
#     j = t[:num]
#     for i in j:
#         h = i[:num]
#         print(h)
# else:
#     print('Incorect data')

    #####

# all_tuple = tuple(int(val) for val in input('Enter num: ').split())
# for i, val in enumerate(all_tuple):
#     if all_tuple.count(val) > 1:
#         print(i, end=' ')
    
    
    
    
    ######### DICT 

# dicT = {
#     ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'):1,
#     ('D', 'G'):2,
#     ('B', 'C', 'M', 'P'):3,
#     ('F', 'H', 'V', 'W', 'Y'):4,
#     'K':5,
#     ('J', 'X'):8,
#     ('Q', 'Z'):10
# }
# lis = []
# eny = input('Enter: ').upper()
# for u in eny:
#     for i in dicT:
#         if u in i:
#             h = dicT[i]
#             lis.append(h)
# print(sum(lis))

    #####

# dicT = {
#     'eny':['bob', 'to'],
#     'фрукти':['полуниця', 'малина', 'яблуко', 'банан'],
#     'морепродукти':['кальмар', 'краб', 'креветки', 'мідії'],
#     'випічка':['бісквіт', 'безе', 'печиво', 'млинці']
# }

# product = input('Enter product: ')

# listKey = [key for key, val in dicT.items() if product in val]
# if listKey:
#     print(*listKey)
# else:
#     print('Інше')

    #####

# cities = ['london', 'New York', 'Tokyo', 'cambridge', 'Oxford']
# countries = ['uK', 'US', 'Japan', 'uK', 'UK']
# uk_cities = {city.capitalize(): country.upper() for city, country in zip(cities, countries) if country in ('UK', 'uK')}
# print(uk_cities)##{'London': 'UK', 'Cambridge': 'UK', 'Oxford': 'UK'}

    ##### dict of dicts

# import json
# print(json.dumps({'a':2, 'b':{'x':3, 'y':{'t1': 4, 't2':5}}}, sort_keys=True, indent=4))

    #####

# myDict5 = dict(['qw', 'er', 'ty'])
# print(myDict5)  #{'q': 'w', 'e': 'r', 't': 'y'}

    #####

# keyList=['a','b']
# valueList=[111,222]
# myDict6=dict(zip(keyList,valueList))
# print(myDict6)  #{'a': 111, 'b': 222}

    #####

# myDict7=dict(firstName='Joe', lastName='Smith')
# print(myDict7)  #{'firstName': 'Joe', 'lastName': 'Smith'}




    ########## PLURAL

# num = 0
# attepmt = True
# plural = set()
# while attepmt != False:
#     product = input('Enter products: ').split()# можна вводити в рядок через пробіл або й з нової стрічки
#     for i in product:
#         if '.' not in i:
#             plural.add(i)
#             continue
#         else:
#             for indX, val in enumerate(plural):
#                 n=1
#                 num+=n
#             print(num)
#             attepmt = False

    #####

# work_test = {'Andey', 'Oleg', 'Danil'}
# work_real = {'Oleg', 'Danil', 'Tom', 'Jeck'}
# person = input('Enter person: ').capitalize()

# if person in work_test or person in work_real:
#     all = work_test & work_real# intersection changed to &
#     diff_all = work_test ^ work_real# symmetric_difference changed to ^
#     diff = work_test - work_real# difference changed to -
#     print('Visited all works:', ', '.join(all))
#     print('Visited one work:', ', '.join(diff_all))
#     print('Visited one work:', ', '.join(diff))
# else:
#     print(f'{person} - not visited')


    #####frozenset(), select only unical element from Tuple

# tupl = (3, 4, 4, True, 'nother')
# froz = frozenset(tupl)
# print(*froz)



    ########## FUNCTION
    

# import calendar
# def cale():
#     month = input('Enter num: ')
#     if month.isdigit() and 1 <= int(month) <= 12:
#         range = calendar.monthrange(2023, month)
#         name = calendar.month_name[int(month)]
#         print(f'In {calendar.month_name[int(month)]} we got {calendar.monthrange(2023, month)[1]} days')
#     else:
#         print('Incorect data!')
    
# cale()


    ######

# def mass(product, mass):
#     print(f'Weight product: {product} : {mass}')
# mass(input('Enter product: '), float(input('Weight: ')))

    #####

# def math(lst):
#     print(f'MIN = {min(lst)}; MAX = {max(lst)}; SUMM = {sum(lst)}')
# math([n for n in int(input('List numbers: ').split())])
    

    #####

# def math(width, height):
#     width_side = width*2
#     height_side = height*2
#     res = width_side + height_side
#     print(f'Периметр прямокутника зі сторонами: {width_side} і {height_side} = {res}')
# math(20, 10)

    #####
    
# def txt(text):
#     if len(text) < 10:
#         return True
#     else:
#         return False
# print(txt(input('Enter text: ')))

    #####

# import calendar
# def cale(data):
#     if data.isdigit() and 1 <= int(data) <= 12:
#         range = calendar.monthrange(2023, int(data))
#         name = calendar.month_name[int(data)]
#         print(f'In {calendar.month_name[int(data)]} we got {calendar.monthrange(2023, int(data))[1]} days')
#     else:
#         print('Incorect data!')
    
# cale(input('Enter num: '))


    #####

# def math(num, next_num):
#     return num**next_num
        

# def format_big_name(num):
#     for i in num:
#         str(i)


# res = math(2, 4)

# format_big_name(res)

    #####

# def make(num1, num2):
#     return num1 if num1<num2 else num2

# num1 = int(input('Num_1: '))
# num2 = int(input('Num_2: '))
# num3 = int(input('Num_3: '))
# res = make(num1, num2)
# print(res)

    #####

# def math(num):
#     return [num[el:el+3] for el in range(0, len(num), 3)]
# print(*math(int(input('Enter numbers: '))))

    #####

# def truc(side1, side2, side3):
#     if side3 < side1 + side2 and side3 == side1:
#         return True
#     else:
#         return False
# res = truc(3, 4, 3)
# print(res)

    #####

# a = 2, 4
# print([range(*a)])
# print([*range(*a)])
# print(*[*range(*a)])

    #####

# *lst, a, b, c = [int(val) for val in input('Enter: ').split()]
# print(*lst)
# print(a)
# print(b)
# print(c)

    #####

# lst_nums = [int(val) for val in input('Enter: ').split()]
# lst_words = input('Enter: ').split()

# res = [*lst_words, *lst_nums]
# print(res)

    #####

# def fun(age, name):
#     print(age, name)
# fun(19, name='Tom')

    #####


# def func(x, y, operation=False):
#     if operation:
#         return x+y
#     return x-y
# print(func(7, 5))

    #####

# def func(num, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(num)
#     return lst

# print(func(5, [10, 15]))


    #####

# def math(num):
#     return [num[el:el+3] for el in range(0, len(num), 3)]
# print(*math(int(input('Enter numbers: '))))

    #####

# def make(num1, num2):
#     return num1 if num1<num2 else num2

# num1 = int(input('Num_1: '))
# num2 = int(input('Num_2: '))
# num3 = int(input('Num_3: '))
# print(min(make(num1, num2), num3))

    #####
    
# x = 0
# def outher():
#     x = 1
#     def inner():
#         nonlocal x
#         print(x)
#         x = 3
#         print(f'INNER = {x}')
#     inner()
#     print(f'OUTHER = {x}')

# outher()
# print(f'GLOBAL = {x}')

    #####

# def lst_eny(num):
#     return max(num, key=len)
# print(lst_eny(input('Enter eny: ').split()))

    #####

# x = lambda a, b: a+b
# print(x(3, 5))

# if lambda: 3+2<2:
#     print('ok')

# a = [lambda: print(input(''))]

    #####

# def get_filter(data, filter, lst=None):
#     if lst is None:
#         lst=[]

#     for value in data:
#         if filter(value):
#             lst.append(value)
#     return lst

# a = [3, 8, -2, 6, 10, -1]
# print(get_filter(a, lambda num: num % 2 == 0))
# get_filter(a, lambda num: num > 5)

    #####

# x = lambda n:n**2
# print(x(2))

    #####

# n = lambda x, y: x/y if y else None
# print(n(4, 2))

    #####

# l = lambda num, x: round(num, x)
# print(l(3.454545, 2))

    #####

# l = lambda txt: True if 'or' in txt else False
# print(l('topor'))

    #####

# lst=[5, 7, 2, 3, 1, 8]

# do_it = list(filter(lambda x: x % 2 == 0, lst))
# print(do_it)

    #####

# lst=[5, 7, 2, 3, 1, 8]

# do_it = list(map(lambda x: x**2, lst))
# print(do_it)




    ########## RECURSION

# def num(n):
#     if n > 1:
#         num(n-1)
#     print(n)
# num(7)

    #####

# def rec(num):
#     if num >= 10:
#         rec(num//10)
#     print(num%10)
# rec(234)

    #####

# def slice(num):
    
#     if num <= 10:
#         return num
#     return num % 10 + slice(num//10)

# print(slice(456))

    #####

# def rec(num):
#     if num == 1:
#         return 1
#     return rec(num - 1) * num

# print(rec(5))

    #####

# def str_txt(lst_txt, lamb, lst=None):
#     if lst is None:
#         lst = []

#     for i in lst_txt:
#         if lamb(i):
#             lst.append(i)
#     return lst

# txt = ['allan', 'car', 'air', 'bus', 'gogan']
# print(str_txt(txt, lambda opt: opt if len(opt) == 5 and 'an' in opt else False))

    #####

# def palindrom(txt):
#     if len(txt)<=1:
#         return True

#     if txt[0] != txt[-1]:
#         return False
#     return palindrom(txt[1:-1])
    
# print(palindrom('golog'))

    #####

# def do_rec(txt):
#     if len(txt) == 1 or len(txt) == 2:
#         return txt
#     return txt[0] + '(' + do_rec(txt[1:-1]) + ')' + txt[-1]
# print(do_rec(input('Enter text: ')))

    #####

# def rec(num):
#     if num < 10:
#         return [num]
#     return rec(num//10)+[num%10]
# print(rec(int(input('Enter num: '))))

    #####

# def rec(num, lst=[]):
#     for el in num:
#         if type(el) is list:
#             rec(el)
#         else:
#             lst.append(el)
#     return lst

# data = [26, -3, ['Hello', False], [True, "Bye", [200.1, 45.12], ['recursion', [777, -321]]], 'i`m last element ;D']
# print(rec(data))



    ########## CLOSURE

# gl = 'global'

# def outer(text):
#     def inner():
#         print(text, gl)
#     return inner

# x = outer('hello')
# x()

    #####

# def counter(count=0):
#     def tick():
#         nonlocal count
#         count += 1
#         return count
#     return tick

# c_1 = counter(5)
# print(c_1())
# print(c_1())

    #####

# def add_10():
#     def do_it(num):
#         return num+10

#     return do_it

# print(add_10()(5))

    #####

# def add_10():
#     return lambda num: num+10

# print(add_10()(5))

    #####

# def teg(tegs):
#     return lambda txt: '<'+tegs+'>'+txt+'</'+tegs+'>'

# x = teg(input('Type Teg: ')) (input('Text: '))
# print(x)

    #####

# def locking(txt):
#     return lambda num: list(num) if type(txt) == list else tuple(num)

# x = locking(input('Text: ')) (int(n) for n in input('Num: ').split())
# print(x)

    #####

# def main(x):
#     def next(y):
#         return x+y
#     return next
# print(main(10)(5))

    #####

# def main(x):
#     return lambda y: x+y
# print(main(10)(5))

    #####

# def outer(lst=[]):
#     def inner(n):
#         lst.append(n)
#         return lst
#     return inner

# x = outer([])
# x(7)
# x(2)
# print(x(1))




    ########### DECORATOR


# def func_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('DO BEGIN')
#         res = func(*args)
#         print('DO AFTER')
#         return res 
#     return wrapper

# @func_decorator
# def my_print(text, *args, **kwargs):
#     print(f'THIS IS YOUR TEXT = {text}, else fargs')
#     return 'new text ' + text

# a = my_print('abc','dfsdf', 234234, 23424234)
# print(a)

# def decorator_math(func):
#     def main(*args):
#         return f'Rectangle square = {func(*args)}'
#     return main


# @decorator_math
# def get_rec_square(width, height):
#     return width*height

# print(get_rec_square(10, 20))

    #####

# def decorator(func):
#     def main(*args):
#         for num, val in enumerate(func(*args), 1):
#             print(num, val)
#     return main


# @decorator
# def product(txt):
#     return txt.split()

# print(product(input('Enter product: ')))

    #####

# def decorator(func):
#     def main(*args):
#         return sorted(func(*args))
#     return main

# @decorator
# def convert_to_list(num):
#     return [int(n) for n in num.split()]
#     """doc"""
# print(convert_to_list(input('Enter numbers: ')).__doc__)
# print(convert_to_list(input('Enter numbers: ')).__name__)

    #####

# def dec(name):
#     def wrapper(func):
#         def inside(*args):
#             print(f'{name} = {sum(func(*args))}')
#         return inside
#     return wrapper


# def convert_to_list(num):
#     return [int(n) for n in num.split()]

# a = dec('txt')(convert_to_list)
# a(input('num: '))

    #####

# def do_elements(func):
#     def main(nums, stri):
#         set_num = {}
#         for i, l in zip(nums, stri):
#             set_num.setdefault(i, l)
#         return set_num
#     return main


# @do_elements
# def elements(nums, stri):
#     return f'{nums}{stri}'

# print(elements('1 2 3 4 5'.split(), 'one two three four five'.split()))

    #####

# def decor_for_teg(func):
#     def main(text):
#         def nexte(tag='h3'):
#             return f'<{tag}>{text}</{tag}>'
#         return nexte()
#     return main

    

# @decor_for_teg
# def teg_txt(txt):
#     return txt.lower()
# print(teg_txt(input('Text: ')))



    ########### CURRYING 

# def outer(func): 
#     def f1(a):
#         def f2(b):
#             func(a, b)
#         return f2
#     return f1

# def my_p(a, b):
#     print(a, b)

# outer(my_p)('Helo')('World')

    #####

# def outer(func): 
#     def names(name):
#         def ages(age):
#             return func(name, age)

#         return ages
#     return names


# def my_p(name, age):
#     return f'{name}{age}'

# print(outer(my_p)(input('name: '))(input('age: ')))

    #####


# def outer(func): 
#     def names(num1):
#         def ages(num2):
#             return func(num1, num2)

#         return ages
#     return names


# def my_p(num1, num2):

#     return num1**2 + 2*num1*num2 + num2**2

# print(outer(my_p)(int(input('num: ')))(int(input('num: '))))

    #####

# from functools import partial

# def my_p(num1, num2):
#     return num1**2 + 2*num1*num2 + num2**2

# x = partial(my_p, num1=2, num2=5)
# print(x())

    #####

# from functools import partial
# lst=[]
# def main_func(names, *args):
#     dic = {}
#     for i in args: alls = ', '.join(args)
#     dic.setdefault(names, alls)
#     lst.append(dic)
#     return lst

# res = partial(main_func, input('Country: '), input('Capital: '), input('People: '))
# print(res())
# t = partial(main_func, input('Country: '), input('Capital: '), input('People: '))
# print(t())



    ############ MAP, FILTER, ZIP, REDUCE


# res = list(map(lambda x: x+ 'a', 'hello'))

# for _ in range(5):
#     print(next(res))

# lst = iter([1, 2, 3])
# print(lst)

    #####

# res = map(float, input().split())
# for _ in range(2): print(next(res))
# print(res)

    #####

# num = input('Nums: ').split()
# print(list(map(lambda x: abs(int(x)), num)))  

    #####

# alls = input('Key:value ')
# print(tuple(map(lambda val: tuple(val.split('=')), alls.split())))

    #####

# city = input('City: ').split()
# res = filter(lambda x: len(x)>5, city)
# print(*[next(res) for _ in range(2)])

    #####

# nums = '2 43 7 2323 98 -23'
# res = list(filter(lambda n: len(n)==2 and abs((int(n))), nums.split()))
# print(res)

    #####

# names = iter(input('Name: ').split())
# res_name = list(map(lambda x: x if len(x)>3 else '*', names))
# print(*res_name)

    #####

# lst_num = ['a=300', 'b=600', 'c=750', 'e=500', 'f=130']
# res_num = tuple(map(lambda x: tuple(x.split('=')), lst_num))
# res = ''
# for i in res_num:
#     fil = list(filter(lambda n: n[0] if int(n[-1])<500 else None, res_num))
# for l in fil:
#     res += l[0]
            
# print(', '.join(res))

    #####

# nums = iter(input('Nums: ').split())
# res_nums = list(filter(lambda x: x if len(x)==2 else None, nums))
# print(*res_nums)

    #####

# from functools import reduce

# num = input('Num: ').split()
# sum_el = reduce(lambda x, y: x+y, num)
# print(sum_el)

    #####

# a = [1, 2, 3, 4]
# b = [3, 6, 5]
# res = list(zip(a, b))
# print(res)

    #####

# a = [1, 2, 3, 4]
# b = [2, 3, 4, 5, 7]
# res = list(map(lambda x: x[0]*x[1], zip(a, b)))
# print(res)
    
    #####

# a = [1, 2, 3, 4]
# b = [6, 7, 8, 5, 7]
# c = [10, 11, 15, 22]
# d = [5, 10, 13]

# res = zip(a, b, c, d)

# for v in zip(*res):
#     print(*v)

    #####

# from functools import reduce
# res = reduce(lambda t, x: t+' '+x, input('txt: ').split())
# print(res)

    #####

# from functools import reduce
# print(reduce(lambda x, y: x*y, range(1, int(input('Num: '))+1)))

    #####



# from functools import reduce

# noth = zip(range(1, 4), range(4, 7))
# for i in zip(*noth):
#     print(reduce(lambda x, y: x+y, i))

    #####


# from random import choice

# lst = ['океан', 'листя', 'вітер']

# def check_word_decorator(func):
#     hist=[]

#     def wrapper(*args, **kwargs):
#         nonlocal hist
#         if kwargs['answer'] in hist:
#             return True
#         hist += [kwargs['answer']]
#         if func(*args, **kwargs):
#             return kwargs['answer']
#         return False

#     return wrapper

# @check_word_decorator
# def check_word(guess, answer, *args, **kwargs):
#     if guess == answer:
#         return lst
#     return False


# def translate_decorator(func):
#     tries = dict()
#     def wrapper(answer, guess):
#         nonlocal tries
#         text=''
#         tries[' '.join(answer)]=guess
#         print(answer)
#         for i in zip(answer, guess):
#             if i[0]==i[1]:
#                 text+='+'
#             elif i[0] in guess:
#                 text+='*'
#             else:
#                 text+=' '
#         tries[' '.join(answer)]=' '.join(text)
#         for k, v in tries.items():
#             print(f'\n\t{k}')
#             print(f'\t{v}')

#     return wrapper

# @translate_decorator
# def translate(answer, guess):
#     return answer.lower()



# lives = 6
# rand_word = choice(lst)
# while lives > 0:
#     print(rand_word)
#     user_answer = input('Введіть слово: ')
#     if len(user_answer) == 5:
#         res = check_word(guess=rand_word, answer=user_answer)
#     else:
#         print(f'\n\tДовжина слова не рівна 5 символам\n')
#         continue

#     if type(res) is not bool:
#         lst.remove(res)
#         translate(user_answer, rand_word)
#         print('\n\t'+'Перемога!\n')
#         break

#     elif res:
#         print(f'\n\tВи вже вводили слово {user_answer}\n')
#         continue
#     translate(user_answer, rand_word)
#     lives -= 1
#     print(f'\n\tУ вас залишилось {lives} життів!\n')


    #####

# lst_month = ['січень', 'лютий', 'березень', 'квітень', 'травень', 'червень', 'липень', 'серпень', 'вересень', 'жовтень', 'листопад', 'грудень']
# lst_salary = [12234, 55432, 876123, 993245, 12324, 328753, 875643, 123465, 8845322, 875634, 98213, 195534]
# zipo = list(zip(lst_month, lst_salary))
# for i, _ in enumerate(zipo, 1):
#     print(i)
#     for n in zipo[:3]:
#         fil = list(map(lambda x: x, n))
#         print(*fil)
    

    #####

# lst_abc = ['a', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 
#     'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я', ' ']

# lst_rand = ['н', 'ж', 'п', 'й', 'ч', 'в', 'a', 'б', 'с', 'г', 'ґ', 'д', 'ь', 'і', 'е', 'ф', 'ю', 'и', 'х', 'щ', 'ш', 
# 'л', 'т', 'ц', 'о', 'з', 'к', 'л', 'у', 'є', 'ї', ' ', 'р', 'м']
# res = ''
# quest = input('Шифр/Розшифр: ').lower()
# if quest == 'шифр':
#     txt = input('Your text: ')
#     for orig, noth in zip(lst_abc, lst_rand):
#         if orig in txt:
#             res+=noth
#     print(res)
# else:
#     txt = input('Your text: ')
#     for orig, noth in zip(lst_abc, lst_rand):
#         if noth in txt:
#             res+=orig
#     print(res)


    #####

# from functools import reduce
# eny = input('Text: ').split()
# for i in eny:
#     print(reduce(lambda num1, num2: num1+1, range(len(i)+1)))





    ################# RANDOM GENERATORS


# from random import randint

# def generate_lst():
#     l = []
#     for _ in range(21):
#         while True:
#             rand_num = randint(-10, 10)
#             if rand_num not in l:
#                 l.append(rand_num)
#                 break
#     return l

# lis = generate_lst()
# print(lis)
# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(1, len(lst)-i):
#             if lst[j-1] > lst[j]:
#                 lst[j-1], lst[j] = lst[j], lst[j-1]

#     return lst

# print(bubble_sort(lis))


    #####

# from random import randint

# def generate_lst():
#     l = []
#     for _ in range(21):
#         while True:
#             rand_num = randint(-10, 10)
#             if rand_num not in l:
#                 l.append(rand_num)
#                 break
#     return l

# lis = generate_lst()
# print(lis)
# def selection_sort(lst):
#     for i in range(len(lst)-1):
#         min = i
#         for j in range(i+1, len(lst)):
#             if lst[j] < lst[min]:
#                 min = j
#         lst[i], lst[min] = lst[min], lst[i]

#     return lst

# print(selection_sort(lis))


    #####

# def shell_sort(lst):
#     n = len(lst)//2
#     while n > 0:
#         for i in range(n, len(lst)) :
#             current_val = lst[i]
#             position = i
#             while position >= n and lst[position-n] > current_val:
#                 lst[position] = lst[position-n]
#                 position -= n
#                 lst[position] = current_val
#         n //= 2
#     return lst

# lst=[7, 1, 23, 13, 4, 2, 0]
# print(shell_sort(lst))


    #####

# def binary_seach(lst, el):
#     begin = 0
#     last = len(lst)+1

#     while begin <= last:
#         mid = (begin+last)//2
#         if lst[mid] == el:
#             return mid
#         elif el > lst[mid]:
#             begin = mid+1
#         else:
#             last = mid-1
#     return None

# x = [-3, 4, 6, -2, 6, 12, 8]
# print(binary_seach(x, int(input('element: '))))





    #################### TRY, EXCEPT, FINALLY


# try:
#     num = int(input('Nums: '))
# except ValueError:
#     print('Incorect data')


    #####

# while True:
#     try:
#         num = int(input('Nums: '))
#     except ValueError:
#         print('Incorect data')
#     else:
#         print(num)


    #####

# lst = ['hello', 'ps', False, 15, 18, True, 'tomas']
# while True:
#     try:
#         inde = int(input('Nums: '))
#         print(lst[0:inde+1])
#         break
#     except (IndexError, ValueError):
#         print('Incorect data')


    #####

# lst = ['hello', 'ps', False, 15, 18, True, 'tomas']
# while True:
#     try:
#         try:
#             inde = int(input('Nums: '))
#             print(lst[inde])
#             break
#         except IndexError:
#             print('incorect index')
#     except ValueError:
#         print('incorect value')
        






    ################### FILES

# file = open('/Users/danil/Documents/work_py/main/text.txt')
# res_1 = file.read()
# res_2 = file.readline()
# res_3 = file.readlines()
# print(res_2, ende='')

    #####

# file = open('/Users/danil/Documents/work_py/main/text.txt')
# file.readline()
# res_1 = file.tell()
# print(res_1)

    #####

# file = open('/Users/danil/Documents/work_py/main/text.txt')
# res_1 = file.seek()
# print(res_1)

    #####

# try:
#     with open('/Users/danil/Documents/work_py/main/text.txt') as file:
#         res = file.read()
#         try:
#             print(int(res))
#         except ValueError:
#             print('file data not a numeric')
# except FileNotFoundError:
#     print('Not found')


    #####

# try:
#     with open('/Users/danil/Documents/work_py/main/text.txt') as file:
#         country = file.readline()
#         capital = file.readline()
#         populations = file.readline()
#         print(country, capital, populations)
# except FileNotFoundError:
#     print('not found file')

    #####

# try:
#     with open('/Users/danil/Documents/work_py/main/f.txt') as file:
#         data = tuple()
#         for value in file.read().split('\n\n'):
#             res = value.split('\n')
#             data += ({
#                 'country': res[0],
#                 'capital': res[1],
#                 'population': float(res[2]),
#                 'neighbors':
#                 res[3].split()
#             }, )
# except FileNotFoundError:
#     print ('File not found' )


    #####

# data = dict()
# def read_file():
#     try:
#         with open('/Users/danil/Documents/work_py/main/event_info.txt') as file:
#             try:
#                 for value in file.read().split('\n'):
#                     value.split()
#                     k, v = value.split('=')
#                     data[int(k)]=v
#             except ValueError:
#                 print('file empty')
#             finally:
#                 return data

#     except FileNotFoundError:
#         with open('/Users/danil/Documents/work_py/main/event_info.txt', 'w') as file:
#             file.write('')

# def write_file(collection):
#     for val in read_file():
#         pass
#     return collection

# lst=[]
# write = write_file(lst)
# print(write)


# def free_tables(specefication, event_data):
#     all_tables=[]
#     for value in specefication.values():
#         for num in value:
#             lst.append(num)
#     all_tables.sort()
#     for table in all_tables:
#         if table not in event_data.keys():
#             print(table)

    
# spaceReadGood = False
# try:
#     with open('/Users/danil/Documents/work_py/main/place_specification.txt') as file:
#         spec = dict()
#         for value in file.read().split('\n\n'):
#             value.split()
#             k, v = value.split()
#             spec[int(k)] = [int(value) for value in v.split(',')]
#         spaceReadGood = True
# except FileNotFoundError:
#     print('Not found file')

# file_data = read_file()
# print(file_data)
# while spaceReadGood:
#     try:
#         menu_choice = int(input('1, 2, 3, 4, 5, 0: '))
#     except ValueError:
#         print('Use only numbers for menu')
#         continue
#     if 0 <= menu_choice <= 5:

#         if menu_choice == 0:
#             exit()
#         elif menu_choice == 1:
#             print(write)
#         elif menu_choice == 2:
#             pass
#         elif menu_choice == 3:
#             pass
#         elif menu_choice == 4:
#             free_tables(specefication=spec, event_data=data)
#         elif menu_choice == 5:
#             pass


    #####

# try:
#     with open('/Users/danil/Documents/work_py/main/auto.txt') as file:
#         list_avto=[]
#         list_avto.append(file.read())
#         print(*list_avto)
# except FileNotFoundError:
#     print('not found file')

    #####

# import pickle

# dic = {
#     1:'pip', 
#     2:'bus', 
#     3:'loop'
# }
# with open('/Users/danil/Documents/work_py/main/txt.bin', 'wb') as file:
#     pickle.dump(dic, file)
# with open('/Users/danil/Documents/work_py/main/txt.bin', 'rb') as file:
#     for k, v in pickle.load(file).items():
#         print(k, v)


    #####

# import pickle
# lst = [1, 2, 4, 7, 9]
# with open('/Users/danil/Documents/work_py/main/txt.bin', 'wb') as file:
#     pickle.dump(lst, file)

# with open('/Users/danil/Documents/work_py/main/txt.bin', 'rb') as file:
#     res = list(filter(lambda x: x<10, pickle.load(file)))
# print(res)



    #######

# from random import randint
# import pickle

# def num_validation(num):
#     if user1 <= 0 or user1 > 100:
#         return True
#     return False

# rand = randint(1, 100)

# try:
#     with open('/Users/danil/Documents/work_py/main/txt.bin', 'rb') as file:
#         data = pickle.load(file)
# except FileNotFoundError:
#     with open('/Users/danil/Documents/work_py/main/txt.bin', 'wb') as file:
#         pickle.dump({
#             'round':1,
#         }, file)
#     with open('/Users/danil/Documents/work_py/main/txt.bin', 'rb') as file:
#         data = pickle.load(file)



# def game_start(data):
#     choice = '-'
#     if len(data.keys()) != 1:
#         choice = input('Do you want continue last game? (+ / -): ')
#         if choice == '-':
#             data = {
#                 'round':1,
#             }
#     if choice == '-':
#         for x in range(1, 3):
#             data[input(f'User {x}, enter your name: ')] = 0


# def check_win(data):
#     if data[list(data.keys())[2]] == data[list(data.keys())[1]]:
#         print('Game END by DRAW')
#     elif data[list(data.keys())[2]] > data[list(data.keys())[1]]:
#         print(f'USER {data[list(data.keys())[2]]} WIN')
#     else:
#         print(f'USER {data[list(data.keys())[1]]} WIN')
#     return {'round': 1, }



# while True:
#         rand = randint(1, 100)
#         print(rand)
#         try:
#             user1 = int(input('Enter num in range 1-100: '))
#             user2 = int(input('Enter num in range 1-100: '))
#             if num_validation(user1) or num_validation(user2):
#                 raise ValueError

#         except ValueError:
#             print('Use only numbers')

#         if abs(user1-rand) < abs(user2-rand):
#             data['round']+=1
#             data[list(data.keys())[1]] += 1
#         elif abs(user1-rand) < abs(user2-rand):
#             data['round']+=1
#             data[list(data.keys())[2]] += 1
#         else:
#             print('Draw')
#         data[list(data.keys())[0]] += 1
    
#         if data[list(data.keys())[0]] == 5:
#             data = check_win(data)

#         with open('/Users/danil/Documents/work_py/main/txt.bin', 'wb') as file:
#             pickle.dump(data, file)

#         print(data)
        
        

    #####

# try:
#     with open('/Users/danil/Documents/work_py/main/auto.txt') as file:
#         list_avto=[]
#         list_avto.append(file.read())
#         print(*list_avto)
# except FileNotFoundError:
#     print('not found file')


    #####

# from random import randint
# try: 
#     number = 1
#     def main(guess, rand):
#         global number
#         if guess!=rand:
#             number+=1
#             main(guess=int(input('Nums: ')), rand=randint(1, 5))
#         return number

#     with open('/Users/danil/Documents/work_py/main/auto.txt') as file:
#         res = file.readlines()
#         user = input('User name: ')
#         main(guess=int(input('Nums: ')), rand=randint(1, 5))
#         for i in range(3):
#             score, player = res[i].split()
#             if user in player:
#                 res[i] = f"{number} {user}\n"
#                 break
#             elif number < int(score):
#                 res.insert(i, f"{number} {user}\n")
#                 res.pop()
#                 break
#         with open('/Users/danil/Documents/work_py/main/auto.txt', 'w') as file:
#             file.writelines(res)
        
# except FileNotFoundError:
#     print('Not found file')    


    #####

# import pickle
# lst_nums = []
# def main_func(num):
#     if num!=0:
#         lst_nums.append(num)
#         main_func(int(input('Enter num: ')))

# with open('/Users/danil/Documents/work_py/main/nums.bin', 'rb') as file:
#     try:
#         for i in pickle.load(file):
#             lst_nums.append(i)
#         main_func(int(input('Enter num: ')))
#     except EOFError:
#         main_func(int(input('Enter num: ')))

# with open('/Users/danil/Documents/work_py/main/nums.bin', 'wb') as file:
#     pickle.dump(lst_nums, file)
# print(f'Sum = {sum(lst_nums)}')


    #####

# import pickle
# lst_tabl = []
# for i in range(1, 10):
#     lst = []
#     for j in range(1, 10):
#         lst.append(i*j)
#     lst_tabl.append(lst)

# with open('/Users/danil/Documents/work_py/main/nums.bin', 'wb') as file:
#     for lst in lst_tabl:
#         pickle.dump(lst_tabl, file)

# num = int(input('Enter num: '))
# if num < 1 or num>9:
#     print('\tPlease, use only number 1-9')

# else:
#     nex=0
#     with open('/Users/danil/Documents/work_py/main/nums.bin', 'rb') as files:
#         l = pickle.load(files)
#         for n in l[num-1]:
#             nex+=1
#             print(f'\t{num} * {nex} = {n}')
        











    ######################## O O P

        # INCAPSULATIA


# class Student:
#     def __init__(self, name, surname, age, average_grade):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.average_grade = average_grade
    
#     def get_student_info(self):
#         print (f'Name = {self .name}\n'
#         f'Surname = {self .surname} \n'
#         f'Age = {self.age} \n'
#         f'AVG grade = {self .average_grade}\n')

#     def get_student_scholarship(self) :
#         if self.average_grade > 93:
#             return 2500
#         elif self.average_grade > 74:
#             return 1700
#         return 1000
    
# student1 = Student('Vlad', 'Bipov', 21, 76)
# student2 = Student('Tomas', 'Komich', 19, 83)

# student1.get_student_info()
# student2.get_student_info()

# print(student1.name, '=', student1.get_student_scholarship()) 
# print(student2.name, '=', student2.get_student_scholarship())


    #####

# class Book:
#     def __init__(self, name, author, year_publication):
#         self.name = name
#         self.author = author
#         self.year_publication = year_publication

#     def get_data_book(self):
#         print(f'\n\tName: {self.name}   Author: {self.author}   Year of publication: {self.year_publication}\n')

#     def get_data_age(self):
#         try:
#             if self.year_publication <= 0:
#                 raise ValueError
#             print(f'\tThis book is {2023 - self.year_publication} years old\n')
#         except ValueError:
#             print('Incorrect year of publication\n')
#         except TypeError:
#             print('Use only numbers for year of publication\n')


    #####

# import pickle

# class Advertising:
#     def __init__(self, user, tel_number, date_of_publication, price):
#         self.user = user
#         self.tel_number = tel_number
#         self.date_of_publication = date_of_publication
#         self.price = price
    
#     def check_data_base_user(self):
#         user_data = {
#             ('Mark', +380689124343, '150$'):'17.03.2023',
#         }
#         if self.tel_number not in user_data:
#             user_data.setdefault((self.user, 
#                                 self.tel_number, 
#                                 self.price), self.date_of_publication)

#             with open('/Users/danil/Documents/work_py/main/list_user.bin', 'wb') as file_upd:
#                 pickle.dump(user_data, file_upd)
#             with open('/Users/danil/Documents/work_py/main/list_user.bin', 'rb') as file_r:
#                 show_file = pickle.load(file_r)

#             for i, k in show_file.items():
#                 print('\n\t', *i, '-', k)

# while True:
#     user_advertisig = Advertising(input('Your name: '), input('Your tel-number: '), input('Date_of_publication: '), '50$')
#     user_advertisig.check_data_base_user()


    #####


# class PersonalComputer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram

#     def __getattribute__(self, item):
#         if item == 'cpu11':
#             raise ValueError('error')
#         else:
#             return object.__getattribute__(self, item)
        
#     def __setattr__(self, key, value):
#         if key == 'ptu':
#             raise ValueError('error')
#         else:
#             return object.__setattr__(self, key, value)
        
#     def __getattr__(self, item):
#         return False
    
#     def __delattr__(self, item):
#         return object.__delattr__(self, item)
    
# pc_1 = PersonalComputer('i5', 16)
# setattr(pc_1, 'gpu', 'nvidia')
# print(pc_1.cpu)
# print(pc_1.ram)

# print(pc_1.abc)

# del pc_1.cpu

# print(pc_1.__dict__)
# print(pc_1.cpu)


    #####

# class PersonalComputer:
#     __description = 'hello world'

#     def __init__(self, uid, cpu, ram):
#         self.__uid = uid
#         self._cpu = cpu
#         self.ram = ram


# pc_1 = PersonalComputer('35423', 'i3', 15)
# print(pc_1._cpu)
# print(pc_1.__dict__)
# print(pc_1._PersonalComputer__uid)
# print(pc_1._PersonalComputer__description)


    #####

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def get_x_coord(self):
#         return f'x = {self.x}'
    
#     def set_x_coord(self, new_value):
#         self.__x = new_value
    

# a = Point(3, 10)
# print(a.get_x_coord())

# a.__x = 20
# print(a.__dict__)


    #####

# class Studia:
    
#     def __init__(self, area, popul):
#         self.area = area
#         self.__popul = popul

#     def get_area(self):
#         return f'area = {self.area}, popul = {self.__popul}'
    
#     def set_new_popul(self, new_peopl):
#         self.__popul = new_peopl

#     def get_new_popul(self):
#         return self.area, self.__popul


# peop_1 = Studia(400, 50)
# print(peop_1.get_area())
# peop_1.set_new_popul(70)
# print(*peop_1.get_new_popul())


    #####

# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def get_x_coord(self):
#         return f'x = {self.x}'
    
#     def set_x_coord(self, new_value):
#         self.__x = new_value
    

# a = Point(3, 10)


    #####

# from datetime import date

# class Person:

#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     @classmethod
#     def from_birth_year(cls, name, birth_year):
#         return cls(name, date.today().year - birth_year)
    
#     def get_person_info(self):
#         return f'Name = {self.__name}, Age = {self.__age}'

#     @staticmethod
#     def is_adult(age):
#         return age >= 18



# pers_1 = Person('Oleg', 20)
# pers_2 = Person.from_birth_year('Mark', 1999)
# print(pers_1.get_person_info())
# print(pers_2.get_person_info())    

# print(pers_1.is_adult(19))


    #####

# class Car:

#     def __init__(self, brand, age):
#         self.__brand = brand
#         self.__age = age

#     def get_brand_car(self):
#         return self.__brand, self.__age

#     def __str__(self):
#         return self.__brand, self.__age
    

# bmw = Car('BMW', 5)
# print(bmw.get_brand_car())
# print(bmw)




    #####   GETTER    SETTER

# class Phone:

#     def __init__(self, brand, model):
#         self.__brand = brand
#         self.__model = model
    
#     @property
#     def brand(self):
#         return self.__brand
    
#     @brand.setter
#     def brand(self, brand):
#         self.__brand = brand
    
#     def __str__(self):
#         return f'{self.__brand}, {self.__model}'


# p1 = Phone('Iphone', '14')
# print(p1)

# p1.brand = 'Samsung'
# print(p1.brand)

# p1.brand = '7plus'
# print(p1.brand)


    #####

# class Bus:

#     def __init__(self, marka, model, number_auto):
#         self.__marka = marka
#         self.__model = model
#         self.__number_auto = number_auto
    
#     def get_data_bus(self):
#         return f'Marka = {self.__marka}, Model = {self.__model}, Number bus = {self.__number_auto}'
    

# class Driver:

#     def __init__(self, name, last_name, tel_number):
#         self.__bus = None
#         self.__name = name
#         self.__last_name = last_name
#         self.__tel_number = tel_number
    
#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, name):
#         self.__name = name


#     def add_bus_for_driver(self, marka, model, number_auto):
#         self.__bus = Bus(marka, model, number_auto)
    

#     def __str__(self):
#         return f'\n\tName = {self.__name} Last name = {self.__last_name} Tel-number = {self.__tel_number} {self.__bus.get_data_bus()}\n'


# driv1 = Driver('Mark', 'Domich', '+380973244871')
# driv1.add_bus_for_driver('Mercedes', 'GLS', '2111')
# print(driv1)

# driv1.name = 'Tomas'
# print(driv1.name)


    #####

# import datetime

# class BankAccout:

#     __CURRENCIES = {
#         'UAH': '₴', 
#         'EUR': '€', 
#         'USD': '$',
#     }

#     def __init__(self, currency, balance=0):
#         self.validation_amount(balance)    
#         self.validation_currency(currency)

#         self.__currency = currency
#         self.__balance = balance

#         self.transactions = []

#     def __str__(self):
#         return f'Currency = {self.__currency}\nbalance = {self.__balance}\n{self.__CURRENCIES[self.__currency]}'

#     @classmethod
#     def validation_amount(cls, balance):
#         if not isinstance(balance, (int, float) or balance < 0):
#             raise TypeError('\t\nEnter positive number')

#     @classmethod
#     def validation_currency(cls, currency):
#         if currency.upper() not in cls.__CURRENCIES.keys():
#             raise ValueError('\t\nIncorect currency type')

#     @property
#     def currencies(self):
#         return self.__CURRENCIES

#     def deposit(self, amount):
#         self.validation_amount(amount)
#         self.__balance += amount
#         self.transactions.append(HistoryOperation('Deposit', amount))
#         self.write_data_to_file()

#     def withdraw(self, amount):
#         self.validation_amount(amount)
#         if amount > self.__balance:
#             raise ValueError('\t\nYou have not this amount on your bank account')
#         else:
#             self.__balance -= amount
#             self.transactions.append(HistoryOperation('WithDraw', amount))
#             self.write_data_to_file()
    
#     def write_data_to_file(self):
#         with open('/Users/danil/Documents/work_py/main/data.txt', 'a') as file:
#             for transaction in self.transactions:
#                 file.write(f'{transaction}\n')



# class HistoryOperation:
#     def __init__(self, type, operation):
#         self.type = type
#         self.operation = operation
#         self.time = datetime.datetime.now()

#     def __str__(self):
#         return f'\n\t{self.time}: {self.type} {self.operation}'


# class User:

#     def __init__(self):
#         self.data_accounts = {}

#     def add_account(self, currency, balance=0):
#         if len(self.data_accounts) >= 3:
#             raise ValueError(f'\n\t3 accounts already exist! You cannot add more than 3 accounts')
#         new_account = BankAccout(currency, balance)
#         self.data_accounts[currency] = new_account

#     def get_account_balance(self, currency):
#         if currency not in self.data_accounts:
#             raise ValueError(f'\n\tNo account found for currency - {currency}')
#         return self.data_accounts[currency]

#     def get_all_accounts_balance(self):
#         return '\n'.join([f'{self.data_accounts[data]}\n' for data in self.data_accounts])

#     def deposit_amount_to_account(self, currency, amount):
#         if currency not in self.data_accounts:
#             raise ValueError(f'\n\tNo account found for currency - {currency}')
#         self.data_accounts[currency].deposit(amount)

#     def withdraw_amount_from_account(self, currency, amount):
#         if currency not in self.data_accounts:
#             raise ValueError(f'\n\tNo account found for currency - {currency}')
#         self.data_accounts[currency].withdraw(amount)

#     def get_transaction_history(self, currency):
#         if currency not in self.data_accounts:
#             raise ValueError(f'\n\tNo account found for currency {currency}')
#         with open('/Users/danil/Documents/work_py/main/data.txt', 'r') as file:
#             return file.read()



# user = User()


# user.add_account('USD', 3000)
# user.withdraw_amount_from_account('USD', 500)
# print(user.get_account_balance('USD'))
# # print(user.get_transaction_history('USD'))


# user.add_account('UAH', 5000)
# user.deposit_amount_to_account('UAH', 500)
# print(user.get_account_balance('UAH'))
# # print(user.get_transaction_history('UAH'))


# user.add_account('EUR', 1000)
# user.withdraw_amount_from_account('EUR', 500)
# print(user.get_account_balance('EUR'))
# # print(user.get_transaction_history('EUR'))


# # print(user.get_all_accounts_balance())




    ######  DESCRUPTION

# class Number:
#     @classmethod
#     def validation_number (cls, number):
#         if number <= 0:
#             raise ValueError ()
        
#     def __set_name__(self, owner, name):
#         self.name + '-' + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
    
#     def __set__(self, instance, value):
#         self.validation_number(value)
#         setattr(instance, self.name, value)


# class Brush:
#     size = Number ()
#     hardness = Number ()
#     def __init__(self, size, hardness):
#         self.size = size
#         self.hardness = hardness
    
# res = Brush(15, 50)
# print(res.size)


    #####

# class OptionPerson:

#     @classmethod
#     def validation_name(cls, text):
#         if not text.isalpha():
#             raise ValueError('Use only literal...')
#         return text
    
#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
    
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)
#         self.validation_name(value)

# class Person:
#     name = OptionPerson()
#     last_name = OptionPerson()
#     middle_name = OptionPerson()

#     def __init__(self, name, lastname, middle_name):
#         self.name = name
#         self.last_name = lastname
#         self.middle_name = middle_name

# pers = Person('Oleg', 'Kolipchuk', 'Anatoliovich')
# print(pers.name)
# print(pers.last_name)
# print(pers.middle_name)

# pers.name = 'Mark'
# print(pers.name)


    #####

# class CheckTemperature:
    
#     @classmethod
#     def validation_temperature(cls, val):
#         if not (-273.15 <= 1000.0):
#             raise ValueError('Invalid temperature')
#         return val

#     def __set_name__(self, owner, name):
#         self.name = '_' + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

#     def __set__(self, instance, value):
#         self.validation_temperature(value)
#         setattr(instance, value)


# class CheckScale:

#     __VALID_SCALE = ('C', 'F', 'K')

#     @classmethod
#     def validation_scale(cls, value):
#         if value not in 

# class Temperature:
#     value = CheckTemperature()
#     scale = CheckScale()
    
#     def __init__(self, value, scale):
#         self.value = value
#         self.scale = scale

#     def convert(self, to_scale):
#             if self.scale == "C":
#                 if to_scale == "F":
#                     return self.value * 9 / 5 + 32
#                 elif to_scale == "K":
#                     return self.value + 273.15
#             elif self.scale == "F":
#                 if to_scale == "C":
#                     return (self.value - 32) * 5 / 9
#                 elif to_scale == "K":
#                     return (self.value - 32) * 5 / 9 + 273.15
#             elif self.scale == "K":
#                 if to_scale == "C":
#                     return self.value - 273.15
#                 elif to_scale == "F":
#                     return (self.value - 273.15) * 9 / 5 + 32
#             raise ValueError('Error with data')



    #####

# import calendar


# class DateDescriptor:

#     @classmethod
#     def validation_date(cls, year, month, day):
#         if not (1 < month < 12):
#             raise ValueError('Incorrect month')
#         if not (1 < day < calendar.monthrange(year, month)[1]):
#             raise ValueError('Incorrect day')

#     def __set_name__(self, owner, name):
#         self.year_attr = f'_{name}_year'
#         self.month_attr = f'_{name}_month'
#         self.day_attr = f'_{name}_day'

#     def __get__(self, instance, owner):
#         year = getattr(instance, self.year_attr)
#         month = getattr(instance, self.month_attr)
#         day = getattr(instance, self.day_attr)
#         return f'{year}-{month}-{day}'

#     def __set__(self, instance, date):
#         year, month, day = date.split('-')
#         year = int(year)
#         month = int(month)
#         day = int(day)

#         self.validation_date(year, month, day)

#         setattr(instance, self.year_attr, year)
#         setattr(instance, self.month_attr, month)
#         setattr(instance, self.day_attr, day)


# class SomeDate:

#     date = DateDescriptor()


# all_date = SomeDate()
# all_date.date = '2022-03-20'
# print(all_date.date)


    #####

# class DesctriptorDataUser:
#     def validation_name(cls, text_name):
#         for el in text_name:
#             if not el.isalnum():
#                 raise ValueError('Use only literal or nums')
    
#     def __set_name__(self, owner, name):
#         self.name = '-' + name

#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)

#     def __set__(self, instance, value):
#         self.validation_name(value)
#         setattr(instance, self.name, value)
        

# class Main:
#     name = DesctriptorDataUser()
#     last = DesctriptorDataUser()

# main = Main()
# main.name = 'Mark'
# print(main.name)





    ####### __CALL__ 

# class Main:
#     def __init__(self, x):
#         self.x = x
    
#     def __call__(self, y, *args, **kwds): 
#         return self.x+y
    

# ma = Main(1)
# print(ma(2))



# def main(x):
#     def nex(y):
#         return x+y
#     return nex

# do = main(1)

# print(do(2))


    #####

# class Main:
#     def __init__(self, lst):
#         self.lst = lst
    
#     def __call__(self, func):
#         return list(filter(func, self.lst))

# main = Main([7, 1, 3, 2, 8])
# print(main(lambda x: x % 2 == 0))


    #####

# class Main:
#     def __init__(self, lst):
#         self.lst = None

#     def __call__(self, *args, **kwds):
#         return list(filter(lambda x: x if x%2==0 else None, self.lst))
    
# main = Main(3, 4, 5)
# print(main())



    ########  DECORATOR FOR CLASS

# class MyClass:
#     def __init__(self, func):
#         self.__func = func
    
#     def __call__(self, text, symbol='_'):
#         return symbol.join(self.__func(text))
    
# @MyClass
# def some_func(text):
#     return text

# func = some_func('abc')
# print(func)


    #####

# class TagText:

#     __tags = 'p, h1, h2, h3, h4, h5, h6, span'.split(', ')

#     def __init__(self, func):
#         self.__func = func

#     def __call__(self, text, tag='h1'):
#         self.validation_tags(tag)
#         return f'<{tag}>{text}</{tag}>'
    
#     @classmethod
#     def validation_tags(cls, tag):
#         if tag not in cls.__tags:
#             raise ValueError('Use only: p, h1, h2, h3, h4, h5, h6, span')
        

# @TagText
# def do_teg(text, tag):
#     return text, tag
    
# data = do_teg('Python')
# print(data)

    #####

# class IntegerNumbers:

#     def __init__(self, func_num):
#         self.func = func_num
    
#     def __call__(self, num1, num2, *args, **kwds):
#         if self.validation_num(num1, num2):
#             return self.func(num1, num2)
#         else:
#             return 'Numbers must be integer'
    
#     @classmethod
#     def validation_num(cls, num1, num2):
#         if isinstance(num1, int) and isinstance(num2, int):
#             return False
#         return True
    

# @IntegerNumbers
# def enter_num(num1, num2):
#     return num1+num2

# print(enter_num(2, 3))
    


    #######    __LEN__

# class Master:

#     def __init__(self, name, lst_auto=[]):
#         self.name = name
#         self.lst_auto = lst_auto

#     def add_auto(self, brand, num_auto, problem):
#         self.lst_auto.append(Car(brand, num_auto, problem))

#     def __len__(self):
#         return len(self.lst_auto)


# class Car:
#     def __init__(self, brand, num_auto, problem):
#         self.brand = brand
#         self.num_auto = num_auto
#         self.problem = problem


# master = Master('Mark')
# print(master.add_auto(input('Brand: '), input('Num-auto: '), input('Problem: ')))
# print(len(master))


    #####

# import datetime

# class SaveDate:
#     def __init__(self, func):
#         self.func = func

#     def __call__(self, menu, lst_data={}):
#         if menu == 1 or menu == 2 or menu == 3:
#             lst_data[menu]=datetime.datetime.now().strftime('%H:%M:%S')
#             return menu
#         elif menu == 0:
#             return lst_data
        
# @SaveDate
# def choice_menu(menu):
#     return menu

# while True:
#     data = choice_menu(int(input('Menu: 1-Eat, 2-Work, 3-Sleep, 0-Exit: ')))
#     print(data)

    
    ######

# class Name:
#     @classmethod
#     def validation_name(cls, name):
#         for el in name:
#             if not el.isalpha():
#                 raise ValueError('Incorrect data')
#             return name
        
#     def __init__(self, value):
#         self.value = value

#     def __get__(self, instance, owner):
#         return self.value

#     def __set__(self, instance, value):
#         self.validation_name(value)
#         self.value = value


# class Grade:
#     @classmethod
#     def validation_grade(cls, value):
#         if not 1 <= value <= 12:
#             raise ValueError('Grade must be between 1 and 12')
        
#     def __init__(self, value):
#         self.value = value

#     def __get__(self, instance, owner):
#         return self.value

#     def __set__(self, instance, value):
#         self.validation_grade(value)
#         self.value = value


# class Subject:
#     def __init__(self, name, grades=[]):
#         self.name = name
#         self.grades = grades

#     def add_grade(self, grade):
#         self.grades.append(Grade(grade))

#     def edit_grade(self, index, grade):
#         self.grades[index] = Grade(grade)

#     def delete_grade(self, index):
#         del self.grades[index]

#     def __len__(self):
#         return len(self.grades)


# class Student:
#     def __init__(self, first_name, last_name, middle_name, group, subjects=[]):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.middle_name = middle_name
#         self.group = group
#         self.subjects = subjects

#     def add_subject(self, subject):
#         self.subjects.append(subject)

#     def edit_subject(self, index, subject):
#         self.subjects[index] = subject

#     def delete_subject(self, index):
#         del self.subjects[index]

#     def __len__(self):
#         return len(self.subjects)


# s = Student('Oleg', 'Gopich', 'Antonovich', 'Group 1')
# math = Subject('Math', [Grade(10), Grade(11), Grade(12)])
# history = Subject('History', [Grade(9), Grade(8)])

# s.add_subject(math)

# s.add_subject(history)

# english = Subject('English')

# s.add_subject(english)

# s.edit_subject(1, english)

# s.delete_subject(2)
# math.add_grade(11)

# math.edit_grade(0, 12)
# math.delete_grade(1)

# print(s.first_name, s.last_name)




    #####  __ADD__

# class Number:
#     def __init__(self, num, text):
#         self.num = num
#         self.text = text

#     def __add__(self, other):
#         return Number(self.num + other.num, other.text)

    # def __str__(self):
    #     return self.num, self.text

# n = Number(2, 'hi')
# b = Number(3, 'Hello')
# res = n+b
# print(res)


    #####

# class ShoppingList:
#     def __init__(self, *args):
#         self.lst = self.convert(args)

#     def convert(self, args):
#         if isinstance(args[0], str):
#             return [value for value in args]
#         return args[0]
        
#     def __add__(self, other):
#         return ShoppingList(self.lst + other.lst)

#     def __str__(self):
#         return str(self.lst)


# ins = ShoppingList(['Book', 'Apple', 'Car'])
# ins_noth = ShoppingList('MP3')
# all_data = ins + ins_noth
# print(all_data)

    
    #####

# class Order:
#     def __init__(self, order):
#         self.order = order

#     def __add__(self, other):

#         new_order = self.order.copy()
#         for key, val in other.order.items():
#             new_order[key] = new_order.get(key, 0) + val
    
#         return Order(new_order)

#     def __str__(self):
#         return str(self.order)

# main = Order({'Orange':12, 'Name':3})
# nexte = Order({'Name':5})
# res = main + nexte
# print(res)


    #####

# class Line:
#     def __init__(self, line):
#         self.line = line
    
#     def __add__(self, other):
#         return Line(self.line + other.line)

#     def __str__(self):
#         return str(self.line)


# summ_line = Line(5)
# summ_line_nother = Line(5)
# res_line = summ_line+summ_line_nother
# print(res_line)





    #######  __GETITEM__   __SETITEM__

# class Dish:
#     def __init__(self, name, price, description):
#         self.name = name
#         self.price = price
#         self.description = description


# class Menu:
#     def __init__(self):
#         self.dishes = {}

#     def __getitem__(self, item):
#         return self.dishes[item]

#     def __setitem__(self, key, value):
#         self.dishes[key]=value
    
#     def __delitem__(self, key):
#         del self.dishes[key]

# while True:
#     menu = Menu()
#     menu['Margarita'] = Dish('Margarita', 100, 'best pizza')
#     user = input('SELECT: name; price; description: ')
#     if user == 'name':
#         print(menu['Margarita'].name)
#     elif user == 'price':
#         print(menu['Margarita'].price)
#     elif user == 'description':
#         print(menu['Margarita'].description)
#     else:
#         print('Use only object in the menu')


    #####

# class Car:
#     def __init__(self, model, year, run):
#         self.model = model
#         self.year = year
#         self.run = run
    

# class Garage:
#     all_cars = {}

#     def __getitem__(self, item):
#         return self.all_cars[item]
    
#     def __setitem__(self, key, value):
#         self.all_cars[key]=value
    
#     def __delitem__(self, key):
#         del self.all_cars[key]


# main = Garage()
# main['AUDI'] = Car('Q8', 2022, 4000)
# print(main['AUDI'].model)
# del main['AUDI']






    ########   IMITATION  

# class Transport:
#     def __init__(self, car, bus, moto):
#         self.car = car
#         self.bus = bus
#         self.moto = moto
    
#     def __str__(self):
#         return 'Just base'


# class Bmw(Transport):
#     def __init__(self, car, bus, moto, about):
#         super().__init__(car, bus, moto)
#         self.about = about

#     def __str__(self):
#         return self.about


# class Mercedes(Transport):
#     def __init__(self, car, bus, moto):
#         super().__init__(car, bus, moto)
    
#     def __str__(self):
#         return super().__str__()


# cars_1 = Bmw('BMW', 'Mercedes-Benz', 'Yamaha R600', 'This list for speed!')
# cars_2 = Mercedes('Mercedes', 'Opel', 'Yamaha R200')
# print(cars_1)
# print(cars_2)


    #####

# import datetime

# class History:
#     __id_key = 0
    
#     def __init__(self):
#         History.__id_key += 1
#         self.__id_key = History.__id_key
#         self.history = []
    
#     def add_event(self, event):
#         timestamp = datetime.datetime.now().strftime('%d %d.%m.%Y %H:%M:%S')  #знайшов цікаве рішення, для діставання дати і часу
#         self.history.append(f'[{self.__id_key}] {timestamp}: {event}')
    
#     def __str__(self):
#         return '\n'.join(self.history)


# class Person:
#     def __init__(self, name, last_name, birthyear):
#         self.name = name
#         self.last_name = last_name
#         self.birthyear = birthyear
#         self.age = self.__get_age(birthyear)

#     @classmethod
#     def __get_age(cls, birthyear):
#         return datetime.datetime.now().year - birthyear

#     def __str__(self):
#         return f'name = {self.name}, last-name = {self.last_name}, birthday = {self.birthyear}, age = {self.age}'
    

# class Surgeon(Person):
#     def __init__(self, name, surname, birth_year):
#         super().__init__(name, surname, birth_year)
#         self.history = History()
#         self.patients = []

#     def add_patient(self, patient):
#         self.patients.append(patient)
#         self.history.add_event(f'add Patient {patient.name} {patient.last_name}')
    
#     def create_operation(self, patient, date):
#         if patient in self.patients:
#             operation = Operation(self, patient, date)
#             self.history.add_event(f'create operation: surgeon - {self.name} {self.last_name}, patient - {patient.name} {patient.last_name}, date - {date}')
#             return operation
#         else:
#             print(f'{patient.name} {patient.last_name} is not a patient of {self.name} {self.last_name}')
    
#     def show_my_patients(self):
#         print(f'{self.name} {self.last_name} patients: \n') 
#         for obj in self.patients:
#             print(obj)
    
#     def show_history(self):
#         print(f'{self.name} {self.last_name} history: \n')
#         print(self.history)


# class Patient(Person):
#     def __init__(self, name, last_name, birthyear, problem):
#         super().__init__(name, last_name, birthyear)
#         self.problem = problem
    
#     def __str__(self):
#         return f'name = {self.name}, last-name = {self.last_name}, birthday = {self.birthyear}, age = {self.age}, problem = {self.problem}'


# class Operation:
#     def __init__(self, surgeon, patient, date):
#         self.surgeon = surgeon
#         self.patient = patient
#         self.date = date
    
#     def __str__(self):
#         return f'surgeon - {self.surgeon.name} {self.surgeon.last_name}, patient - {self.patient.name} {self.patient.last_name}, date - {self.date}'

    
# s1 = Surgeon('Stepan', 'Vasiliv', 1963)
# p1 = Patient('Orest', 'Pishiv', 1978, 'Pain in neck')
# p2 = Patient('Vita', 'Bol', 1994, 'Head ace')
# his = History()
# his.add_event(p1)
# print(his)






    ###### DOUBLE CLASS

