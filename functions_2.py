# -----------
#  task_1
# -----------

def add(a, b):
    return a + b


def substruct(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

# -----------
#  task_2
# -----------


def len_sent(sent):
    sum = 0
    for i in sent:
        sum += 1
    return sum


predl = 'Люблю грозу в начале мая!'
print(len_sent(predl), len(predl))

# -----------
#  task_3
# -----------

cars1 = {'opel': 10000, 'bmw': 20000}
cars2 = {'mclaren': 1000000}


def list_concat(list1, list2):
    list1.update(list2)


list_concat(cars1, cars2)
print(cars1)

# -----------
#  task_4
# -----------


def menu():
    menu = [i for i in input(
        'Введите то, что хотите покушать и попить -> ').split()]
    with open('/home/denis/Desktop/menu.txt', 'w') as menu_text:
        for dish in menu:
            print(dish, file=menu_text)
        print('Your dishes is added to menu.txt file by "~/Desktop/menu.txt"')

# menu()

# -----------
#  task_5
# -----------


def create_file(file_name):
    with open(f'{file_name}', 'w'):
        pass

# create_file('krokozyablik.txt')

# -----------
#  task_6
# -----------


def main_function():
    print('Я главная функция')

    def nested_function():
        print('Я вложенная функция')
    nested_function()


main_function()

# -----------
#  task_7
# -----------


def dict_separator(dict):
    a, b = [], []
    for i in dict:
        a.append(i)
        b.append(dict.get(i))
    return a, b


print(dict_separator(cars1))
a, b = dict_separator(cars1)
# print(dict_separator(cars1))
print(b)
print(a)


# -----------
#  task_8
# -----------

def is_simple(num):
    p = num % 2 != 0
    m = 3
    while m < num**0.5 + 1 and p:
        if num % m == 0:
            p = False
        m += 2
    if p:
        p = ''
    else:
        p = 'НЕ'

    return f'Число {num} {p} является простым'


print(is_simple(113))

# -----------
#  task_9
# -----------


def args_to_list(a, b):
    lst = []
    lst.append(a)
    lst.append(b)
    return lst


print(args_to_list(3, 'asdlfj'))

# -----------
#  task_10
# -----------


def how_much_to_print():
    num = input("Введите число, которое распечатается столько же раз -> ")
    for i in range(int(num)):
        print(num)


how_much_to_print()

# -----------
#  task_11
# -----------


def name_zarik(name, zarik=5000):
    return f'{name} - {zarik}\n'


print(name_zarik('Vasilij'), name_zarik('Denis Kominarets', 100000))

# -----------
#  task_12
# -----------


def list_of_n_random_elements():
    from random import randint
    n = int(input('Сечас создам список из n элементов\nВведите n -> '))
    lst = [randint(0, 1000) for i in range(n)]
    return lst


a = list_of_n_random_elements()
print(a)
