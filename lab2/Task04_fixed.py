# изменения по кодстайлу:
# - отступы только табами
# - имена в snake_case
# - добавлены докстроки с @param
# - строки сокращены
# - данные в константы


INITIAL_VALUES = (3, 4, 7, 9, 7, 8)
INSERT_STEP = 3


class Node:
	'''узел списка.'''

	def __init__(self, data=None, next_node=None):
		'''создать узел.

		@param data: данные узла.
		@param next_node: следующий узел.
		'''
		self.data = data
		self.next = next_node

	def __str__(self):
		'''строка узла.'''
		return str(self.data)


class Queue:
	'''список с добавлением в конец.'''

	def __init__(self):
		'''создать пустой список.'''
		self.head = None

	def push(self, data):
		'''добавить в конец.

		@param data: значение для добавления.
		'''
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		current = self.head
		while current.next is not None:
			current = current.next
		current.next = new_node

	def print_queue(self):
		'''печать списка.'''
		current = self.head
		while current is not None:
			print(current, end=' ')
			current = current.next
		print()


def main():
	'''запуск задачи.'''
	one = Queue()
	for value in INITIAL_VALUES:
		one.push(value)

	p1 = one.head
	m_value = input('Введите M -> ')
	try:
		m_value = int(m_value)
	except ValueError:
		print('M должно быть целым числом')
		return

	print('Изначальный список: ', end='')
	one.print_queue()

	count = 0
	while p1 is not None:
		count += 1
		if count % INSERT_STEP == 0:
			inserted = Node(m_value)
			inserted.next = p1.next
			p1.next = inserted
			p1 = inserted
		p1 = p1.next

	print('Итоговый список: ', end='')
	one.print_queue()

	p2 = one.head
	while p2 is not None and p2.next is not None:
		p2 = p2.next

	if p2 is not None:
		print(
			'Значение последнего '
			f'элемента: {p2.data}'
		)
		print(
			'Ссылка на последний '
			f'элемент: {one}'
		)


if __name__ == '__main__':
	main()
