"""
B. Прожекторы
ограничение по времени на тест
1 секунда
ограничение по памяти на тест
256 мегабайт
ввод
стандартный ввод
вывод
стандартный вывод

Театральная сцена представляет собой прямоугольное поле размером n × m. Директор театра выдал вам план сцены, согласно
которому на ней будут располагаться актёры. На плане отмечено в каких клетках будут стоять актёры, а в каких нет.

Прожектор, установленный на сцену, будет светить в одном из четырёх направлений (если смотреть на план сцены сверху) —
влево, вверх, вправо или вниз. Таким образом, под позицией прожектора понимается клетка,
в которую он установлен, а также направление, в котором он светит.

Перед вами стоит задача поставить на сцену прожектор в хорошую позицию.
Позиция называется хорошей, если одновременно выполняются два условия:

    в соответствующей ей клетке нет актёра;
    в направлении, в котором светит прожектор, находится хотя бы один актёр.

Перед вами стоит задача посчитать количество хороших позиций для установки прожектора.
Две позиции установки прожектора считаются различными, если отличаются клетки расположения прожектора,
или направление, в котором он светит.
Входные данные

В первой строке следует два целых положительных числа n и m (1 ≤ n, m ≤ 1000) —
количество строк и количество столбцов в плане.

В следующих n строках следует по m целых чисел, каждое равно либо 0, либо 1, —
описание плана. Если очередное число равно 1, то в соответствующей клетке находится актёр,
а если 0, то клетка останется пустой. Гарантируется, что в плане есть хотя бы один актёр.
Выходные данные

Выведите единственное целое число — количество хороших позиций для установки прожектора.
Примеры
Входные данные

2 4
0 1 0 0
1 0 1 0

Выходные данные

9

Входные данные

4 4
0 0 0 0
1 0 0 1
0 1 1 0
0 1 0 0

Выходные данные

20

Примечание

В первом примере хорошими позициями для установки прожектора являются:

    клетка (1, 1) и направление вправо;
    клетка (1, 1) и направление вниз;
    клетка (1, 3) и направление влево;
    клетка (1, 3) и направление вниз;
    клетка (1, 4) и направление влево;
    клетка (2, 2) и направление влево;
    клетка (2, 2) и направление вверх;
    клетка (2, 2) и направление вправо;
    клетка (2, 4) и направление влево.

Таким образом, в данном примере всего 9 хороших позиций.
"""
print('Test first example.')


def count_neighbors(row, col):
    result = 0
    temp_offset = 1
    while (row - temp_offset) >= 0:
        if input_array[row - temp_offset][col] == 1:  # North
            result += 1
            break
        temp_offset += 1
    temp_offset = 1
    while (col - temp_offset) >= 0:
        if input_array[row][col - temp_offset] == 1:  # West
            result += 1
            break
        temp_offset += 1
    temp_offset = 1
    while (row + temp_offset) < len(input_array):
        if input_array[row + temp_offset][col] == 1:  # South
            result += 1
            break
        temp_offset += 1
    temp_offset = 1
    while (col + temp_offset) < len(input_array[row]):
        if input_array[row][col + temp_offset] == 1:  # East
            result += 1
            break
        temp_offset += 1
    return result


def count_best_positions():
    result = 0
    for i in range(len(input_array)):
        for j in range(len(input_array[i])):
            if input_array[i][j] != 1:
                result += count_neighbors(i, j)
    return result


input_array = []
with open('./example_1.txt') as file:
    count_rows = int(file.readline().split()[0])
    for number_row in range(count_rows):
        input_array.append([int(cell) for cell in file.readline().split()])

print('Count best positions on first example = %s' % (count_best_positions()))
input_array = []
with open('./example_2.txt') as file:
    count_rows = int(file.readline().split()[0])
    for number_row in range(count_rows):
        input_array.append([int(cell) for cell in file.readline().split()])
print('Count best positions on second example = %s' % (count_best_positions()))

print('THE END.')
