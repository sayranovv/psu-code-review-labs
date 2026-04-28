package ru.sayranov.math;

/**
 * неизменяемая дробь-наследник Number.
 */
public final class Fraction_2_4_2 extends Number {

	private final int numerator;
	private final int denominator;

	/**
	 * создает нормализованную дробь.
	 *
	 * @param numerator числитель
	 * @param denominator знаменатель
	 */
	public Fraction_2_4_2(
		final int numerator,
		final int denominator
	) {
		if (denominator == 0) {
			throw new IllegalArgumentException(
				"знаменатель не может быть равен 0"
			);
		}

		int checkedNumerator = numerator;
		int checkedDenominator = denominator;

		if (checkedDenominator < 0) {
			checkedNumerator = -checkedNumerator;
			checkedDenominator = -checkedDenominator;
		}

		final int divisor = gcd(
			Math.abs(checkedNumerator),
			Math.abs(checkedDenominator)
		);

		this.numerator = checkedNumerator / divisor;
		this.denominator = checkedDenominator / divisor;
	}

	/**
	 * складывает две дроби.
	 *
	 * @param other вторая дробь
	 * @return результат сложения
	 */
	public Fraction_2_4_2 sum(final Fraction_2_4_2 other) {
		validateFraction(other);
		final int newNumerator =
			numerator * other.denominator
				+ other.numerator * denominator;
		final int newDenominator = denominator * other.denominator;
		return new Fraction_2_4_2(newNumerator, newDenominator);
	}

	/**
	 * вычитает дробь.
	 *
	 * @param other вычитаемая дробь
	 * @return результат вычитания
	 */
	public Fraction_2_4_2 minus(final Fraction_2_4_2 other) {
		validateFraction(other);
		final int newNumerator =
			numerator * other.denominator
				- other.numerator * denominator;
		final int newDenominator = denominator * other.denominator;
		return new Fraction_2_4_2(newNumerator, newDenominator);
	}

	/**
	 * вычитает целое число.
	 *
	 * @param value целое число
	 * @return результат вычитания
	 */
	public Fraction_2_4_2 minus(final int value) {
		return minus(new Fraction_2_4_2(value, 1));
	}

	/**
	 * умножает на дробь.
	 *
	 * @param other вторая дробь
	 * @return результат умножения
	 */
	public Fraction_2_4_2 multiply(final Fraction_2_4_2 other) {
		validateFraction(other);
		return new Fraction_2_4_2(
			numerator * other.numerator,
			denominator * other.denominator
		);
	}

	/**
	 * умножает на целое число.
	 *
	 * @param value множитель
	 * @return результат умножения
	 */
	public Fraction_2_4_2 multiply(final int value) {
		return new Fraction_2_4_2(numerator * value, denominator);
	}

	/**
	 * делит на дробь.
	 *
	 * @param other делитель
	 * @return результат деления
	 */
	public Fraction_2_4_2 div(final Fraction_2_4_2 other) {
		validateFraction(other);
		if (other.numerator == 0) {
			throw new IllegalArgumentException(
				"деление на ноль невозможно"
			);
		}

		return new Fraction_2_4_2(
			numerator * other.denominator,
			denominator * other.numerator
		);
	}

	/**
	 * делит на целое число.
	 *
	 * @param value делитель
	 * @return результат деления
	 */
	public Fraction_2_4_2 div(final int value) {
		if (value == 0) {
			throw new IllegalArgumentException(
				"деление на ноль невозможно"
			);
		}

		return new Fraction_2_4_2(numerator, denominator * value);
	}

	/**
	 * возвращает целочисленное значение.
	 *
	 * @return значение int
	 */
	@Override
	public int intValue() {
		return numerator / denominator;
	}

	/**
	 * возвращает long-значение.
	 *
	 * @return значение long
	 */
	@Override
	public long longValue() {
		return (long) numerator / denominator;
	}

	/**
	 * возвращает float-значение.
	 *
	 * @return значение float
	 */
	@Override
	public float floatValue() {
		return (float) numerator / denominator;
	}

	/**
	 * возвращает double-значение.
	 *
	 * @return значение double
	 */
	@Override
	public double doubleValue() {
		return (double) numerator / denominator;
	}

	/**
	 * возвращает строковое представление.
	 *
	 * @return строка с дробью
	 */
	@Override
	public String toString() {
		return numerator + "/" + denominator;
	}

	/**
	 * вычисляет наибольший общий делитель.
	 *
	 * @param left первое число
	 * @param right второе число
	 * @return наибольший общий делитель
	 */
	private int gcd(final int left, final int right) {
		int first = left;
		int second = right;

		while (second != 0) {
			final int temp = second;
			second = first % second;
			first = temp;
		}

		return first;
	}

	/**
	 * проверяет входную дробь.
	 *
	 * @param fraction дробь
	 */
	private static void validateFraction(
		final Fraction_2_4_2 fraction
	) {
		if (fraction == null) {
			throw new IllegalArgumentException(
				"дробь не может быть null"
			);
		}
	}
}
