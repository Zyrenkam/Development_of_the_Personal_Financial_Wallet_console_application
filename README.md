# Development_of_the_Personal_Financial_Wallet_console_application

## Введение

Консольное приложение "Личный финансовый кошелек" осуществляет следующий набор функций:
  1. демонстрировать текущий баланс пользователя;
  2. изменять значение счета кошелька на указанную сумму;
  3. выводить список операций (Доход / Расход) по отдельности;
  4. искать информацию по ключевым словам;
  5. осуществлять поиск по категории, дате или сумме;
  6. добавлять новую запись, операцию;
  7. редактировать уже существующие записи.

## Запуск программы

Чтобы запустить модуль необходимо установить все файлы и запустить файл main.py через командную строку.

<code>C:\Users\PFWca> python main.py</code>

Файл info.json содержит информацию о существующих пользователях, а таакже их данные по операциям

## Работа приложения

При запуске программ спросит, кем вы являетесь, для продолжения нужно будет вписать имя. Тогда начнется проверка наличия вас в файле info.json и добавление.

<code>C:\Users\PFWca>python main.py
What is your name? Petya
User Petya added
You can use theese commands:
 -show_balance() - to show balance
 -change_balance(value) - to change balance (value - integer)
 -show_operation(type) - to show list of operations ("profit"/"expenses")
 -search_info(info) - to show more about info ("info")
 -add_operation(date, category, summa, description) - add new operation (summa - integer, other string type)
 -change_note(id, type, value) - to change note by note id (type - string, id - integer)
 -stop - to stop code.
What are you want to do?
</code>

Теперь, когда вы были найдены в базе или добавлены в нее, программа предлагает перечень команд, которые можно использовать:

1. show_balance()
   
   Показывает текущий баланс кошелька пользователя

   <code>What are you want to do? show_balance()
Your balance 0</code>
3. change_balance(value)
   
    Изменяет баланс пользователя на значение value. На вход принимает значение int.

    <code>What are you want to do? change_balance(1000)
Balance changed
What are you want to do? change_balance(-100)
Balance changed
What are you want to do? show_balance()
Your balance 900</code>

Мы дважды изменили баланс: в первый раз добавили 1000, во второй - забрали 100, таким образом, на счете осталось 0 + 1000 - 100 = 900.

3. add_operation(date, category, summa, description)

  Добавляет операцию, совершенную пользователем, записывая следующие параметры date - дата, str; category - категория (profit / expenses), str; summa - стоимость, int; description - описание, str.

  <code>What are you want to do? add_operation('09-09-2019', 'profit', '999', 'MONEY')
Balance changed
Operation added</code>

5. search_info(info)

  Поиск точного совпадения информации по категории, дате, сумме. На вход подается строковый тип. 

  <code>What are you want to do? search_info(999)
+----+------------+----------+-------+-------------+
| ID |    Date    | Category | Summa | Description |
+----+------------+----------+-------+-------------+
| 7  | 09-09-2019 |  profit  |  999  |    MONEY    |
+----+------------+----------+-------+-------------+</code>
  
6. show_operation(type)

  Вывод всех значений заданной категории, type принимает значения 'profit' / 'expenses'.

  <code>What are you want to do? show_operation('profit')
+----+------------+----------+-------+-------------+
| ID |    Date    | Category | Summa | Description |
+----+------------+----------+-------+-------------+
| 7  | 09-09-2019 |  profit  |  999  |    MONEY    |
+----+------------+----------+-------+-------------+</code>

7. change_note(id, type, value)

  Редактирование любой операции пользователя по id. id - int, уникальный номер операции; type - str, название параметра ('date', 'category', 'summa', 'description'); value - новое значение.

  <code>What are you want to do? change_note(7, 'date', '10-09-2011')
Note changed</code>

Посмотрим, что поменялось

<code>What are you want to do? show_operation('profit')
+----+------------+----------+-------+-------------+
| ID |    Date    | Category | Summa | Description |
+----+------------+----------+-------+-------------+
| 7  | 10-09-2011 |  profit  |  999  |    MONEY    |
+----+------------+----------+-------+-------------+</code>

8. stop

   <code>What are you want to do? stop
   C:\Users\PFWca></code>

   Завершение работы программы.

   
