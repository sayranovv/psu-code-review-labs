package ru.sayranov.geography;

import java.util.*;
import java.util.stream.Collectors;

public class City_2_6_5 {

    private final String name;
    private final Map<City_2_6_5, Integer> paths;

    public City_2_6_5(String name) {
        this.name = name;
        this.paths = new HashMap<>();
    }

    public City_2_6_5(String name, Map<City_2_6_5, Integer> initialPaths) {
        this.name = name;
        this.paths = new HashMap<>(initialPaths);

        for (Map.Entry<City_2_6_5, Integer> entry : initialPaths.entrySet()) {
            addPath(entry.getKey(), entry.getValue());
        }
    }

    public void addPath(City_2_6_5 city, int cost) {
        if (city == null) {
            throw new IllegalArgumentException("Город не может быть null");
        }

        if (city == this) {
            throw new IllegalArgumentException("Нельзя соединить город сам с собой");
        }

        if (cost <= 0) {
            throw new IllegalArgumentException("Стоимость дороги должна быть положительной");
        }

        if (paths.containsKey(city)) {
            System.out.println("Между " + name + " и " + city.name + " уже есть дорога!");
            return;
        }

        paths.put(city, cost);

        // обратная связь
        if (!city.paths.containsKey(this)) {
            city.paths.put(this, cost);
        }
    }

    public void removePath(City_2_6_5 city) {
        if (city == null) return;

        paths.remove(city);
        city.paths.remove(this);
    }

    public Map<City_2_6_5, Integer> getPaths() {
        return Map.copyOf(paths);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(name).append(" -> ");

        for (Map.Entry<City_2_6_5, Integer> entry : paths.entrySet()) {
            sb.append(entry.getKey().name).append(":").append(entry.getValue()).append(" ");
        }

        return sb.toString();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof City_2_6_5 other)) return false;

        return pathsEquals(this.paths, other.paths);
    }

    @Override
    public int hashCode() {
        List<String> pathStrings = new ArrayList<>();

        for (Map.Entry<City_2_6_5, Integer> entry : paths.entrySet()) {
            pathStrings.add(entry.getKey().name + ":" + entry.getValue());
        }

        Collections.sort(pathStrings);

        return Objects.hash(pathStrings);
    }

    private boolean pathsEquals(Map<City_2_6_5, Integer> paths1, Map<City_2_6_5, Integer> paths2) {
        if (paths1.size() != paths2.size()) return false;

        Set<String> pathSet1 = paths1.entrySet().stream()
                .map(entry -> entry.getKey().name + ":" + entry.getValue())
                .collect(Collectors.toSet());

        Set<String> pathSet2 = paths2.entrySet().stream()
                .map(entry -> entry.getKey().name + ":" + entry.getValue())
                .collect(Collectors.toSet());

        return pathSet1.equals(pathSet2);
    }
}