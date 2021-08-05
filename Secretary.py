documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def ret_name():
    num_doc = input('Введите номер документа: ')
    x = 0
    for num in documents:

        if num["number"] == num_doc:
            print(f'Это документ человека с именем: {num["name"]}')
        else:
            x += 1

        if x == len(documents):
            print('Человека с таким документом в базе нет')


def ret_dir():
    num_doc = input('Введите номер документа: ')
    x = 0

    for key, value in directories.items():

        for element in value:

            if element == num_doc:
                print(f'Документы данного человека лежат на {key} полке')
                x -= 1
                break

        x += 1

    if x == len(directories):
        print('Человека с таким документом в базе нет')


def print_list():
    for element in documents:
        print(f'{list(element.values())[0]}   "{list(element.values())[1]}"  "{list(element.values())[2]}"; ')


def add_doc():
    type_doc = input('Введите тип документа: ')
    num_doc = input('Введите номер документа: ')
    name_of = input('Введите ФИО человека: ')
    num_shelf = input('Введите номер полки для хранения: ')

    if int(num_shelf) > len(directories):
        print('Невозможно поместить данный документ на несуществующую полку')
    else:
        documents.append({'type': type_doc, 'number': num_doc, 'name': name_of})
        directories[num_shelf].append(num_doc)


print('Добрый день! Вас приветсвует программа секретарь!')
print('Нажмите P если хотите найти человека по номеру документа')
print('Нажмите S если хотите узнать, на какой полке лежит документ')
print('Нажмите L если хотите просмотреть весь список документов')
print('Нажмите A если хотите добавить документ в базу')
print()

enter = str(input('Ваш выбор - '))

if enter == 'p' or enter == 'P':
    ret_name()

elif enter == 's' or enter == 'S':
    ret_dir()

elif enter == 'l' or enter == 'L':
    print_list()

elif enter == 'a' or enter == 'A':
    add_doc()

else:
    print('Команда некорректна, повторите еще раз')
print ('Это мой опыт в GIT')
