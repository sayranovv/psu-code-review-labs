#File23. Дан файл вещественных чисел. Создать файл целых чисел, содержащий длины всех убывающих последовательностей элементов исходного файла.
# Например, для исходного файла с элементами 1.7, 4.5, 3.4, 2.2, 8.5, 1.2 содержимое результирующего файла должно быть следующим: 3, 2.

import os

def find_decreasing_subsequences(nums):
    n = len(nums)
    lengths = []
    #Итерируемся по списку, чтобы найти убывающие последовательности
    for i in range(n):
        current_length = 1  # Начинаем с первого элемента
        for j in range(i + 1, n):
            if nums[j] < nums[j - 1]:  # Проверяем на убывание
                current_length += 1
            else:
                break  # Останавливаемся, если последовательность больше не убывает
        if current_length > 1:  # Учитываем только длины больше 1
            lengths.append(current_length)
    return lengths

input_file = input('Введите название входного файла: ')
output_file = input('Введите название выходного файла: ')

if not os.path.exists(input_file): #Через модуль os.path проверяем наличие файла по его названию. Если не существует, то вывод соответствующего сообщения пользователю
    print(f'Файла {input_file} не существует. Попробуйте снова')
else:
    with open(input_file,'r') as f:
        numbers = list(map(float,f.read().strip().split(','))) #Создаем список номеров
    decreas_lenght = find_decreasing_subsequences(numbers) #Возвращаем длины убывающей последовательности наших номеров
    with open(output_file,'w') as f:
        f.write(', '.join(map(str,decreas_lenght)))#Записываем в файл через запятую с пробелом наши длины

    print(f'Длины убывающей последовательности записаны в файл {output_file}')