def cumsum_and_erase(A, erase = 1):
    B = [0]
    for i in A:
        sum = B[-1] + i
        B.append(sum)

    C = B[1::]
    for i in C:
        if i == erase:
            C.remove(i)
    return C

# Все правильно, еще можно сделать с экономией памяти под массив.
# Мы создаем массив и записываем в него только те элементы
# которые в нем останутся.
# Принесет пользу, только если массив будет очень большим, а
# erase элементов будет очень много:

# def cumsum_and_erase(A, erase = 1):
#     B = []
#     summa = 0
#     for i in A:
#         summa += i
#         if summa != erase:
#             B.append(summa)

#     return B