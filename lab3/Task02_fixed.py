"""calctree8: дерево выражения в префиксной форме."""

import sys


OP_CODE = {
	'+': -1,
	'-': -2,
	'*': -3,
	'/': -4,
	'%': -5,
	'^': -6,
}


class Node:
	"""узел дерева выражения."""

	def __init__(
		self,
		value: int,
		left: 'Node | None' = None,
		right: 'Node | None' = None,
	) -> None:
		"""создает узел.

		@param value: значение узла.
		@param left: левый потомок.
		@param right: правый потомок.
		"""
		self.value = value
		self.left = left
		self.right = right


def tokenize(expression: str) -> list[str]:
	"""делит выражение на токены.

	@param expression: префиксная запись.
	@return: список токенов.
	"""
	return [char for char in expression if not char.isspace()]


def parse_prefix(
	tokens: list[str],
	index: int = 0,
) -> tuple[Node, int]:
	"""строит дерево по префиксу.

	@param tokens: токены выражения.
	@param index: текущая позиция.
	@return: узел и новая позиция.
	"""
	if index >= len(tokens):
		raise ValueError('неполное выражение')

	token = tokens[index]
	index += 1

	if token in OP_CODE:
		node = Node(OP_CODE[token])
		node.left, index = parse_prefix(tokens, index)
		node.right, index = parse_prefix(tokens, index)
		return node, index

	if not token.isdigit():
		raise ValueError('неверный токен')

	return Node(int(token)), index


def evaluate(node: Node) -> int:
	"""вычисляет значение поддерева.

	@param node: корень поддерева.
	@return: значение поддерева.
	"""
	if node.left is None and node.right is None:
		return node.value

	if node.left is None or node.right is None:
		raise ValueError('некорректное дерево')

	left = evaluate(node.left)
	right = evaluate(node.right)

	if node.value == -1:
		return left + right
	if node.value == -2:
		return left - right
	if node.value == -3:
		return left * right
	if node.value == -4:
		if right == 0:
			raise ZeroDivisionError('деление на ноль')
		return left // right
	if node.value == -5:
		if right == 0:
			raise ZeroDivisionError('остаток от деления на ноль')
		return left % right
	if node.value == -6:
		return left ** right

	raise ValueError('неизвестная операция')


def reduce_tree(node: Node) -> Node:
	"""сворачивает поддеревья по условию.

	@param node: корень поддерева.
	@return: новый корень поддерева.
	"""
	if node.left is None and node.right is None:
		return node

	if node.left is None or node.right is None:
		raise ValueError('некорректное дерево')

	node.left = reduce_tree(node.left)
	node.right = reduce_tree(node.right)

	left_value = evaluate(node.left)
	right_value = evaluate(node.right)
	if left_value == 0 or right_value == 0:
		return Node(evaluate(node))

	return node


def main() -> None:
	"""точка входа."""
	input_file = 'filename'
	if len(sys.argv) > 1:
		input_file = sys.argv[1]

	try:
		with open(input_file, 'r', encoding='utf-8') as source:
			expression = source.read()
		tokens = tokenize(expression)
		root, position = parse_prefix(tokens)
		if position != len(tokens):
			raise ValueError('лишние токены')
		root = reduce_tree(root)
	except (FileNotFoundError, ValueError, ZeroDivisionError) as error:
		print(f'ошибка: {error}')
		return

	print(root)


if __name__ == '__main__':
	main()
