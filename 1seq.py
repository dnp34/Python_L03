Num = int(input('\nВведите количество элементов будущего списка: '))
List = []
print('Вводите любые цифры по одной.')
for i in range(Num):
    List.append(int(input(f'Введите {i + 1} элемент: ')))
print(sorted(List))
