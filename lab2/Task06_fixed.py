# изменения по кодстайлу:
# - отступы только табами
# - имена в snake_case
# - добавлены докстроки с @param
# - строки сокращены
# - барьер вынесен в константу


import random


ELEMENTS_MIN = 10
ELEMENTS_MAX = 20
VALUE_MIN = 1
VALUE_MAX = 50
BARRIER_VALUE = 0


class Node:
	'''узел двусвязного списка.'''

	def __init__(self, data=None, prev_node=None, next_node=None):
		'''создать узел.

		@param data: данные узла.
		@param prev_node: предыдущий узел.
		@param next_node: следующий узел.
		'''
		self.data = data
		self.prev = prev_node
		self.next = next_node

	def __str__(self):
		'''строка узла.'''
		return str(self.data)


class IntListB:
	'''барьерный двусвязный список.'''

	def __init__(self, a_barrier, a_current=None):
		'''создать список.

		@param a_barrier: барьерный узел.
		@param a_current: текущий узел.
		'''
		self._barrier = a_barrier
		self._current = a_current

	def insert_last(self, value_d):
		'''вставить в конец.

		@param value_d: добавляемое значение.
		'''
		new_node = Node(value_d)
		new_node.prev = self._barrier.prev
		new_node.next = self._barrier
		self._barrier.prev.next = new_node
		self._barrier.prev = new_node
		self._current = new_node

	def put(self):
		'''вернуть текущий узел.'''
		return (
			'Ссылка на текуший '
			f'элемент списка: {self._current}'
		)

	def to_last(self):
		'''сместить на хвост.'''
		if self._barrier.prev != self._barrier:
			self._current = self._barrier.prev

	def to_prev(self):
		'''сместить назад.'''
		if self._barrier.next != self._barrier:
			self._current = self._current.prev

	def get_data(self):
		'''вернуть данные текущего.'''
		return int(self._current.data)

	def is_barrier(self):
		'''текущий - барьер?'''
		if self._current == self._barrier:
			return True
		return False

	def print_all(self):
		'''печать всех узлов.'''
		current = self._barrier.next
		while current != self._barrier:
			print(str(current.data), end=', ')
			current = current.next
		print()


def main():
	'''запуск задачи.'''
	barrier = Node(BARRIER_VALUE)
	barrier.next = barrier
	barrier.prev = barrier
	int_list_b = IntListB(barrier, barrier)

	elements = [
		random.randint(VALUE_MIN, VALUE_MAX)
		for _ in range(random.randint(ELEMENTS_MIN, ELEMENTS_MAX))
	]
	for elem in elements:
		int_list_b.insert_last(elem)

	print('Исходный список:')
	int_list_b.print_all()
	print(int_list_b.put())

	int_list_b.to_last()
	count = 0
	print('Четные элементы списка:')
	while not int_list_b.is_barrier():
		data = int_list_b.get_data()
		if data % 2 == 0:
			print(data, end=', ')
		count += 1
		int_list_b.to_prev()
	print()
	print(
		'Количество элементов '
		f'в списке: {count}'
	)


if __name__ == '__main__':
	main()
