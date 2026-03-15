# изменения по кодстайлу:
# - отступы только табами
# - имена в snake_case
# - добавлены докстроки с @param
# - строки сокращены
# - диапазоны вынесены в константы


import random


SIZE_MIN = 1
SIZE_MAX = 5
RANDOM_MIN = 1
RANDOM_MAX = 20


class Node:
	'''узел двусвязного списка.'''

	def __init__(self, data, prev_node=None, next_node=None):
		'''создать узел.

		@param data: данные узла.
		@param prev_node: предыдущий узел.
		@param next_node: следующий узел.
		'''
		self.data = data
		self.prev = prev_node
		self.next = next_node


def concatenate_lists(a1, a2, a0):
	'''склеить два списка.

	@param a1: голова первого списка.
	@param a2: хвост первого списка.
	@param a0: узел второго списка.
	'''
	if a1 is None:
		return a0, find_last(a0)
	if a0 is None:
		return a1, a2

	print(
		'\nВставка перед узлом '
		'со значением: '
		f'{a0.data}'
	)

	if a0.prev is not None:
		a0.prev.next = a1
	a1.prev = a0.prev
	a0.prev = a2
	a2.next = a0

	if a1.prev is None:
		first_node = a1
	else:
		first_node = find_first(a0)
	last_node = find_last(a0)
	return first_node, last_node


def find_last(node):
	'''найти последний элемент.

	@param node: стартовый узел.
	'''
	if node is None:
		return None
	while node.next is not None:
		node = node.next
	return node


def find_first(node):
	'''найти первый элемент.

	@param node: стартовый узел.
	'''
	if node is None:
		return None
	while node.prev is not None:
		node = node.prev
	return node


def create_random_doubly_linked_list(
	size,
	min_val=RANDOM_MIN,
	max_val=RANDOM_MAX,
):
	'''создать случайный список.

	@param size: размер списка.
	@param min_val: минимум диапазона.
	@param max_val: максимум диапазона.
	'''
	if size <= 0:
		return None, None
	head = Node(random.randint(min_val, max_val))
	tail = head
	for _ in range(size - 1):
		new_node = Node(
			random.randint(min_val, max_val),
			prev_node=tail,
		)
		tail.next = new_node
		tail = new_node
	return head, tail


def print_list(head):
	'''печать списка.

	@param head: голова списка.
	'''
	current = head
	while current is not None:
		print(current.data, end=' ')
		current = current.next
	print()


def pick_random_node(head, size):
	'''выбрать случайный узел.

	@param head: голова списка.
	@param size: длина списка.
	'''
	current = head
	steps = random.randint(0, size - 1)
	for _ in range(steps):
		if current.next is not None:
			current = current.next
	return current


def main():
	'''запуск задачи.'''
	size1 = random.randint(SIZE_MIN, SIZE_MAX)
	size2 = random.randint(SIZE_MIN, SIZE_MAX)
	a1, a2 = create_random_doubly_linked_list(size1)
	b1, _ = create_random_doubly_linked_list(size2)
	a0 = pick_random_node(b1, size2)

	print('Первый список:')
	print_list(a1)
	print('Второй список:')
	print_list(b1)

	first_node, last_node = concatenate_lists(a1, a2, a0)

	print('\nОбъединенный список:')
	print_list(first_node)

	if first_node is None:
		first_value = 'None'
	else:
		first_value = first_node.data

	if last_node is None:
		last_value = 'None'
	else:
		last_value = last_node.data

	print(
		'\nНачало объединенного '
		f'списка: {first_value}'
	)
	print(
		'Конец объединенного '
		f'списка: {last_value}'
	)


if __name__ == '__main__':
	main()
