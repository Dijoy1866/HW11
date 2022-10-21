
#Задание #2:
'''Права доступа
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.

Пример ввода:
3
python.exe X
book.txt R W
notebook.exe R W X

5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt

Пример вывода:
Access denied
OK
OK
OK
OK
'''

n = int(input('количество запросов к файлам: '))
keys = {'write': 'W', 'read': 'R', 'execute': 'X'}
A = {}

for i in range(n):
    a, b = input('введите имя файла и права доступа к файлу: ').split()
    A[a] = b

m = int(input('количество запросов к файлам: '))

for i in range(m):
    c, d = input('введите разрешение для файла и имя файла: ').split()
    if keys[c] in A[d]:
        print('ok')
    else:
        print('Access denied')



