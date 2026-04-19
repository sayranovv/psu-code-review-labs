import java.util.HashMap;
import java.util.Map;

/**
 * город с набором путей
 */
public class City {

	private final String name;
	private final Map<City, Integer> paths;

	/**
	 * создает город без путей
	 *
	 * @param name имя города
	 */
	public City(final String name) {
		this.name = name;
		this.paths = new HashMap<>();
	}

	/**
	 * создает город с путями
	 *
	 * @param name имя города
	 * @param initialPaths карта путей
	 */
	public City(
		final String name,
		final Map<City, Integer> initialPaths
	) {
		this.name = name;
		this.paths = new HashMap<>(initialPaths);
	}

	/**
	 * добавляет путь до города
	 *
	 * @param city город назначения
	 * @param cost стоимость пути
	 */
	public void addPath(final City city, final int cost) {
		if (city == null) {
			throw new IllegalArgumentException(
				"город назначения не задан"
			);
		}

		if (cost < 0) {
			throw new IllegalArgumentException(
				"стоимость пути < 0"
			);
		}

		paths.put(city, cost);
	}

	/**
	 * возвращает строку города
	 *
	 * @return строка с путями
	 */
	@Override
	public String toString() {
		final StringBuilder sb = new StringBuilder();
		sb.append(name).append(" -> ");

		for (Map.Entry<City, Integer> entry : paths.entrySet()) {
			sb.append(entry.getKey().name)
				.append(":")
				.append(entry.getValue())
				.append(" ");
		}

		return sb.toString();
	}
}
