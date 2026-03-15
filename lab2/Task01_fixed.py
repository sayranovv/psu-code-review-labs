# изменения по кодстайлу:
# - отступы только табами
# - имена в snake_case
# - добавлены докстроки с @param
# - строки сокращены
# - вершина вынесена в константу


INITIAL_STACK_TOP = 100


class Node:
	'''узел списка.'''

	def __init__(self, data, next_node=None):
		'''создать узел.

		@param data: данные узла.
		@param next_node: следующий узел.
		'''
		self.data = data
		self.next = next_node

	def __str__(self):
		'''строка узла.'''
		return str(self.data)


class Stack:
	'''стек.'''

	def __init__(self):
		'''создать пустой стек.'''
		self.head = None

	def is_empty(self):
		'''проверить, пуст ли стек.'''
		if self.head is None:
			return True
		return False

	def push(self, data):
		'''положить элемент.

		@param data: добавляемое значение.
		'''
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def pop(self):
		'''снять элемент с вершины.'''
		if self.is_empty():
			print('Ошибка: Стек пуст!')
			return None
		popped_node = self.head
		self.head = self.head.next
		popped_node.next = None
		return popped_node.data

	def peek(self):
		'''вернуть вершину без удаления.'''
		if self.is_empty():
			return None
		return self.head.data


def main():
	'''запуск задачи.'''
	stack = Stack()
	stack.push(INITIAL_STACK_TOP)
	print(
		'Исходна вершина '
		'стека A1:',
		stack.head,
	)

	while True:
		try:
			value_d = float(input('Введите число D: '))
			break
		except ValueError:
			print('Ошибка! Повторная попытка...')

	stack.push(value_d)
	a2 = stack.head
	print('Новая вершина стека A2:', a2)


if __name__ == '__main__':
	main()
