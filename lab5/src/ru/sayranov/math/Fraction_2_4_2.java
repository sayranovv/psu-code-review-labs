package ru.sayranov.math;

public final class Fraction_2_4_2 extends Number {
    private final int chislitel;
    private final int znamenatel;

    public Fraction_2_4_2(int chislitel, int znamenatel) {
        if (znamenatel == 0) {
            throw new IllegalArgumentException("Знаменатель не может быть равен 0");
        }

        int nod = nod(Math.abs(chislitel), Math.abs(znamenatel));

        if (znamenatel < 0) {
            chislitel = -chislitel;
            znamenatel = -znamenatel;
        }
        this.chislitel = chislitel / nod;
        this.znamenatel = znamenatel / nod;
    }

    private int nod(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    @Override
    public String toString() {
        return chislitel + "/" + znamenatel;
    }

    public Fraction_2_4_2 sum(Fraction_2_4_2 other) {
        int num = this.chislitel * other.znamenatel + other.chislitel * this.znamenatel;
        int den = this.znamenatel * other.znamenatel;

        return new Fraction_2_4_2(num, den);
    }

    public Fraction_2_4_2 minus(Fraction_2_4_2 other) {
        int num = this.chislitel * other.znamenatel - other.chislitel * this.znamenatel;
        int den = this.znamenatel * other.znamenatel;

        return new Fraction_2_4_2(num, den);
    }

    public Fraction_2_4_2 minus(int n) {
        return this.minus(new Fraction_2_4_2(n, 1));
    }

    public Fraction_2_4_2 multiply(Fraction_2_4_2 other) {
        return new Fraction_2_4_2(this.chislitel * other.chislitel, this.znamenatel * other.znamenatel);
    }

    public Fraction_2_4_2 multiply(int n) {
        return new Fraction_2_4_2(this.chislitel * n, this.znamenatel);
    }

    public Fraction_2_4_2 div(Fraction_2_4_2 other) {
        if (other.chislitel == 0) {
            throw new IllegalArgumentException("Деление на ноль невозможно!");
        }

        return new Fraction_2_4_2(this.chislitel * other.znamenatel, this.znamenatel * other.chislitel);
    }

    public Fraction_2_4_2 div(int n) {
        if (n == 0) {
            throw new IllegalArgumentException("Деление на ноль невозможно!");
        }

        return new Fraction_2_4_2(this.chislitel, this.znamenatel * n);
    }

    @Override
    public int intValue() {
        return chislitel / znamenatel;
    }

    @Override
    public long longValue() {
        return (long) chislitel / znamenatel;
    }

    @Override
    public float floatValue() {
        return (float) chislitel / znamenatel;
    }

    @Override
    public double doubleValue() {
        return (double) chislitel / znamenatel;
    }
}