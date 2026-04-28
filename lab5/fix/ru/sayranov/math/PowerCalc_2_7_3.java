package ru.sayranov.math;

/**
 * калькулятор возведения в степень.
 */
public final class PowerCalc_2_7_3 {

	/**
	 * закрытый конструктор утилитного класса.
	 */
	private PowerCalc_2_7_3() {
	}

	/**
	 * возводит целое основание в целую степень.
	 *
	 * @param xStr основание в строке
	 * @param yStr показатель степени в строке
	 * @return результат вычисления
	 */
	public static double power(
		final String xStr,
		final String yStr
	) {
		final int base = parseInt(xStr, "основание");
		final int exponent = parseInt(yStr, "показатель степени");
		return Math.pow(base, exponent);
	}

	/**
	 * разбирает строку в целое число.
	 *
	 * @param value строковое значение
	 * @param fieldName имя поля для ошибки
	 * @return целое число
	 */
	private static int parseInt(
		final String value,
		final String fieldName
	) {
		if (value == null || value.isBlank()) {
			throw new IllegalArgumentException(
				fieldName + " не может быть пустым"
			);
		}

		try {
			return Integer.parseInt(value);
		} catch (NumberFormatException exception) {
			throw new IllegalArgumentException(
				fieldName + " должно быть целым числом",
				exception
			);
		}
	}
}
