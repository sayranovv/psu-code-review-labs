# изменения по кодстайлу:
# - переписан IntListB с типизацией
# - добавлены docstring с @param
# - добавлена обработка исключений
# - данные заменены random
# - to_prev и to_last теперь кидают RuntimeError
# 	если prev is None, вместо молчаливой проверки
# 	if barrier.next != barrier
# - метод put изменён: в оригинале Put() возвращал
# 	готовую строку с текстом — было смешение логики и представления
# - промежуточный список elems убран — элементы добавляются напрямую в insert_last
# - создание барьера и заполнение списка вынесены в build_barrier_list()
# - логика вывода чётных вынесена в print_even_from_end()

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


class IntListB:
	'''двусвязный список с барьером.

	@param barrier_node: барьерный узел.
	@param current_node: текущий узел.
	'''

	def __init__(
		self,
		barrier_node: Node,
		current_node: Node,
	) -> None:
		'''создать список.

		@param barrier_node: барьерный узел.
		@param current_node: текущий узел.
		'''
		self._barrier: Node = barrier_node
		self._current: Node = current_node

	def insert_last(self, data: int) -> None:
		'''добавить элемент в конец.

		@param data: добавляемое значение.
		'''
		new_node = Node(data)
		last = self._barrier.prev
		if last is None:
			raise RuntimeError('У барьера нет prev')
		new_node.prev = last
		new_node.next = self._barrier
		last.next = new_node
		self._barrier.prev = new_node
		self._current = new_node

	def put(self) -> Node:
		'''вернуть ссылку на current.

		@param self: экземпляр класса.
		'''
		return self._current

	def to_last(self) -> None:
		'''сделать текущим последний узел.

		@param self: экземпляр класса.
		'''
		last = self._barrier.prev
		if last is None:
			raise RuntimeError('У барьера нет prev')
		self._current = last

	def to_prev(self) -> None:
		'''сдвинуть current к предыдущему.

		@param self: экземпляр класса.
		'''
		prev_node = self._current.prev
		if prev_node is None:
			raise RuntimeError('Нет предыдущего')
		self._current = prev_node

	def get_data(self) -> int:
		'''получить значение current.

		@param self: экземпляр класса.
		'''
		return self._current.data

	def is_barrier(self) -> bool:
		'''проверить current на барьер.

		@param self: экземпляр класса.
		'''
		return self._current is self._barrier

	def to_list(self) -> list[int]:
		'''вернуть значения без барьера.

		@param self: экземпляр класса.
		'''
		values: list[int] = []
		current = self._barrier.next
		while current is not None and (
			current is not self._barrier
		):
			values.append(current.data)
			current = current.next
		return values


def build_barrier_list() -> IntListB:
	'''создать список с барьером и random.

	@param нет: входных параметров нет.
	'''
	barrier = Node(0)
	barrier.prev = barrier
	barrier.next = barrier
	int_list = IntListB(barrier, barrier)
	size = random.randint(10, 20)
	for _ in range(size):
		int_list.insert_last(random.randint(1, 50))
	return int_list


def print_even_from_end(int_list: IntListB) -> None:
	'''вывести четные значения с конца.

	@param int_list: список для обхода.
	'''
	int_list.to_last()
	count = 0
	even_values: list[int] = []
	while not int_list.is_barrier():
		value = int_list.get_data()
		if value % 2 == 0:
			even_values.append(value)
		count += 1
		int_list.to_prev()
	print('Четные с конца:', even_values)
	print('Количество элементов:', count)


def main() -> None:
	'''точка входа.'''
	try:
		int_list = build_barrier_list()
		print('Исходный список:', int_list.to_list())
		print('Ссылка на current:', int_list.put())
		print_even_from_end(int_list)
	except (RuntimeError, ValueError) as error:
		print(f'Ошибка выполнения: {error}')


if __name__ == '__main__':
	main()
