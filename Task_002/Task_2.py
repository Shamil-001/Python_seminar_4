# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_index_in_range(arr, min_val, max_val):
    index = [i for i in range(len(arr)) if min_val <= arr[i] <= max_val]
    return index

arr = [3, 7, 12, 5, 9, 15, 2, 8]
min_val = int(input("Введите наименьшее значение: "))
max_val = int(input("Введите наибольшее значение: "))
result = find_index_in_range(arr, min_val, max_val)
print("Индексы элементов в диапазоне от", min_val, "до", max_val, ":", result)