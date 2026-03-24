# изменения по кодстайлу:
# - добавлена строгая типизация
# - добавлены docstring с @param
# - добавлена обработка исключений
# - убраны захардкоженные данные
# - генерация данных через random
# - переименован класс
# - добавлено преобразование списка в обычный для удобства вывода
# - оставлен только append и get_nth_node для решения задачи

import random


class Node:
	'''узел односвязного списка.

	@param data: данные узла.
	@param next_node: следующий узел.
	'''

	def __init__(
		self,
		data: int,
		next_node: 'Node | None' = None,
	) -> None:
		'''инициализировать узел.

		@param data: данные узла.
		@param next_node: следующий узел.
		'''
		self.data: int = data
		self.next: Node | None = next_node

	def __str__(self) -> str:
		'''вернуть строку узла.

		@param self: экземпляр класса.
		'''
		return f'Node(data={self.data})'


class SinglyList:
	'''односвязный список.

	@param head: начало списка.
	@param tail: конец списка.
	'''

	def __init__(self) -> None:
		'''инициализировать пустой список.

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
		self.tail.next = new_node
		self.tail = new_node

	def get_nth_node(self, index: int) -> Node:
		'''вернуть узел по индексу от 1.

		@param index: номер узла в списке.
		'''
		if index <= 0:
			raise ValueError('Индекс должен быть > 0')
		current = self.head
		step = 1
		while current is not None and step < index:
			current = current.next
			step += 1
		if current is None:
			raise IndexError('Узел не найден')
		return current

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


def build_random_list() -> SinglyList:
	'''создать случайный список.'''
	result = SinglyList()
	size = random.randint(9, 15)
	for _ in range(size):
		result.append(random.randint(1, 99))
	return result


def main() -> None:
	'''точка входа.'''
	try:
		linked_list = build_random_list()
		p1 = linked_list.head
		if p1 is None:
			raise RuntimeError('Список не был создан')
		p9 = linked_list.get_nth_node(9)
		print('Список:', linked_list.to_list())
		print('Указатель P1:', p1)
		print('Указатель P9:', p9)
		print('Значение P9:', p9.data)
	except (RuntimeError, IndexError, ValueError) as error:
		print(f'Ошибка выполнения: {error}')


if __name__ == '__main__':
	main()
