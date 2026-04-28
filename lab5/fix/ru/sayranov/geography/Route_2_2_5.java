package ru.sayranov.geography;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/**
 * маршрут между двумя городами.
 */
public class Route_2_2_5 {

	private City_2_1_10 start;
	private City_2_1_10 end;

	/**
	 * создает маршрут между двумя городами.
	 *
	 * @param start начальный город
	 * @param end конечный город
	 */
	public Route_2_2_5(
		final City_2_1_10 start,
		final City_2_1_10 end
	) {
		setStart(start);
		setEnd(end);
	}

	/**
	 * возвращает начальный город.
	 *
	 * @return начальный город
	 */
	public City_2_1_10 getStart() {
		return start;
	}

	/**
	 * задает начальный город.
	 *
	 * @param start начальный город
	 */
	public void setStart(final City_2_1_10 start) {
		if (start == null) {
			throw new IllegalArgumentException(
				"город начала не может быть null"
			);
		}

		this.start = start;
	}

	/**
	 * возвращает конечный город.
	 *
	 * @return конечный город
	 */
	public City_2_1_10 getEnd() {
		return end;
	}

	/**
	 * задает конечный город.
	 *
	 * @param end конечный город
	 */
	public void setEnd(final City_2_1_10 end) {
		if (end == null) {
			throw new IllegalArgumentException(
				"город конца не может быть null"
			);
		}

		this.end = end;
	}

	/**
	 * строит путь в ширину.
	 *
	 * @return массив городов маршрута
	 */
	public City_2_1_10[] getRoute() {
		if (start.equals(end)) {
			return new City_2_1_10[] {start};
		}

		final Deque<City_2_1_10> queue = new ArrayDeque<>();
		final Set<City_2_1_10> visited = new HashSet<>();
		final Map<City_2_1_10, City_2_1_10> previous =
			new HashMap<>();

		queue.add(start);
		visited.add(start);

		while (!queue.isEmpty()) {
			final City_2_1_10 current = queue.removeFirst();

			if (current.equals(end)) {
				break;
			}

			for (City_2_1_10 neighbor : current.getPaths().keySet()) {
				if (!visited.contains(neighbor)) {
					visited.add(neighbor);
					previous.put(neighbor, current);
					queue.addLast(neighbor);
				}
			}
		}

		if (!previous.containsKey(end)) {
			return new City_2_1_10[0];
		}

		final List<City_2_1_10> path = new ArrayList<>();
		City_2_1_10 current = end;

		while (current != null) {
			path.add(0, current);
			current = previous.get(current);
		}

		return path.toArray(new City_2_1_10[0]);
	}

	@Override
	public String toString() {
		final City_2_1_10[] route = getRoute();

		if (route.length == 0) {
			return "путь не найден";
		}

		final StringBuilder builder = new StringBuilder();

		for (int index = 0; index < route.length; index++) {
			builder.append(route[index].getName());

			if (index < route.length - 1) {
				builder.append(" -> ");
			}
		}

		return builder.toString();
	}
}
