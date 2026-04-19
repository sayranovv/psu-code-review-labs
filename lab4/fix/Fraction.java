/**
 * несократимая дробь
 */
public class Fraction {
	private final int numerator;
	private final int denominator;

	/**
	 * создает дробь и сокращает ее
	 *
	 * @param numerator числитель
	 * @param denominator знаменатель
	 */
	public Fraction(final int numerator, final int denominator) {
		if (denominator == 0) {
			throw new IllegalArgumentException(
				"знаменатель равен 0"
			);
		}

		int safeNumerator = numerator;
		int safeDenominator = denominator;
		final int gcd = greatestCommonDivisor(
			Math.abs(safeNumerator),
			Math.abs(safeDenominator)
		);

		if (safeDenominator < 0) {
			safeNumerator = -safeNumerator;
			safeDenominator = -safeDenominator;
		}

		this.numerator = safeNumerator / gcd;
		this.denominator = safeDenominator / gcd;
	}

	/**
	 * вычисляет нод
	 *
	 * @param first первое число
	 * @param second второе число
	 * @return наибольший общий делитель
	 */
	private int greatestCommonDivisor(
		int first,
		int second
	) {
		while (second != 0) {
			final int temp = second;
			second = first % second;
			first = temp;
		}

		return first;
	}

	/**
	 * складывает две дроби
	 *
	 * @param other вторая дробь
	 * @return сумма дробей
	 */
	public Fraction sum(final Fraction other) {
		final int numeratorResult = this.numerator
			* other.denominator
			+ other.numerator * this.denominator;
		final int denominatorResult = this.denominator
			* other.denominator;

		return new Fraction(numeratorResult, denominatorResult);
	}

	/**
	 * вычитает дробь из текущей
	 *
	 * @param other вычитаемая дробь
	 * @return результат вычитания
	 */
	public Fraction minus(final Fraction other) {
		final int numeratorResult = this.numerator
			* other.denominator
			- other.numerator * this.denominator;
		final int denominatorResult = this.denominator
			* other.denominator;

		return new Fraction(numeratorResult, denominatorResult);
	}

	/**
	 * вычитает целое число из дроби
	 *
	 * @param value целое число
	 * @return результат вычитания
	 */
	public Fraction minus(final int value) {
		return this.minus(new Fraction(value, 1));
	}

	/**
	 * умножает дробь на дробь
	 *
	 * @param other второй множитель
	 * @return результат умножения
	 */
	public Fraction multiply(final Fraction other) {
		return new Fraction(
			this.numerator * other.numerator,
			this.denominator * other.denominator
		);
	}

	/**
	 * умножает дробь на целое число
	 *
	 * @param value множитель
	 * @return результат умножения
	 */
	public Fraction multiply(final int value) {
		return new Fraction(this.numerator * value, this.denominator);
	}

	/**
	 * делит текущую дробь на дробь
	 *
	 * @param other делитель
	 * @return результат деления
	 */
	public Fraction div(final Fraction other) {
		if (other.numerator == 0) {
			throw new IllegalArgumentException(
				"деление на ноль невозможно"
			);
		}

		return new Fraction(
			this.numerator * other.denominator,
			this.denominator * other.numerator
		);
	}

	/**
	 * делит дробь на целое число
	 *
	 * @param value делитель
	 * @return результат деления
	 */
	public Fraction div(final int value) {
		if (value == 0) {
			throw new IllegalArgumentException(
				"деление на ноль невозможно"
			);
		}

		return new Fraction(this.numerator, this.denominator * value);
	}

	/**
	 * возвращает строку дроби
	 *
	 * @return строка в формате a/b
	 */
	@Override
	public String toString() {
		return numerator + "/" + denominator;
	}
}
