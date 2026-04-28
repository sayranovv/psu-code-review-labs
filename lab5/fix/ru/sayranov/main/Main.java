package ru.sayranov.main;

import java.util.Scanner;

import ru.sayranov.geography.City_2_1_10;
import ru.sayranov.geography.City_2_6_5;
import ru.sayranov.geography.Route_2_2_5;
import ru.sayranov.math.Fraction_2_1_4;
import ru.sayranov.math.Fraction_2_3_1;
import ru.sayranov.math.Fraction_2_4_2;
import ru.sayranov.math.PowerCalc_2_7_3;

/**
 * точка входа для запуска заданий лабораторной 5.
 */
public final class Main {

	/**
	 * закрытый конструктор утилитного класса.
	 */
	private Main() {
	}

	/**
	 * запускает программу.
	 *
	 * @param args аргументы командной строки
	 */
	public static void main(final String[] args) {
		final Scanner scanner = new Scanner(System.in);

		try {
			final int exercise = readInt(
				scanner,
				"введите номер задания"
			);
			final int task = readInt(
				scanner,
				"введите номер задачи"
			);

			runSelectedTask(exercise, task, scanner);
		} catch (IllegalArgumentException exception) {
			System.out.println("ошибка: " + exception.getMessage());
		} catch (Exception exception) {
			System.out.println("непредвиденная ошибка");
		}
	}

	/**
	 * запускает выбранную задачу.
	 *
	 * @param exercise номер задания
	 * @param task номер задачи
	 * @param scanner сканер ввода
	 */
	private static void runSelectedTask(
		final int exercise,
		final int task,
		final Scanner scanner
	) {
		if (exercise == 1 && task == 4) {
			runTask_1_4(scanner);
			return;
		}

		if (exercise == 1 && task == 10) {
			runTask_1_10(scanner);
			return;
		}

		if (exercise == 2 && task == 5) {
			runTask_2_5(scanner);
			return;
		}

		if (exercise == 3 && task == 1) {
			runTask_3_1(scanner);
			return;
		}

		if (exercise == 4 && task == 2) {
			runTask_4_2(scanner);
			return;
		}

		if (exercise == 5 && task == 1) {
			runTask_5_1(scanner);
			return;
		}

		if (exercise == 6 && task == 5) {
			runTask_6_5(scanner);
			return;
		}

		if (exercise == 7 && task == 3) {
			runTask_7_3(scanner);
			return;
		}

		System.out.println("нет такой задачи");
	}

	/**
	 * выполняет задачу 1.4.
	 *
	 * @param scanner сканер ввода
	 */
	private static void runTask_1_4(final Scanner scanner) {
		System.out.println("задача 1 | задание 4");

		final Fraction_2_1_4 first = readFraction214(scanner, "первая");
		final Fraction_2_1_4 second = readFraction214(scanner, "вторая");

		System.out.println("first = " + first);
		System.out.println("second = " + second);
		System.out.println("first + second = " + first.sum(second));
		System.out.println("first - second = " + first.minus(second));
		System.out.println("first * second = " + first.multiply(second));
		System.out.println("first / second = " + first.div(second));
	}

	/**
	 * выполняет задачу 1.10.
	 *
	 * @param scanner сканер ввода
	 */
	private static void runTask_1_10(final Scanner scanner) {
		System.out.println("задача 1 | задание 10");

		final City_2_1_10 firstCity =
			new City_2_1_10(readText(scanner, "имя первого города"));
		final City_2_1_10 secondCity =
			new City_2_1_10(readText(scanner, "имя второго города"));
		final City_2_1_10 thirdCity =
			new City_2_1_10(readText(scanner, "имя третьего города"));

		final int firstCost = readInt(
			scanner,
			"стоимость дороги 1-2"
		);
		final int secondCost = readInt(
			scanner,
			"стоимость дороги 1-3"
		);
		final int thirdCost = readInt(
			scanner,
			"стоимость дороги 2-3"
		);

		firstCity.addPath(secondCity, firstCost);
		firstCity.addPath(thirdCity, secondCost);
		secondCity.addPath(thirdCity, thirdCost);

		System.out.println(firstCity);
		System.out.println(secondCity);
		System.out.println(thirdCity);
	}

	/**
	 * выполняет задачу 2.5.
	 *
	 * @param scanner сканер ввода
	 */
	private static void runTask_2_5(final Scanner scanner) {
		System.out.println("задача 2 | задание 5");

		final int cityCount = readInt(scanner, "количество городов");
		if (cityCount < 2) {
			throw new IllegalArgumentException(
				"нужно минимум 2 города"
			);
		}

		final City_2_1_10[] cities = new City_2_1_10[cityCount];
		for (int index = 0; index < cityCount; index++) {
			final String prompt = "имя города #" + (index + 1);
			cities[index] = new City_2_1_10(readText(scanner, prompt));
		}

		final int edgeCount = readInt(scanner, "количество дорог");
		for (int index = 0; index < edgeCount; index++) {
			System.out.println("дорога #" + (index + 1));
			final int from = readInt(scanner, "индекс города от") - 1;
			final int to = readInt(scanner, "индекс города до") - 1;
			final int cost = readInt(scanner, "стоимость");

			validateIndex(from, cityCount);
			validateIndex(to, cityCount);
			cities[from].addPath(cities[to], cost);
		}

		final int startIndex = readInt(scanner, "индекс города старта") - 1;
		final int endIndex = readInt(scanner, "индекс города финиша") - 1;
		validateIndex(startIndex, cityCount);
		validateIndex(endIndex, cityCount);

		final Route_2_2_5 route =
			new Route_2_2_5(cities[startIndex], cities[endIndex]);
		System.out.println(route);
	}

	/**
	 * выполняет задачу 3.1.
	 *
	 * @param scanner сканер ввода
	 */
	private static void runTask_3_1(final Scanner scanner) {
		System.out.println("задача 3 | задание 1");

		final Fraction_2_3_1 first = readFraction231(scanner, "первая");
		final Fraction_2_3_1 second = readFraction231(scanner, "вторая");

		System.out.println("first = " + first);
		System.out.println("second = " + second);
		System.out.println("first + second = " + first.sum(second));
		System.out.println("first - second = " + first.minus(second));
		System.out.println("first * second = " + first.multiply(second));
		System.out.println("first / second = " + first.div(second));
	}

	/**
	 * выполняет задачу 4.2.
	 *
	 * @param scanner сканер ввода
	 */
	private static void runTask_4_2(final Scanner scanner) {
		System.out.println("задача 4 | задание 2");

		final Fraction_2_4_2 fraction = readFraction242(scanner, "число");
		final Number number = fraction;

		System.out.println("double = " + number.doubleValue());
		System.out.println("float = " + number.floatValue());
		System.out.println("int = " + number.intValue());
		System.out.println("long = " + number.longValue());
	}

	/**
	 * выполняет задачу 5.1.
	 *
	 * @param scanner сканер ввода
	 */
	private static void runTask_5_1(final Scanner scanner) {
		System.out.println("задача 5 | задание 1");

		final int count = readInt(scanner, "количество слагаемых");
		if (count <= 0) {
			throw new IllegalArgumentException(
				"количество должно быть положительным"
			);
		}

		final Number[] values = new Number[count];

		for (int index = 0; index < count; index++) {
			values[index] = readNumber(scanner, "слагаемое #" + (index + 1));
		}

		System.out.println("сумма = " + Sum_2_5_1.sum(values));
	}

	/**
	 * выполняет задачу 6.5.
	 *
	 * @param scanner сканер ввода
	 */
	private static void runTask_6_5(final Scanner scanner) {
		System.out.println("задача 6 | задание 5");

		final City_2_6_5 first =
			new City_2_6_5(readText(scanner, "имя первого города"));
		final City_2_6_5 second =
			new City_2_6_5(readText(scanner, "имя второго города"));
		final City_2_6_5 third =
			new City_2_6_5(readText(scanner, "имя третьего города"));
		final City_2_6_5 fourth =
			new City_2_6_5(readText(scanner, "имя четвертого города"));

		final int firstCost = readInt(scanner, "стоимость дороги 1-2");
		final int secondCost = readInt(scanner, "стоимость дороги 1-3");

		first.addPath(second, firstCost);
		first.addPath(third, secondCost);
		fourth.addPath(second, firstCost);
		fourth.addPath(third, secondCost);

		System.out.println("сравнение городов: " + first.equals(fourth));
	}

	/**
	 * выполняет задачу 7.3.
	 *
	 * @param scanner сканер ввода
	 */
	private static void runTask_7_3(final Scanner scanner) {
		System.out.println("задача 7 | задание 3");

		final String base = readText(scanner, "основание степени");
		final String exponent = readText(scanner, "показатель степени");

		final double result = PowerCalc_2_7_3.power(base, exponent);
		System.out.println(base + " ^ " + exponent + " = " + result);
	}

	/**
	 * читает целое число.
	 *
	 * @param scanner сканер ввода
	 * @param prompt текст запроса
	 * @return введенное целое число
	 */
	private static int readInt(
		final Scanner scanner,
		final String prompt
	) {
		System.out.print(prompt + ": ");
		final String value = scanner.nextLine();

		try {
			return Integer.parseInt(value.trim());
		} catch (NumberFormatException exception) {
			throw new IllegalArgumentException(
				"требуется целое число",
				exception
			);
		}
	}

	/**
	 * читает текстовое значение.
	 *
	 * @param scanner сканер ввода
	 * @param prompt текст запроса
	 * @return введенная строка
	 */
	private static String readText(
		final Scanner scanner,
		final String prompt
	) {
		System.out.print(prompt + ": ");
		final String value = scanner.nextLine();

		if (value == null || value.isBlank()) {
			throw new IllegalArgumentException(
				"ввод не может быть пустым"
			);
		}

		return value;
	}

	/**
	 * читает значение Number.
	 *
	 * @param scanner сканер ввода
	 * @param prompt текст запроса
	 * @return число int, double или Fraction_2_4_2
	 */
	private static Number readNumber(
		final Scanner scanner,
		final String prompt
	) {
		final String value = readText(scanner, prompt);

		if (value.contains("/")) {
			final String[] parts = value.split("/");
			if (parts.length != 2) {
				throw new IllegalArgumentException(
					"дробь должна быть в формате a/b"
				);
			}

			final int numerator = Integer.parseInt(parts[0].trim());
			final int denominator = Integer.parseInt(parts[1].trim());
			return new Fraction_2_4_2(numerator, denominator);
		}

		if (value.contains(".")) {
			return Double.parseDouble(value);
		}

		return Integer.parseInt(value);
	}

	/**
	 * читает дробь для класса 2.1.4.
	 *
	 * @param scanner сканер ввода
	 * @param label метка значения
	 * @return созданная дробь
	 */
	private static Fraction_2_1_4 readFraction214(
		final Scanner scanner,
		final String label
	) {
		final int numerator = readInt(scanner, label + " числитель");
		final int denominator = readInt(scanner, label + " знаменатель");
		return new Fraction_2_1_4(numerator, denominator);
	}

	/**
	 * читает дробь для класса 2.3.1.
	 *
	 * @param scanner сканер ввода
	 * @param label метка значения
	 * @return созданная дробь
	 */
	private static Fraction_2_3_1 readFraction231(
		final Scanner scanner,
		final String label
	) {
		final int numerator = readInt(scanner, label + " числитель");
		final int denominator = readInt(scanner, label + " знаменатель");
		return new Fraction_2_3_1(numerator, denominator);
	}

	/**
	 * читает дробь для класса 2.4.2.
	 *
	 * @param scanner сканер ввода
	 * @param label метка значения
	 * @return созданная дробь
	 */
	private static Fraction_2_4_2 readFraction242(
		final Scanner scanner,
		final String label
	) {
		final int numerator = readInt(scanner, label + " числитель");
		final int denominator = readInt(scanner, label + " знаменатель");
		return new Fraction_2_4_2(numerator, denominator);
	}

	/**
	 * проверяет корректность индекса массива.
	 *
	 * @param index индекс
	 * @param length длина массива
	 */
	private static void validateIndex(
		final int index,
		final int length
	) {
		if (index < 0 || index >= length) {
			throw new IllegalArgumentException(
				"индекс города вне диапазона"
			);
		}
	}
}
