package ru.sayranov.geography;

import java.util.*;

public class Route_2_2_5 {
    private City_2_1_10 start;
    private City_2_1_10 end;

    public Route_2_2_5(City_2_1_10 start, City_2_1_10 end) {

        if (start == null || end == null) {
            throw new IllegalArgumentException("Начальный и конечный города не могут быть null");
        }

        this.start = start;
        this.end = end;
    }

    public City_2_1_10 getStart() {
        return start;
    }

    public void setStart(City_2_1_10 start) {

        if (start == null) {
            throw new IllegalArgumentException("Город начала не может быть null");
        }

        this.start = start;
    }

    public City_2_1_10 getEnd() {
        return end;
    }

    public void setEnd(City_2_1_10 end) {

        if (end == null) {
            throw new IllegalArgumentException("Город конца не может быть null");
        }

        this.end = end;
    }

    // bfs
    public City_2_1_10[] getRoute() {

        if (start.equals(end)) {
            return new City_2_1_10[]{start};
        }

        Queue<City_2_1_10> queue = new LinkedList<>();
        Set<City_2_1_10> visited = new HashSet<>();
        Map<City_2_1_10, City_2_1_10> previous = new HashMap<>();

        queue.add(start);
        visited.add(start);

        while (!queue.isEmpty()) {
            // Берём город из начала очереди
            City_2_1_10 current = queue.poll();

            if (current.equals(end)) {
                break;
            }

            Map<City_2_1_10, Integer> neighbors = current.getPaths();

            for (City_2_1_10 neighbor : neighbors.keySet()) {

                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    previous.put(neighbor, current); // запоминаем откуда пришли
                    queue.add(neighbor);
                }

            }
        }

        if (!previous.containsKey(end) && !start.equals(end)) {
            return new City_2_1_10[0];
        }

        // восстановление пути
        LinkedList<City_2_1_10> path = new LinkedList<>();
        City_2_1_10 current = end;

        while (current != null) {
            path.addFirst(current);
            current = previous.get(current);
        }

        return path.toArray(new City_2_1_10[0]);
    }

    @Override
    public String toString() {
        City_2_1_10[] route = getRoute();

        if (route.length == 0) {
            return "Путь не найден";
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < route.length; i++) {

            sb.append(route[i].toString().split(" -> ")[0]);

            if (i < route.length - 1) {
                sb.append(" -> ");
            }

        }

        return sb.toString();
    }
}
