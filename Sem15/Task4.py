import argparse
import datetime

from log_new import log_dec

# import logging
# logging.basicConfig(filename='logs.log', filemode='w', encoding='utf-8', level=logging.ERROR)
MOUTH = {"января": 1, "февраля": 2, "марта": 3, "апреля": 4, "мая": 5, "июня": 6,
         "июля": 7, "августа": 8, "сентября": 9, "октября": 10, "ноября": 11, "декабря": 12}

MOUTHREV = dict(map(lambda x: (x[1], x[0]), MOUTH.items()))

WEEKDAY = {"понедельник": 1, "вторник": 2, "среда": 3,
           "четверг": 4, "пятница": 5, "суббота": 6, "воскресенье": 7}

WEEKDAYREV = dict(map(lambda x: (x[1], x[0]), WEEKDAY.items()))


@log_dec
def print_date(str_day):
    num, weekday, mouth = str_day.split()
    num = int(num[0])
    weekday = WEEKDAY[weekday] - 1
    mouth = MOUTH[mouth]
    count = 0
    for i in range(1, 32):
        temp_date = datetime.datetime(datetime.datetime.now().year, mouth, i)
        if temp_date.weekday() == weekday:
            count += 1
            if count == num:
                return temp_date
    raise ValueError

def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number', default=1)
    parser.add_argument('-w', '--weekday', default=WEEKDAYREV.get(datetime.datetime.now().weekday(), "понедельник"))
    parser.add_argument('-m', '--month', default=MOUTHREV.get(datetime.datetime.now().month, "января"))
    args = parser.parse_args()
    return print_date(f'{args.number}-ый {args.weekday} {args.month}')

print(par())
    # print(print_date("1 четверг ноября"))
