"""graf10: все маршруты между городами."""

import sys


def read_input(
	file_name: str,
) -> tuple[int, list[list[int]], list[int]]:
	"""читает n, матрицу и хвост чисел.

	@param file_name: путь к входному файлу.
	@return: n, матрица смежности, хвост чисел.
	"""
	with open(file_name, 'r', encoding='utf-8') as source:
		numbers = [int(item) for item in source.read().split()]

	if not numbers:
		raise ValueError('пустой входной файл')

	n = numbers[0]
	index = 1
	matrix: list[list[int]] = []
	for _ in range(n):
		row = numbers[index:index + n]
		if len(row) != n:
			raise ValueError('некорректная матрица')
		matrix.append(row)
		index += n

	return n, matrix, numbers[index:]


def find_paths(
	matrix: list[list[int]],
	start: int,
	end: int,
) -> list[list[int]]:
	"""ищет все простые маршруты.

	@param matrix: матрица смежности.
	@param start: начальная вершина.
	@param end: конечная вершина.
	@return: список маршрутов.
	"""
	n = len(matrix)
	visited = [False] * n
	path = [start + 1]
	paths: list[list[int]] = []

	def dfs(vertex: int) -> None:
		if vertex == end:
			paths.append(path.copy())
			return

		visited[vertex] = True
		for neighbour in range(n):
			if matrix[vertex][neighbour] != 1:
				continue
			if visited[neighbour]:
				continue
			path.append(neighbour + 1)
			dfs(neighbour)
			path.pop()
		visited[vertex] = False

	dfs(start)
	return paths


def write_output(
	file_name: str,
	paths: list[list[int]],
) -> None:
	"""записывает ответ в файл.

	@param file_name: путь к выходному файлу.
	@param paths: найденные маршруты.
	"""
	with open(file_name, 'w', encoding='utf-8') as target:
		if not paths:
			target.write('-1\n')
			return

		target.write(f'{len(paths)}\n')
		for route in paths:
			target.write(' '.join(map(str, route)))
			target.write('\n')


def main() -> None:
	"""точка входа."""
	input_file = 'FileName1'
	output_file = 'FileName2'
	k1 = None
	k2 = None

	if len(sys.argv) > 1:
		input_file = sys.argv[1]
	if len(sys.argv) > 2:
		output_file = sys.argv[2]
	if len(sys.argv) > 4:
		k1 = int(sys.argv[3])
		k2 = int(sys.argv[4])

	n, matrix, tail = read_input(input_file)
	if k1 is None or k2 is None:
		if len(tail) >= 2:
			k1, k2 = tail[0], tail[1]
		else:
			k1, k2 = 1, n

	if not 1 <= k1 <= n or not 1 <= k2 <= n:
		raise ValueError('города вне диапазона')

	paths = find_paths(matrix, k1 - 1, k2 - 1)
	paths.sort(key=lambda route: (len(route), route))
	write_output(output_file, paths)


if __name__ == '__main__':
	main()
