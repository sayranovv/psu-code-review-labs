"""homedyn17: k-ичные числа без трёх нулей подряд."""

import sys


def count_numbers(n: int, k: int) -> int:
	"""считает число подходящих n-разрядных чисел.

	@param n: количество разрядов.
	@param k: основание системы счисления.
	@return: количество подходящих чисел.
	"""
	prev0 = k - 1
	prev1 = 0
	prev2 = 0

	for _ in range(2, n + 1):
		cur0 = (prev0 + prev1 + prev2) * (k - 1)
		cur1 = prev0
		cur2 = prev1
		prev0 = cur0
		prev1 = cur1
		prev2 = cur2

	return prev0 + prev1 + prev2


def main() -> None:
	"""точка входа."""
	if len(sys.argv) >= 3:
		n = int(sys.argv[1])
		k = int(sys.argv[2])
	else:
		n, k = map(int, input().split())

	if not 1 < n < 20:
		raise ValueError('n вне диапазона')
	if not 2 <= k <= 10:
		raise ValueError('k вне диапазона')
	if n + k >= 26:
		raise ValueError('n + k должно быть меньше 26')

	print(count_numbers(n, k))


if __name__ == '__main__':
	main()
