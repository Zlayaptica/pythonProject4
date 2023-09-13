# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.




MIN_LIM = 0
MAX_LIM = 100000
SINGLE = 1
MIN_NUM = 2

input_num = -1

while not (MIN_LIM <= input_num <= MAX_LIM):
    input_num = int(input('Введите целое число от 0 до 100000'))

if input_num >= MIN_NUM:
    sum = 0
    for i in range(SINGLE, input_num + 1):
        if input_num % i == 0:
            sum += 1
    if sum <= 2:
        print(f'Число {input_num} простое')
    else:
        print(f'Число {input_num} составное')
else:
    print('Числа 0 и 1 не являются ни простыми, ни составными')