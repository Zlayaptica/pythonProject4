import argparse
import random
import logging

logging.basicConfig(filename='logs.log', filemode='w', encoding='utf-8', level=logging.INFO)

original_list = [random.randint(0, 9) for _ in range(15)]
unique_dublicate_list = list({item for item in original_list if original_list.count(item) > 1})
logging.info(f"The values of original_list and unique_dublicate_list are {original_list} and {unique_dublicate_list}.")
try:
    print(original_list, unique_dublicate_list)
    logging.info(f"original_list, unique_dublicate_list successful with "
                 f"result: {original_list, unique_dublicate_list}.")

except ZeroDivisionError as err:
    logging.error("Ошибка", exc_info=True)


def par():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--original_list', action='append')
    parser.add_argument('-u', '--unique_dublicate_list', action='append')
    args = parser.parse_args()
    return print(f'{args.original_list} {args.unique_dublicate_list}')

print(par())
