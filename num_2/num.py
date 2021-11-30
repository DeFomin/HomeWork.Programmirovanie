# Программа для контроля собственных денежных средств
from tabulate import tabulate
import sys

file_out = open('output.txt', 'w')

def main_exit(): # Возможность выйти из программы
    print('Завершить программу (Да/Нет)?')
    print('| ', end = '')
    question_exit = input()

    while (question_exit not in num_proverka): # Прооверка на правильный ввод
        print('Попробуйте еще раз (Да/Нет): ')
        print('| ', end = '')
        question_exit = input()

    if (question_exit in num_proverka_da):
        print('Досрочное завершение программы')
        result = tabulate(table, headers, tablefmt="grid")
        file_out.write('Итоговая таблица:\n') # Запись в файл
        file_out.write(str(result))
        sys.exit()

    if (question_exit in num_proverka_not):
        print('Продолжим')
        print()


headers=["Number","Product", "Category Product", "Price", "Data"]
table = []
Proverka_arr = ['+', '-']
Proverka = ''
row = 0

# Основной цикл. Заполнение массива
while True:
    a = []
    #print(row)
    print('Введите данные: ')

    print('1. Product:', end = ' ')
    product_input = [str(input())]

    print('2. Category Product:', end = ' ')
    product_category_input = [str(input())]

    print('3. Price:', end = ' ')
    price_input = [str(input())]

    print('4. Data:', end = ' ')
    data_input = [str(input())]

    a += str(row)
    a += product_input
    a += product_category_input
    a += price_input
    a += data_input

    table.append(a)

    print('Если хотите добавить еще покупку введите "+", если хотите выйти введите "-": ', end = ' ')
    Proverka = input()

    while (Proverka not in Proverka_arr): # Прооверка на правильный ввод
        print('Попробуйте ещё раз ("+"/"-"): ', end = ' ')
        Proverka = input()

    if (Proverka == '+'):
        row += 1
        print()
    else:
        print('Exiting...')
        print()
        result = tabulate(table, headers, tablefmt="grid")
        print(result)
        break


prov_num_2 = []
num_proverka = ['да', 'ДА', 'Да', 'НЕТ', 'Нет', 'нет']
num_proverka_not = ['НЕТ', 'Нет', 'нет']
num_proverka_da = ['да', 'ДА', 'Да']
vvel = ''
num = ''



exit = main_exit() # Выход


print('Вы хотите что-нибудь удалить (Да/Нет)? ')
print('| ', end = '')
question = input()
while (question not in num_proverka): # Прооверка на правильный ввод
    print('Попробуйте еще раз (Да/Нет): ')
    print('| ', end = '')
    question = input()

# Удаление строк
if (question == 'Да') or (question == 'да') or (question == 'ДА'):
    while (num not in num_proverka_not) or (len(table) == 0):
        prov_num_2 = []

        print('Какую строчку?')
        print()
        for i in range(len(table)):
            prov_num_2.append(str(i))
            print(i, end = ' ')

        print()
        print('| ', end = '')
        vvel = input()

        while (vvel not in prov_num_2): # Прооверка на правильный ввод
            print('Попробуйте еще раз: ', *prov_num_2)
            print('| ', end = '')
            vvel = input()

        table.pop(int(vvel))
        # Исправляем нумерцаю
        for i in range(len(table)):
            table[i][0] = i
        # Нельзя удалить последнюю строчку
        if (len(table) > 0):
            print()
            print('Хотите ли удалить ещё строк (Да/Нет)?')
            print('| ', end = '')
            num = input()

            while (num not in num_proverka):
                print('Попробуйте еще раз (Да/Нет): ')
                print('| ', end = '')
                num = input()

            if (num == 'Да') or (num == 'да') or (num == 'ДА'):
                print(tabulate(table, headers, tablefmt="grid"))
                print('Продолжим')
                print()
            else:
                print()
                print('Exiting...')
                print(tabulate(table, headers, tablefmt="grid"))
                break
        else:
            print()
            print('Больше убрать нельзя: ')
            print(tabulate(table, headers, tablefmt="grid"))
            break
else:
    print('Exiting...')
    print(tabulate(table, headers, tablefmt="grid"))
    #print(table, headers, a)

if (len(table) > 1):
    exit = main_exit() # Выход

Infinity = True

if (len(table) > 1):
    print()
    question_sort = ''
    print('Итак, хотите ли вы отсортировать по цене товары (Да/Нет)?')
    question_sort = input()

    while (question_sort not in num_proverka): # Прооверка на правильный ввод
        print('Попробуйте еще раз (Да/Нет): ')
        print('| ', end = '')
        question_sort = input()



    # Сортировка товаров по ценнику (Вниз)
    if (question_sort == 'Да') or (question_sort == 'да') or (question_sort == 'ДА'):
        table.sort(key = lambda x: x[3])
        for i in range(len(table)):
            table[i][0] = i
        print()
        print('Отсортировано')
        print(tabulate(table, headers, tablefmt="grid"))
    else:
        print('Exiting...')
        print(tabulate(table, headers, tablefmt="grid"))
elif (len(table) == 0) or (len(table) == 1):
    print('Интересно, конечно...')
    print()
else:
    Infinity = False
    print()
    print('The End')
    print(tabulate(table, headers, tablefmt="grid"))

if Infinity:
    print()
    print('The End')
    print(tabulate(table, headers, tablefmt="grid"))

result = tabulate(table, headers, tablefmt="grid")




file_out.write('Итоговая таблица:\n')
file_out.write(str(result))

file_out.close()
