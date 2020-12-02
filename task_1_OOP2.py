"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""

#это решение -  переработка первого примера с нечзначительным доавблением ООП

from collections import Counter, deque


class Node:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def haff_tree(s):
    elems_count = Counter(s)
    # можно было бы взять вместо deque список, однако, учитывая скорость, deque будет лучше
    elems_sort = deque(sorted(elems_count.items(), key=lambda x: x[1]))
    # идем по массиву, пока не останется последний элемент
    while len(elems_sort) > 1:
        # берем первые два элемента
        root = elems_sort[0][1] + elems_sort[1][1]
        node = Node(left=elems_sort.popleft()[0], right=elems_sort.popleft()[0])
        # цикл заменен на добавление нового элемента в начало и сортировку
        elems_sort.appendleft((node, root))
        elems_sort = deque(sorted(elems_sort, key=lambda x: x[1]))
    return elems_sort[0][0]
# {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}


code_table = dict()


def elems_code(inp, path=''):
    if not isinstance(inp, Node):
        code_table[inp] = path

    else:
        elems_code(inp.left, path=f'{path}0')
        elems_code(inp.right, path=f'{path}1')


s = "beep boop beer!"
elems_code(haff_tree(s))
'''{'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}'''
# 00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001


for i in s:
    print(code_table[i], end=' ')
