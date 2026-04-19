import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * точка входа
 */
public class Main {
	/**
	 * запускает программу
	 *
	 * @param args аргументы
	 */
	public static void main(final String[] args) {
		try (Scanner scanner = new Scanner(System.in)) {
			final int exercise = readInt(
				scanner,
				"номер задания"
			);
			final int task = readInt(
				scanner,
				"номер задачи"
			);

			final boolean isValid = runSelectedTask(
				scanner,
				exercise,
				task
			);

			if (!isValid) {
				System.out.println("нет такой задачи");
			}
		} catch (IllegalArgumentException exception) {
			System.out.println("ошибка ввода: "
				+ exception.getMessage());
		} catch (RuntimeException exception) {
			System.out.println("ошибка: "
				+ exception.getMessage());
		}
	}

	/**
	 * запускает выбранную задачу
	 *
	 * @param scanner сканер
	 * @param exercise номер задания
	 * @param task номер задачи
	 * @return true, если задача существует
	 */
	private static boolean runSelectedTask(
		final Scanner scanner,
		final int exercise,
		final int task
	) {
		if (exercise == 1 && task == 2) {
			runPersonsTask(scanner);
			return true;
		}

		if (exercise == 1 && task == 3) {
			runNamesTask(scanner);
			return true;
		}

		if (exercise == 2 && task == 2) {
			runPersonsWithNamesTask(scanner);
			return true;
		}

		if (exercise == 3 && task == 3) {
			runCityGraphByAddPathTask(scanner);
			return true;
		}

		if (exercise == 4 && task == 8) {
			runCityGraphByMapTask(scanner);
			return true;
		}

		if (exercise == 5 && task == 5) {
			runFractionsTask(scanner);
			return true;
		}

		return false;
	}

	/**
	 * решает задачу с объектами Person
	 *
	 * @param scanner сканер ввода
	 */
	private static void runPersonsTask(final Scanner scanner) {
		System.out.println("задача 1 | задание 2");
		final int count = readInt(
			scanner,
			"количество людей"
		);

		for (int index = 0; index < count; index++) {
			final String name = readNonEmptyLine(
				scanner,
				"введите имя"
			);
			final int height = readInt(scanner, "рост");
			final Person person = new Person(name, height);
			System.out.println(person);
		}
	}

	/**
	 * решает задачу с объектами Name
	 *
	 * @param scanner сканер ввода
	 */
	private static void runNamesTask(final Scanner scanner) {
		System.out.println("задача 1 | задание 3");
		final int count = readInt(
			scanner,
			"количество имен"
		);

		for (int index = 0; index < count; index++) {
			final Name name = readName(scanner);
			System.out.println(name);
		}
	}

	/**
	 * решает задачу PersonWithName
	 *
	 * @param scanner сканер ввода
	 */
	private static void runPersonsWithNamesTask(
		final Scanner scanner
	) {
		System.out.println("задача 2 | задание 2");
		final int count = readInt(
			scanner,
			"количество людей"
		);

		for (int index = 0; index < count; index++) {
			final Name fullName = readName(scanner);
			final int height = readInt(scanner, "рост");
			final PersonWithName person = new PersonWithName(
				fullName,
				height
			);
			System.out.println(person);
		}
	}

	/**
	 * решает граф через addPath
	 *
	 * @param scanner сканер ввода
	 */
	private static void runCityGraphByAddPathTask(
		final Scanner scanner
	) {
		System.out.println("задача 3 | задание 3");
		final Map<String, City> cities = readCityMap(scanner);
		final int pathsCount = readInt(
			scanner,
			"введите количество путей"
		);

		for (int index = 0; index < pathsCount; index++) {
			final String fromName = readNonEmptyLine(
				scanner,
				"введите город отправления"
			);
			final String toName = readNonEmptyLine(
				scanner,
				"введите город назначения"
			);
			final int cost = readInt(
				scanner,
				"введите стоимость пути"
			);
			final City from = requireCity(cities, fromName);
			final City to = requireCity(cities, toName);
			from.addPath(to, cost);
		}

		printCities(cities);
	}

	/**
	 * решает граф через map-конструктор
	 *
	 * @param scanner сканер ввода
	 */
	private static void runCityGraphByMapTask(
		final Scanner scanner
	) {
		System.out.println("задача 4 | задание 8");
		final Map<String, City> cities = readCityMap(scanner);
		final Map<String, Map<City, Integer>> pathsByName =
			new HashMap<>();

		for (String name : cities.keySet()) {
			pathsByName.put(name, new HashMap<>());
		}

		final int pathsCount = readInt(
			scanner,
			"введите количество путей"
		);

		for (int index = 0; index < pathsCount; index++) {
			final String fromName = readNonEmptyLine(
				scanner,
				"введите город отправления"
			);
			final String toName = readNonEmptyLine(
				scanner,
				"введите город назначения"
			);
			final int cost = readInt(
				scanner,
				"введите стоимость пути"
			);
			final City to = requireCity(cities, toName);
			final Map<City, Integer> fromPaths =
				pathsByName.get(fromName);

			if (fromPaths == null) {
				throw new IllegalArgumentException(
					"город не найден: " + fromName
				);
			}

			fromPaths.put(to, cost);
		}

		for (Map.Entry<String, City> entry : cities.entrySet()) {
			final String name = entry.getKey();
			final City city = new City(name, pathsByName.get(name));
			entry.setValue(city);
		}

		printCities(cities);
	}

	/**
	 * решает задачу с дробями
	 *
	 * @param scanner сканер ввода
	 */
	private static void runFractionsTask(final Scanner scanner) {
		System.out.println("задача 5 | задание 5");
		System.out.println("первая дробь");
		final Fraction first = readFraction(scanner);
		System.out.println("вторая дробь");
		final Fraction second = readFraction(scanner);
		System.out.println("третья дробь");
		final Fraction third = readFraction(scanner);
		final int subtractValue = readInt(
			scanner,
			"целое число для вычитания"
		);

		System.out.println(first + " + " + second + " = "
			+ first.sum(second));
		System.out.println(first + " - " + second + " = "
			+ first.minus(second));
		System.out.println(first + " * " + second + " = "
			+ first.multiply(second));
		System.out.println(first + " / " + second + " = "
			+ first.div(second));
		System.out.println(first + " - " + subtractValue + " = "
			+ first.minus(subtractValue));

		final Fraction result = first.sum(second)
			.div(third)
			.minus(subtractValue);
		System.out.println("(" + first + " + " + second + ") / "
			+ third
			+ " - "
			+ subtractValue
			+ " = "
			+ result);
	}

	/**
	 * читает карту городов по имени
	 *
	 * @param scanner сканер ввода
	 * @return карта городов
	 */
	private static Map<String, City> readCityMap(
		final Scanner scanner
	) {
		final int cityCount = readInt(
			scanner,
			"введите количество городов"
		);
		final Map<String, City> cities = new HashMap<>();

		for (int index = 0; index < cityCount; index++) {
			final String cityName = readNonEmptyLine(
				scanner,
				"введите имя города"
			);

			if (cities.containsKey(cityName)) {
				throw new IllegalArgumentException(
					"город уже существует: " + cityName
				);
			}

			cities.put(cityName, new City(cityName));
		}

		return cities;
	}

	/**
	 * ищет город по имени
	 *
	 * @param cities карта городов
	 * @param name имя города
	 * @return найденный город
	 */
	private static City requireCity(
		final Map<String, City> cities,
		final String name
	) {
		final City city = cities.get(name);

		if (city == null) {
			throw new IllegalArgumentException(
				"город не найден: " + name
			);
		}

		return city;
	}

	/**
	 * печатает города и их пути
	 *
	 * @param cities карта городов
	 */
	private static void printCities(
		final Map<String, City> cities
	) {
		for (City city : cities.values()) {
			System.out.println(city);
		}
	}

	/**
	 * читает объект имени
	 *
	 * @param scanner сканер ввода
	 * @return объект имени
	 */
	private static Name readName(final Scanner scanner) {
		final String lastName = readOptionalLine(
			scanner,
			"фамилия (пусто = null)"
		);
		final String firstName = readOptionalLine(
			scanner,
			"имя (пусто = null)"
		);
		final String middleName = readOptionalLine(
			scanner,
			"отчество (пусто = null)"
		);

		return new Name(lastName, firstName, middleName);
	}

	/**
	 * читает дробь
	 *
	 * @param scanner сканер ввода
	 * @return созданная дробь
	 */
	private static Fraction readFraction(
		final Scanner scanner
	) {
		final int numerator = readInt(
			scanner,
			"числитель"
		);
		final int denominator = readInt(
			scanner,
			"знаменатель"
		);
		return new Fraction(numerator, denominator);
	}

	/**
	 * читает целое число
	 *
	 * @param scanner сканер ввода
	 * @param prompt текст приглашения
	 * @return введенное число
	 */
	private static int readInt(
		final Scanner scanner,
		final String prompt
	) {
		while (true) {
			System.out.println(prompt + ":");
			final String line = scanner.nextLine().trim();

			try {
				return Integer.parseInt(line);
			} catch (NumberFormatException exception) {
				System.out.println("ошибка: нужно целое");
			}
		}
	}

	/**
	 * читает непустую строку
	 *
	 * @param scanner сканер ввода
	 * @param prompt текст приглашения
	 * @return введенная строка
	 */
	private static String readNonEmptyLine(
		final Scanner scanner,
		final String prompt
	) {
		while (true) {
			System.out.println(prompt + ":");
			final String line = scanner.nextLine().trim();

			if (!line.isEmpty()) {
				return line;
			}

			System.out.println("ошибка: пусто");
		}
	}

	/**
	 * читает строку или null
	 *
	 * @param scanner сканер ввода
	 * @param prompt приглашение
	 * @return строка или null
	 */
	private static String readOptionalLine(
		final Scanner scanner,
		final String prompt
	) {
		System.out.println(prompt + ":");
		final String line = scanner.nextLine().trim();

		if (line.isEmpty()) {
			return null;
		}

		return line;
	}
}