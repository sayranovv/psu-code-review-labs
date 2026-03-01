'''File48. Даны три бинарных файла целых чисел одинакового размера с именами SA, SB, SC и строка SD.Создать новый файл с именем SD, в котором чередовались бы элементы исходных файлов
 с одним и тем же номером:
A1, B1, C1, A2, B2, C2, … .'''

import struct

try:
	SD = input('Введите название файла: ')

	def reader(filename):
		numbers = []
		#чтение данных из файла и перевод в десятичную систему счисления
		with open(filename, 'rb') as file:
			while True:
				bytes_read = file.read(4)

				if not bytes_read:
					break
				num = struct.unpack('i', bytes_read)[0]
				numbers.append(num)
			file.close()

		return numbers

	SA = reader('SA.bin')
	SB = reader('SB.bin')
	SC = reader('SC.bin')

	print('SA: ', ', '.join(map(str, SA)))
	print('SB: ',', '.join(map(str, SB)))
	print('SC: ',', '.join(map(str, SC)))

	nums = []


	for i in range(len(SA)):
		nums.append(SA[i])
		nums.append(SB[i])
		nums.append(SC[i])


	with open(SD, 'wb') as file:
		for number in nums:
			file.write(struct.pack('i', number))
		file.close()

	numbers = reader(SD)
	srt_nums = ', '.join(map(str, numbers))
	print(f'\nФайл после объединения:\n{srt_nums}\n')

except:
	print('Неверный ввод')