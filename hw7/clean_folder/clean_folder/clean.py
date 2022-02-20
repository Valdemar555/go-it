import sys


def my_func():
    try:
        print(sys.argv[1])
    except:
        print("аргументы скрипта не были указаны при вызове")