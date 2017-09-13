from datetime import datetime
import random


def insert_sort(list):
    lenth = len(list)
    for i in range(1, lenth):
        key = list[i]
        j = i
        while (j >= 0):
            if (key < list[j]):
                list[j + 1] = list[j]
                list[j] = key
            j -= 1
    return list


def quick_sort(list):
    quick_part(list, 0, len(list)-1)


def quick_part(list, l, r):
    i = l
    j = r
    if i > j:
        return
    posi = list[i]
    while i < j:
        while i < j and posi <= list[j]:
            j -= 1
        if i < j:
            list[i] = list[j]
            i += 1
        while i < j and posi >= list[i]:
            i += 1
        if i < j:
            list[j] = list[i]
            j -= 1
    list[i] = posi
    quick_part(list, l, i - 1)
    quick_part(list, i + 1, r)


def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists


def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)


def build_heap(lists, size):
    for i in range(0, int(size / 2))[::-1]:
        adjust_heap(lists, i, size)


def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)


a = []
for i in range(0,1000):
    a.append(random.randint(0,1000))
start = datetime.now()
print('运行结果', insert_sort(a))
delay = datetime.now() - start
print('插入排序运行时间为：', delay)

start = datetime.now()
print('运行结果', insert_sort(a))
delay = datetime.now() - start
print('希尔排序运行时间为：', delay)

b = []
for i in range(0,1000):
    b.append(random.randint(0,1000))
start = datetime.now()
quick_sort(b)
print('运行结果', b)
delay = datetime.now() - start
print('快速排序运行时间为：', delay)

b = []
for i in range(0,1000):
    b.append(random.randint(0,1000))
start = datetime.now()
heap_sort(b)
print('运行结果', b)
delay = datetime.now() - start
print('堆排序运行时间为：', delay)