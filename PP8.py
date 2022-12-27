import logging
import random
logging.basicConfig(filename="bag.log", level=logging.INFO)


def input_check():
    while True:
        try:
            a = int(input("Введите количество рандомных чисел: "))
            if a <= 0:
                print("Введите натуральное число!")
                logging.error("Incorrect number")
            else:
                logging.info(f"User input, number of random numbers is {a}")
                return a
        except ValueError:
            print("Некоректное значение, попробуйте ещё раз")
            logging.error("ValuerError")


logging.info("--Program started--")
n = input_check()
bag = list(range(1, n + 1))
random.shuffle(bag)

for i in range(n):
    print(f"Ваше {i + 1}-е число = {bag[i]}", end=' ')
    logging.info(f"{i + 1} number is {bag[i]}")
    a = input()

logging.info("--Program finished--")
