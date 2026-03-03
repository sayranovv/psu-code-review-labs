'''
несоответствия в исходнике:
- отступы пробелами вместо табуляции
- нет docstring у класса, методов и функции
- длинные строки больше 64 символов
- использовались двойные кавычки без необходимости

что исправлено:
- отступы переведены на табы
- добавлены docstring
- длинные строки разбиты
- кавычки приведены к одинарным
'''


class ClientActivity:
	'''хранит запись о занятиях клиента фитнес-центра.'''

	def __init__(self, duration, client_id, year, month):
		'''создаёт объект активности клиента.'''
		self.duration = duration
		self.client_id = client_id
		self.year = year
		self.month = month

	def is_less_than(self, other):
		'''сравнивает по длительности и затем по ранней дате.'''
		if self.duration != other.duration:
			return self.duration < other.duration
		return (self.year, self.month) < (other.year, other.month)



def find_min_activity(data):
	'''возвращает запись с минимальной длительностью.'''
	activities = []
	for entry in data:
		activity = ClientActivity(*entry)
		activities.append(activity)
	if not activities:
		raise ValueError('список данных пуст')
	best = activities[0]
	for activity in activities[1:]:
		if activity.is_less_than(best):
			best = activity
	return best



def main():
	'''выводит минимальную активность и дату из данных.'''
	data = [
		(3, 29, 2009, 7),
		(5, 20, 2005, 6),
		(3, 15, 2004, 12),
		(3, 10, 2003, 5),
		(1, 25, 2007, 3),
		(3, 30, 2005, 1),
	]
	result = find_min_activity(data)
	print('минимальная продолжительность:')
	print(result.duration, result.year, result.month)


if __name__ == '__main__':
	main()
