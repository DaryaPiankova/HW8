import sys
import io

def readfile(filename):
    data = [i.split() for i in open(filename, 'r', encoding='utf-8')]
    return data


def printinfo(data):
    for i in data:
        print(i)


def exit(data):
    print('До свидания!')


def writefile(data):
    new = input('Введите данные ').split()
    with open('tel.txt', 'a', encoding='utf-8') as f:
        f.writelines("%s\n" % line for line in new)
    

def finddata(data):
    word = input('введите характеристику')
    with io.open('tel.txt', encoding='utf-8') as file:
        for line in file:
            if word in line:
                print(line, end='')



def main():
    my_choice = -1
    data = readfile('tel.txt')
    while my_choice != 0:
        print('Выберите одно из действий:')
        print('1 - вывести инфо на экран')
        print('2 - произвести экпорт данных')
        print('3 - найти строку')
        print('0 - выход из программы')
        my_choice = int(input())
        operations = {0: exit, 1: printinfo, 2: writefile, 3: finddata}
        operations[my_choice](data)


if __name__ == '__main__':
    main()