#!usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
import matplotlib.pyplot as plt
import random



def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Проверяем, является ли левый потомок больше родителя
    if left < n and arr[i] < arr[left]:
        largest = left

    # Проверяем, является ли правый потомок больше родителя или левого потомка
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Если дочерний элемент больше родительского, меняем их местами и продолжаем сортировку
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Создаем максимальную кучу
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Перемещаем максимальный элемент в конец массива и снова создаем максимальную кучу
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def ever_sort_gph():
    x = []
    y = []

    for i in range(50, 500, 50):
        x.append(i)
        arr = [j for j in range(i)]
        execution_time = timeit.timeit(lambda: heapSort(arr), number=1000)
        y.append(execution_time)
    create_grf(x, y, "TITLE", "X", "Y")


def worst_sort_gph():
    x = []
    y = []

    for i in range(50, 500, 50):
        x.append(i)
        arr = [j for j in range(i, 0, -1)]
        execution_time = timeit.timeit(lambda: heapSort(arr), number=1000)
        y.append(execution_time)
    create_grf(x, y, "TITLE", "X", "Y")

def gen_list(n):
    nums = []
    for _ in range(n):
        nums.append(random.randint(1, 100))
    return nums

def sr_sort_gph():
    x = []
    y = []

    for i in range(100, 10000, 100):
        x.append(i)
        arr = gen_list(i)
        execution_time = timeit.timeit(lambda: heapSort(arr), number=2)
        y.append(execution_time)
    create_grf(x, y, "TITLE", "X", "Y")

def create_grf(x, y, name_of_graph, name_x, name_y):
    plt.plot(x, y, 'o-')

    plt.xlabel(name_x)
    plt.ylabel(name_y)
    plt.title(name_of_graph)

    plt.show()

def main():
    arr = [12, 11, 13, 5, 6, 7]
    # Измеряем время выполнения сортировки кучей
    execution_time = timeit.timeit(lambda: heapSort(arr), number=1000)

    sr_sort_gph()
    # Выводим результат
    print("Время выполнения сортировки кучей:", execution_time)

if __name__ == "__main__":
    main()