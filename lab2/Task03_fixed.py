# изменения по кодстайлу:
# - отступы только табами
# - имена в snake_case
# - добавлены докстроки с @param
# - строки сокращены
# - демо в константы


UNDERFLOW_TEXT = 'Stack Underflow'
TARGET_INDEX = 9
INITIAL_VALUE = 1
DEMO_LENGTH = 12


class Node:
	'''узел списка.'''

	def __init__(self, data):
		'''создать узел.

		@param data: данные узла.
		'''
		self.data = data
		self.next = None


class LinkedList:
	'''односвязный список.'''

	def __init__(self):
		'''создать пустой список.'''
		self.head = None
		self.tail = None

	def add_head(self, data):
		'''добавить в начало.

		@param data: значение для добавления.
		'''
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			return
		new_node.next = self.head
		self.head = new_node

	def add_tail(self, data):
		'''добавить в конец.

		@param data: значение для добавления.
		'''
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			return
		self.tail.next = new_node
		self.tail = new_node

	def delete_tail(self):
		'''удалить хвост.'''
		if self.head is None:
			return
		if self.head.next is None:
			self.head = None
			self.tail = None
			return
		current = self.head
		while current.next.next is not None:
			current = current.next
		current.next = None
		self.tail = current

	def delete_head(self):
		'''удалить голову.'''
		if self.head is None:
			return
		self.head = self.head.next
		if self.head is None:
			self.tail = None

	def display(self):
		'''показать список.'''
		iter_node = self.head
		if self.head is None:
			print(UNDERFLOW_TEXT)
			return
		while iter_node is not None:
			print(iter_node.data, end='')
			iter_node = iter_node.next
			if iter_node is not None:
				print(' -> ', end='')

	def find_ninth(self):
		'''найти 9-й элемент.'''
		iter_node = self.head
		if self.head is None:
			print(UNDERFLOW_TEXT)
			return None
		count = 1
		while iter_node is not None and count != TARGET_INDEX:
			iter_node = iter_node.next
			count += 1
		print(iter_node)
		if iter_node is None:
			return None
		return iter_node.data


def main():
	'''запуск задачи.'''
	linked_list = LinkedList()
	value = INITIAL_VALUE
	for _ in range(DEMO_LENGTH):
		linked_list.add_tail(value)
		value += 1
	linked_list.display()
	print('')
	linked_list.find_ninth()


if __name__ == '__main__':
	main()
