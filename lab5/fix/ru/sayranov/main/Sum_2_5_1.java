package ru.sayranov.main;

/**
 * утилита для суммирования чисел.
 */
public final class Sum_2_5_1 {

	/**
	 * закрытый конструктор утилитного класса.
	 */
	private Sum_2_5_1() {
	}

	/**
	 * суммирует список чисел.
	 *
	 * @param numbers массив чисел
	 * @return сумма чисел
	 */
	public static double sum(final Number... numbers) {
		if (numbers == null || numbers.length == 0) {
			throw new IllegalArgumentException(
				"массив чисел не может быть пустым"
			);
		}

		double result = 0.0;

		for (Number number : numbers) {
			if (number == null) {
				throw new IllegalArgumentException(
					"элемент массива не может быть null"
				);
			}

			result += number.doubleValue();
		}

		return result;
	}
}
