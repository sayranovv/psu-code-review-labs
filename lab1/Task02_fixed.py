'''task02 fixed.

несоответствия в исходнике:
- смешанное форматирование и лишние пустые строки.
- нет docstring у функции.
- имена переменных в стиле констант для обычных данных.
- лишние close внутри with.
- слишком общий except.
- нет проверки равенства размеров файлов.

что исправлено:
- форматирование приведено к единому стилю.
- добавлены docstring.
- имена переменных приведены к snake_case.
- удалены лишние close.
- добавлена проверка входных данных.
- ошибки обрабатываются типизированно.
'''

import struct


class BinaryFilesMerger:
	'''объединяет три бинарных файла по индексам.'''

	def read_ints(self, file_name):
		'''читает целые числа из бинарного файла.'''
		numbers = []
		with open(file_name, 'rb') as source:
			while True:
				chunk = source.read(4)
				if not chunk:
					break
				number = struct.unpack('i', chunk)[0]
				numbers.append(number)
		return numbers

	def merge_by_index(self, first, second, third):
		'''чередует элементы списков с одинаковыми индексами.'''
		if not len(first) == len(second) == len(third):
			raise ValueError('входные файлы должны быть одного размера')
		merged = []
		for index in range(len(first)):
			merged.append(first[index])
			merged.append(second[index])
			merged.append(third[index])
		return merged

	def write_ints(self, file_name, numbers):
		'''записывает целые числа в бинарный файл.'''
		with open(file_name, 'wb') as target:
			for number in numbers:
				target.write(struct.pack('i', number))



def main():
	'''выполняет чтение, объединение и запись файлов.'''
	output_name = input('введите название выходного файла: ')
	merger = BinaryFilesMerger()
	try:
		first = merger.read_ints('SA.bin')
		second = merger.read_ints('SB.bin')
		third = merger.read_ints('SC.bin')
		merged = merger.merge_by_index(first, second, third)
		merger.write_ints(output_name, merged)
		result = ', '.join(str(item) for item in merged)
		print(f'файл после объединения: {result}')
	except FileNotFoundError as error:
		print(f'файл не найден: {error.filename}')
	except ValueError as error:
		print(f'ошибка данных: {error}')


if __name__ == '__main__':
	main()
