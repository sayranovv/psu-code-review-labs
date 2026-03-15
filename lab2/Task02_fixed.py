# изменения по кодстайлу:
# - отступы только табами
# - имена в snake_case
# - добавлены докстроки с @param
# - строки сокращены


class Node:
	'''узел очереди.'''

	def __init__(self, data):
		'''создать узел.

		@param data: данные узла.
		'''
		self.data = data
		self.next = None


class Queue:
	'''очередь.'''

	def __init__(self):
		'''создать пустую очередь.'''
		self.head = None
		self.tail = None

	def is_empty(self):
		'''проверка пустоты.'''
		if self.head is None:
			return True
		return False

	def enqueue(self, data):
		'''добавить в конец.

		@param data: значение для добавления.
		'''
		new_node = Node(data)
		if self.is_empty():
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node

	def dequeue(self):
		'''удалить элемент из начала.'''
		if self.is_empty():
			raise IndexError('Очередь пуста')
		removed_node = self.head
		self.head = self.head.next
		if self.head is None:
			self.tail = None
		return removed_node.data

	def print_queue(self):
		'''печать очереди.'''
		current = self.head
		while current is not None:
			print(current.data, end=' ')
			current = current.next
		print()


def main():
	'''запуск задачи.'''
	queue1 = Queue()
	queue2 = Queue()

	num1 = int(
		input('Введите кол-во 1-й '
			  'очереди: ')
	)
	for index in range(num1):
		prompt = f'Введите элемент {index + 1} 1-й: '
		queue1.enqueue(input(prompt))

	num2 = int(
		input('Введите кол-во 2-й '
			  'очереди: ')
	)
	for index in range(num2):
		prompt = f'Введите элемент {index + 1} 2-й: '
		queue2.enqueue(input(prompt))

	print('Первая очередь '
		  'до перемещения:')
	queue1.print_queue()
	print('Вторая очередь '
		  'до перемещения:')
	queue2.print_queue()

	a1 = queue1.head
	a2 = queue1.tail
	a4 = queue2.tail

	if not queue1.is_empty():
		if queue2.is_empty():
			queue2.head = a1
			queue2.tail = a2
		else:
			a4.next = a1
			queue2.tail = a2
		queue1.head = None
		queue1.tail = None
	else:
		print(
			'Первая очередь пуста, '
			'перемещать нечего'
		)

	print('Вторая очередь '
		  'после перемещения:')
	queue2.print_queue()

	if queue2.head is not None:
		print(
			'Новое начало второй '
			'очереди:',
			queue2.head.data,
		)
		print(
			'Ссылка на начало '
			'второй очереди:',
			queue2.head,
		)
	else:
		print('Вторая очередь пуста')

	if queue2.tail is not None:
		print(
			'Новый конец второй '
			'очереди:',
			queue2.tail.data,
		)
		print(
			'Ссылка на конец '
			'второй очереди:',
			queue2.tail,
		)
	else:
		print('Вторая очередь пуста')


if __name__ == '__main__':
	main()
