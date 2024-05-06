# импорт необходимых библиотек
import json
from pathlib import Path
from prettytable import PrettyTable

# загрузка json файла
path = Path('info.json')
data = json.loads(path.read_text(encoding='utf-8'))

# создание таблицы для дальнейшего вывода информации
table = PrettyTable()
table.field_names = ["ID", "Date", "Category", "Summa", 'Description']


def add_user(name):
    # функция для добавления нового пользователя
    data['personal'].append({
        "name": str(name),
        "balance": 0,
        "operations": []
    })
    path.write_text(json.dumps(data), encoding='utf-8')
    print(f'User {name} added')


def check_user(name):
    # проверка отсутствия пользователя в файле (возвращает True при отсутствии)
    for user in data['personal']:
        if user['name'] == str(name):
            return False

    return True


class Wallet:
    def __init__(self, name, balance=0):
        # инициализация необходимых переменных и добавление нового пользователя в файл по необходимости
        if check_user(name):
            add_user(name)
            self.name = str(name)
            self.balance = int(balance)
        else:
            self.name = str(name)

    def show_balance(self):
        # пробегаемся по файлу и сравниваем имена с именем пользователя, выводим его баланс
        for user in data['personal']:
            if user['name'] == self.name:
                print(f'Your balance {user["balance"]}')

    def change_balance(self, value):
        # пробегаемся по файлу и сравниваем имена с именем пользователя
        # добавляем или вычитаем из баланса значение value
        for user in data['personal']:
            if user['name'] == self.name:
                user['balance'] += int(value)
                path.write_text(json.dumps(data), encoding='utf-8')
                print('Balance changed')

    def show_operation(self, type):
        # функция по выводу всех операций type.
        for user in data['personal']:
            # проходим всех пользователей и останавливаемся на нужном
            if user['name'] == self.name:
                # проходим циклом по его операциям
                for oper in user['operations']:
                    # если категория операции та, что выбрал пользователь (type)
                    # то добавляем информацию об операции в таблицу
                    if oper['category'] == str(type):
                        table.add_row([oper['id'], oper['date'], oper['category'], oper['summa'], oper['description']])
        # вывод информации и очистка таблицы
        print(table)
        table.clear_rows()

    def search_info(self, info):
        # поиск информации по ключевому слову info
        for user in data['personal']:
            # проходим циклом по всем пользователям
            if user['name'] == self.name:
                # останавливаемся на нужном и смотрим все его операции
                for oper in user['operations']:
                    if (oper['date'] == info) or (oper['category'] == info) or (oper['summa'] == info):
                        # если info содержится в одной из строчек профиля то добавляем в таблицу
                        table.add_row([oper['id'], oper['date'], oper['category'], oper['summa'], oper['description']])
        print(table)
        table.clear_rows()

    def add_operation(self, date, category, summa, description):
        # функция по добавлению опреации
        # получаем индекс нужного пользователя путем сравнивания всех имен
        ind = int()
        for i in range(0, len(data["personal"])):
            if data["personal"][i]['name'] == self.name:
                ind = i

        # инициализируем переменную, отвечающую за максимальный id, понадобится для создания уникального id
        max_id = 0
        #  циклами находим максимальный id и записываем его в ранее созданную переменную
        for i in range(0, len(data["personal"])):
            for oper in data["personal"][i]['operations']:
                curr_id = int(oper['id'])
                max_id = max(max_id, curr_id)

        # создаем json запись новой операции и добавляем ее
        data['personal'][ind]['operations'].append({
            'id': max_id + 1,
            'date': str(date),
            'category': str(category),
            'summa': int(summa),
            'description': str(description)
        })
        path.write_text(json.dumps(data), encoding='utf-8')

        # обновляем баланс пользователя ввиду новой операции.
        if category == 'profit':
            # увеличиваем баланс на summa
            Wallet.change_balance(self, summa)
        elif category == 'expenses':
            summa = int(summa) * -1
            # уменьшаем баланс на summa
            Wallet.change_balance(self, summa)

        print('Operation added')

    def change_note(self, id, type, value):
        # функция по изменению любого параметра операции по id
        # циклами добираемся по нужной операции
        for user in data['personal']:
            for oper in user['operations']:
                if oper['id'] == int(id):
                    # заменяем текущее значение ключа type на новое value
                    oper[str(type)] = value

                    # если пользователь выбрал ключ category, то изменяем баланс в нужную сторону
                    if str(type) == 'category':
                        # если меняем категорию на profit то увеличиваем баланс на сумму, указанную в oper['summa']
                        if value == 'profit':
                            Wallet.change_balance(self, oper['summa'])
                        # если меняем категорию на expenses то уменьшаем баланс на сумму, указанную в oper['summa']
                        elif value == 'expenses':
                            Wallet.change_balance(self, (-1 * oper['summa']))

                    path.write_text(json.dumps(data), encoding='utf-8')
        print('Note changed')

# получаем имя пользователя и создаем объект класса
text = str(input('What is your name? '))
user = Wallet(text)
print('You can use theese commands: \n'
      ' -show_balance() - to show balance \n'
      ' -change_balance(value) - to change balance (value - integer)\n'
      ' -show_operation(type) - to show list of operations ("profit"/"expenses")\n'
      ' -search_info(info) - to show more about info ("info")\n'
      ' -add_operation(date, category, summa, description) - add new operation (summa - integer, other string type)\n'
      ' -change_note(id, type, value) - to change note by note id (type - string, id - integer)\n'
      ' -stop - to stop code.')

while text != 'stop':
    # получаем команду, которую необходимо выполнить
    text = str(input('What are you want to do? '))

    # попытка выполнить функцию, при ошибке, выводит соответствующее уведомление
    try:
        exec('user.' + text)
    except:
        if text != 'stop':
            print('Wrong command')
        continue
