# изменения по кодстайлу:
# - исправлены имена и типизация
# - добавлены/заменены docstring с @param
# - добавлена обработка исключений
# - генерация данных через random
# - добавлен класс DoublyList, в исходном коде был только Node,
# 	а логика работы с ним была разбросана по функциям
# - объединение без новых Node
# - добавлено преобразование списка в обычный для удобства вывода
# - concatenate_lists(A1, A2, A0) → merge_before_node(first_list,
# 	second_list, a0): принимает объекты списков, а не отдельные узлы A1/A2

import random


class Node:
	'''узел двусвязного списка.

	@param data: значение узла.
	@param prev_node: предыдущий узел.
	@param next_node: следующий узел.
	'''

	def __init__(
		self,
		data: int,
		prev_node: 'Node | None' = None,
		next_node: 'Node | None' = None,
	) -> None:
		'''создать узел.

		@param data: значение узла.
		@param prev_node: предыдущий узел.
		@param next_node: следующий узел.
		'''
		self.data: int = data
		self.prev: Node | None = prev_node
		self.next: Node | None = next_node

	def __str__(self) -> str:
		'''вернуть строку узла.

		@param self: экземпляр класса.
		'''
		return f'Node(data={self.data})'


class DoublyList:
	'''двусвязный список.

	@param head: начало списка.
	@param tail: конец списка.
	'''

	def __init__(self) -> None:
		'''создать пустой список.

		@param self: экземпляр класса.
		'''
		self.head: Node | None = None
		self.tail: Node | None = None

	def append(self, data: int) -> None:
		'''добавить элемент в конец.

		@param data: добавляемое значение.
		'''
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.tail = new_node
			return
		if self.tail is None:
			raise RuntimeError('Список поврежден')
		new_node.prev = self.tail
		self.tail.next = new_node
		self.tail = new_node

	def to_list(self) -> list[int]:
		'''вернуть значения списка.

		@param self: экземпляр класса.
		'''
		values: list[int] = []
		current = self.head
		while current is not None:
			values.append(current.data)
			current = current.next
		return values

	def get_node_by_index(self, index: int) -> Node:
		'''вернуть узел по индексу от нуля.

		@param index: индекс узла.
		'''
		if index < 0:
			raise ValueError('Индекс не может быть < 0')
		current = self.head
		step = 0
		while current is not None and step < index:
			current = current.next
			step += 1
		if current is None:
			raise IndexError('Узел не найден')
		return current


def build_random_doubly_list(
	min_len: int,
	max_len: int,
) -> DoublyList:
	'''создать random-двусвязный список.

	@param min_len: минимальная длина.
	@param max_len: максимальная длина.
	'''
	result = DoublyList()
	size = random.randint(min_len, max_len)
	for _ in range(size):
		result.append(random.randint(1, 50))
	return result


def merge_before_node(
	first_list: DoublyList,
	second_list: DoublyList,
	a0: Node,
) -> tuple[Node, Node]:
	'''вставить первый список перед a0.

	@param first_list: первый список.
	@param second_list: второй список.
	@param a0: узел второго списка.
	'''
	if first_list.head is None or first_list.tail is None:
		raise ValueError('Первый список пуст')
	if second_list.head is None or second_list.tail is None:
		raise ValueError('Второй список пуст')

	first_head = first_list.head
	first_tail = first_list.tail
	before_a0 = a0.prev

	if before_a0 is not None:
		before_a0.next = first_head
	first_head.prev = before_a0

	first_tail.next = a0
	a0.prev = first_tail

	if second_list.head is a0:
		second_list.head = first_head

	if second_list.tail is None:
		raise RuntimeError('Нет хвоста')
	return second_list.head, second_list.tail


def main() -> None:
	'''точка входа.'''
	try:
		first = build_random_doubly_list(2, 5)
		second = build_random_doubly_list(3, 6)
		if second.head is None:
			raise RuntimeError('Нет второго списка')

		second_size = len(second.to_list())
		a0_index = random.randint(0, second_size - 1)
		a0 = second.get_node_by_index(a0_index)

		print('Первый список:')
		print(first.to_list())
		print('Второй список:')
		print(second.to_list())
		print('Узел A0:', a0)

		first_node, last_node = merge_before_node(
			first,
			second,
			a0,
		)
		print('Объединенный список:')
		print(second.to_list())
		print('Ссылка на первый:', first_node)
		print('Ссылка на последний:', last_node)
	except (
		ValueError,
		IndexError,
		RuntimeError,
	) as error:
		print(f'Ошибка выполнения: {error}')


if __name__ == '__main__':
	main()
