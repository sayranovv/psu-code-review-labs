package ru.sayranov.main;

public class Sum_2_5_1 {

    public static double sum(Number... numbers) {
        double result = 0.0;

        for (Number number : numbers) {
            result += number.doubleValue();
        }

        return result;
    }

}
