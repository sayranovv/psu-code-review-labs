package ru.sayranov.math;

public class PowerCalc_2_7_3 {
    private static int pInt(String s) { return Integer.parseInt(s); }
    private static double pPow(int x, int y) { return Math.pow(x, y); }

    public static double power(String xStr, String yStr) {
        int x = pInt(xStr);
        int y = pInt(yStr);
        return pPow(x, y);
    }
}
