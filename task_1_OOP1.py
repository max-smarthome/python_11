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
#данный пример я нашёл в интернете, долго его разбирал,  только из-за потраченного времени решил его воспроизвести.

import heapq
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Nd", ["lft", "rght"])):
    def tree_expl(self, cd, acc):
        self.lft.tree_expl(cd, acc + "0")
        self.rght.tree_expl(cd, acc + "1")


class Leaf(namedtuple("Lf", ["chr"])):
    def tree_expl(self, cd, acc):
        cd[self.chr] = acc or "0"


def huff_encode(s):
    deq = []
    for ch, frequence in Counter(s).items():
        deq.append((frequence, len(deq), Leaf(ch)))
    heapq.heapify(deq)
    count = len(deq)
    while len(deq) > 1:
        frequence1, _count1, left = heapq.heappop(deq)
        frequence2, _count2, right = heapq.heappop(deq)
        heapq.heappush(deq, (frequence1 + frequence2, count, Node(left, right)))
        count += 1
    code = {}
    if deq:
        [(_freq, _count, root)] = deq
        root.tree_expl(code, "")
    return code


s = input('Строка ')
code = huff_encode(s)
for i in s:
    print(code[i], end = ' ')


