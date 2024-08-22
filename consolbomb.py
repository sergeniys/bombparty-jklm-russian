
import random
from threading import Timer
f = open(r'russian.txt').readlines()
letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
           'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
zapret = ['ь', 'ъ', 'ы', 'ф', 'э', 'й', 'ё', 'щ', 'ш', 'ю']# проще удалить из letters, но это для усложения в дальнейшем

sogls = ["б", "в", "г", "д", "Ж","з","к", "л", "м", "н", "п", "р", "с","т", "ф", "х", "ц", "ч", "ш", "щ"]
vse_gls = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

historsis = []  # list of words







def proverka(choser):
    if choser[0] in zapret   or choser[1] in zapret:
        return False
    if choser[0] in sogls and choser[1] in sogls:
        return False
    if choser[0] in vse_gls and choser[1] in vse_gls:
        return False
    if choser == 'чя' or choser == 'чю':
        return False
    return True


def create():
    while True:
        choser = ''.join(random.choices(letters, k=2))
        if proverka(choser):
            print(choser)
            return choser


def task(message):
    # report the custom message

    print(message)

    raise NameError('HiThere')
    exit(0)


#
#
# print('добро пожаловать')
#
# while True:
#     choser = create()
#
#     timer = Timer(7, task, args=('Время кончилось',))
#     timer.start()
#     while True:
#         inn = input(f'{choser}:-')
#         if choser in inn and f'{inn}\n' in f and inn not in historsis:
#             historsis.append(inn)
#             timer.cancel()
#             break
#         else:
#             print('плохо')

