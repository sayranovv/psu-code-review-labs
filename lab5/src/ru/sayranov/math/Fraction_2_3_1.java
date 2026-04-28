package ru.sayranov.math;

public final class Fraction_2_3_1 {
    private final int chislitel;
    private final int znamenatel;

    public Fraction_2_3_1(int chislitel, int znamenatel) {
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

    public Fraction_2_3_1 sum(Fraction_2_3_1 other) {
        int num = this.chislitel * other.znamenatel + other.chislitel * this.znamenatel;
        int den = this.znamenatel * other.znamenatel;

        return new Fraction_2_3_1(num, den);
    }

    public Fraction_2_3_1 minus(Fraction_2_3_1 other) {
        int num = this.chislitel * other.znamenatel - other.chislitel * this.znamenatel;
        int den = this.znamenatel * other.znamenatel;

        return new Fraction_2_3_1(num, den);
    }

    public Fraction_2_3_1 minus(int n) {
        return this.minus(new Fraction_2_3_1(n, 1));
    }

    public Fraction_2_3_1 multiply(Fraction_2_3_1 other) {
        return new Fraction_2_3_1(this.chislitel * other.chislitel, this.znamenatel * other.znamenatel);
    }

    public Fraction_2_3_1 multiply(int n) {
        return new Fraction_2_3_1(this.chislitel * n, this.znamenatel);
    }

    public Fraction_2_3_1 div(Fraction_2_3_1 other) {
        if (other.chislitel == 0) {
            throw new IllegalArgumentException("Деление на ноль невозможно!");
        }

        return new Fraction_2_3_1(this.chislitel * other.znamenatel, this.znamenatel * other.chislitel);
    }

    public Fraction_2_3_1 div(int n) {
        if (n == 0) {
            throw new IllegalArgumentException("Деление на ноль невозможно!");
        }

        return new Fraction_2_3_1(this.chislitel, this.znamenatel * n);
    }
}