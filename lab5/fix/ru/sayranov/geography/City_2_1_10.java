package ru.sayranov.geography;

import java.util.HashMap;
import java.util.Map;

/**
 * город с двусторонними дорогами и стоимостью пути.
 */
public class City_2_1_10 {

	private final String name;
	private final Map<City_2_1_10, Integer> paths;

	/**
	 * создает город без дорог.
	 *
	 * @param name название города
	 */
	public City_2_1_10(final String name) {
		validateName(name);
		this.name = name;
		this.paths = new HashMap<>();
	}

	/**
	 * создает город с начальными дорогами.
	 *
	 * @param name название города
	 * @param initialPaths начальные дороги
	 */
	public City_2_1_10(
		final String name,
		final Map<City_2_1_10, Integer> initialPaths
	) {
		validateName(name);
		if (initialPaths == null) {
			throw new IllegalArgumentException(
				"карта дорог не может быть null"
			);
		}

		this.name = name;
		this.paths = new HashMap<>();

		for (
			Map.Entry<City_2_1_10, Integer> entry
				: initialPaths.entrySet()
		) {
			addPath(entry.getKey(), entry.getValue());
		}
	}

	/**
	 * добавляет двустороннюю дорогу.
	 *
	 * @param city соседний город
	 * @param cost стоимость дороги
	 */
	public void addPath(final City_2_1_10 city, final int cost) {
		validateCity(city);
		validateCost(cost);

		if (paths.containsKey(city)) {
			return;
		}

		paths.put(city, cost);

		if (!city.paths.containsKey(this)) {
			city.paths.put(this, cost);
		}
	}

	/**
	 * удаляет дорогу между городами.
	 *
	 * @param city соседний город
	 */
	public void removePath(final City_2_1_10 city) {
		if (city == null) {
			throw new IllegalArgumentException(
				"город не может быть null"
			);
		}

		paths.remove(city);
		city.paths.remove(this);
	}

	/**
	 * возвращает неизменяемую копию дорог.
	 *
	 * @return карта дорог
	 */
	public Map<City_2_1_10, Integer> getPaths() {
		return Map.copyOf(paths);
	}

	/**
	 * возвращает название города.
	 *
	 * @return название города
	 */
	public String getName() {
		return name;
	}

	@Override
	public String toString() {
		final StringBuilder builder = new StringBuilder();
		builder.append(name).append(" -> ");

		for (
			Map.Entry<City_2_1_10, Integer> entry
				: paths.entrySet()
		) {
			builder
				.append(entry.getKey().name)
				.append(":")
				.append(entry.getValue())
				.append(" ");
		}

		return builder.toString().trim();
	}

	@Override
	public boolean equals(final Object object) {
		if (this == object) {
			return true;
		}

		if (!(object instanceof City_2_1_10 other)) {
			return false;
		}

		return name.equals(other.name);
	}

	@Override
	public int hashCode() {
		return name.hashCode();
	}

	/**
	 * проверяет корректность имени.
	 *
	 * @param cityName имя города
	 */
	private static void validateName(final String cityName) {
		if (cityName == null || cityName.isBlank()) {
			throw new IllegalArgumentException(
				"имя города не может быть пустым"
			);
		}
	}

	/**
	 * проверяет корректность города.
	 *
	 * @param city город для проверки
	 */
	private void validateCity(final City_2_1_10 city) {
		if (city == null) {
			throw new IllegalArgumentException(
				"город не может быть null"
			);
		}

		if (city == this) {
			throw new IllegalArgumentException(
				"нельзя соединить город сам с собой"
			);
		}
	}

	/**
	 * проверяет корректность стоимости.
	 *
	 * @param cost стоимость дороги
	 */
	private static void validateCost(final int cost) {
		if (cost <= 0) {
			throw new IllegalArgumentException(
				"стоимость дороги должна быть положительной"
			);
		}
	}
}
