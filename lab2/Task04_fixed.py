# изменения по кодстайлу:
# - добавлена типизация и snake_case
# - добавлены docstring с @param
# - добавлена обработка исключений
# - убраны захардкоженные данные
# - генерация данных через random
# - переименован класс
# - добавлено преобразование списка в обычный для удобства вывода
# - логика вставки вынесена в отдельный метод insert_after_each_third
# - tail теперь хранится как атрибут списка — в оригинале P2 находился
# 	отдельным проходом по всему списку после вставки


import random


class Node:
	'''узел односвязного списка.

	@param data: значение узла.
	@param next_node: следующий узел.
	'''

	def __init__(
		self,
		data: int,
		next_node: 'Node | None' = None,
	) -> None:
		'''создать узел.

		@param data: значение узла.
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
		self.tail.next = new_node
		self.tail = new_node

	def insert_after_each_third(self, value: int) -> None:
		'''вставить value после каждого 3-го.

		@param value: вставляемое значение.
		'''
		position = 1
		current = self.head
		while current is not None:
			if position % 3 == 0:
				inserted = Node(value, current.next)
				current.next = inserted
				if self.tail is current:
					self.tail = inserted
				current = inserted.next
				position += 1
				continue
			current = current.next
			position += 1

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
	size = random.randint(6, 12)
	for _ in range(size):
		result.append(random.randint(1, 20))
	return result


def read_m_value() -> int:
	'''прочитать M от пользователя.'''
	raw = input('Введите M, либо Enter для random: ')
	if raw.strip() == '':
		return random.randint(1, 20)
	try:
		return int(raw)
	except ValueError as error:
		raise ValueError(
			'M должно быть целым'
		) from error


def main() -> None:
	'''точка входа.'''
	try:
		linked_list = build_random_list()
		m_value = read_m_value()
		print('Изначальный список:')
		print(linked_list.to_list())
		linked_list.insert_after_each_third(m_value)
		print('Итоговый список:')
		print(linked_list.to_list())
		p2 = linked_list.tail
		if p2 is None:
			raise RuntimeError('Не найден хвост')
		print('Ссылка P2:', p2)
		print('Значение P2:', p2.data)
	except (ValueError, RuntimeError) as error:
		print(f'Ошибка выполнения: {error}')


if __name__ == '__main__':
	main()
