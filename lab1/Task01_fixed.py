'''
несоответствия в исходнике:
- отступы пробелами вместо табуляции
- длинные строки более 64 символов
- нет docstring у функции
- комментарии стояли в конце строк
- ошибки форматирования пробелов
- алгоритм находил лишние подпоследовательности

что исправлено:
- отступы переведены на табы
- строки укорочены до лимита
- добавлены docstring
- комментарии убраны или вынесены отдельно
- пробелы и кавычки приведены к стилю
- реализован корректный поиск серий убывания
'''

import os


class DecreasingSeriesWriter:
	'''строит длины убывающих серий и пишет их в файл.'''

	def get_series_lengths(self, numbers):
		'''возвращает длины всех серий строгого убывания.'''
		lengths = []
		current = 1
		index = 1
		while index < len(numbers):
			if numbers[index] < numbers[index - 1]:
				current += 1
			else:
				if current > 1:
					lengths.append(current)
				current = 1
			index += 1
		if current > 1:
			lengths.append(current)
		return lengths

	def read_numbers(self, file_name):
		'''читает вещественные числа из csv-строки файла.'''
		with open(file_name, 'r', encoding='utf-8') as source:
			text = source.read().strip()
		if not text:
			return []
		parts = text.split(',')
		return [float(item.strip()) for item in parts]

	def write_lengths(self, file_name, lengths):
		'''записывает длины серий в выходной файл.'''
		result = ', '.join(str(item) for item in lengths)
		with open(file_name, 'w', encoding='utf-8') as target:
			target.write(result)



def main():
	'''запускает обработку входного и выходного файла.'''
	input_file = input('введите название входного файла: ')
	output_file = input('введите название выходного файла: ')

	if not os.path.exists(input_file):
		print(f'файла {input_file} не существует')
		return

	writer = DecreasingSeriesWriter()
	numbers = writer.read_numbers(input_file)
	lengths = writer.get_series_lengths(numbers)
	writer.write_lengths(output_file, lengths)
	print(f'длины серий записаны в файл {output_file}')


if __name__ == '__main__':
	main()
