import numpy as np

def run_length_encoding(arr):
    # вычисляем разницу между последующими элементами
    diff = np.diff(arr)
    print(diff)

    # находим индексы, где разница не равна 0
    idx = np.where(diff != 0)[0]
    print(idx)

    # прибавляем 1, т.к. основная индексация начинается с 0, и к концу добавляем общую длину массива
    idx = np.r_[idx, arr.size - 1]
    print(idx)

    # находим элементы
    elements = arr[idx]

    # находим количество повторений, учитывая, что numpy разчитывает индексы от 0
    counts = np.diff(np.r_[-1, idx])

    return (elements, counts)

arr = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
elements, counts = run_length_encoding(arr)

print('Elements:', elements)
print('Counts:', counts)

# отлично
# еще были прикольные решения на форуме решений )