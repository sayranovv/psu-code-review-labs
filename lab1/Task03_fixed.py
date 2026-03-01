'''task03 fixed.

несоответствия в исходнике:
- отступы пробелами вместо табуляции.
- нет docstring у всех функций.
- часть комментариев была в конце строк.
- встречались двойные кавычки без необходимости.
- длинные строки выходили за предел 64 символов.

что исправлено:
- отступы переведены на табы.
- добавлены docstring.
- формат строк и кавычек приведён к правилам.
- логика парсинга оформлена в класс.
'''


class RecursiveExpressionParser:
	'''разбирает выражение по рекурсивной грамматике.'''

	def __init__(self, text):
		'''сохраняет выражение и начальную позицию.'''
		self.text = text
		self.index = 0

	def parse_term(self):
		'''разбирает терм вида цифра или терм * цифра.'''
		if self.index >= len(self.text):
			raise ValueError('ожидалась цифра')
		char = self.text[self.index]
		if not char.isdigit():
			raise ValueError('ожидалась цифра')
		value = int(char)
		self.index += 1
		if self.index < len(self.text):
			if self.text[self.index] == '*':
				self.index += 1
				right = self.parse_term()
				return value * right
		return value

	def parse_expression(self):
		'''разбирает выражение из термов с плюсом и минусом.'''
		value = self.parse_term()
		if self.index < len(self.text):
			operator = self.text[self.index]
			if operator in ('+', '-'):
				self.index += 1
				right = self.parse_expression()
				if operator == '+':
					return value + right
				return value - right
		return value

	def evaluate(self):
		'''возвращает итог вычисления выражения.'''
		result = self.parse_expression()
		if self.index != len(self.text):
			raise ValueError('некорректный синтаксис')
		return result



def main():
	'''читает строку выражения и печатает результат.'''
	expression = input('введите строку с выражением: ')
	try:
		parser = RecursiveExpressionParser(expression)
		print(parser.evaluate())
	except ValueError as error:
		print(error)


if __name__ == '__main__':
	main()
