import sys
import io


def readFile(filename):
    data = [i.split() for i in open(filename, 'r', encoding='utf-8')]
    return data


def printInfo(data):
    for i in data:
        print(f'{i}\n')


def exit(data):
    print('До свидания!')


def writeFile(data):
    new = input('Введите данные ').split()
    with open('tel.txt', 'a', encoding='utf-8') as f:
        f.writelines("%s\n" % line for line in new)


def findData(data):
    word = input('введите характеристику: ')
    with io.open('tel.txt', encoding='utf-8') as file:
        for line in file:
            if word in line:
                print(line, end='')


def main():
    my_choice = -1
    data = readFile('tel.txt')
    while my_choice != 0:
        print('Выберите одно из действий:')
        print('1 - вывести инфо на экран')
        print('2 - вписать данные в файл')
        print('3 - найти строку по характеристрике')
        print('0 - выход из программы')
        my_choice = int(input())
        operations = {0: exit, 1: printInfo, 2: writeFile, 3: findData}
        operations[my_choice](data)


if __name__ == '__main__':
    main()
