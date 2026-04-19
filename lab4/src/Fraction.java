public class Fraction {
    private final int chislitel;
    private final int znamenatel;

    public Fraction(int chislitel, int znamenatel) {
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

    public Fraction sum(Fraction other) {
        int num = this.chislitel * other.znamenatel + other.chislitel * this.znamenatel;
        int den = this.znamenatel * other.znamenatel;

        return new Fraction(num, den);
    }

    public Fraction minus(Fraction other) {
        int num = this.chislitel * other.znamenatel - other.chislitel * this.znamenatel;
        int den = this.znamenatel * other.znamenatel;

        return new Fraction(num, den);
    }

    public Fraction minus(int n) {
        return this.minus(new Fraction(n, 1));
    }

    public Fraction multiply(Fraction other) {
        return new Fraction(this.chislitel * other.chislitel, this.znamenatel * other.znamenatel);
    }

    public Fraction multiply(int n) {
        return new Fraction(this.chislitel * n, this.znamenatel);
    }

    public Fraction div(Fraction other) {
        if (other.chislitel == 0) {
            throw new IllegalArgumentException("Деление на ноль невозможно!");
        }

        return new Fraction(this.chislitel * other.znamenatel, this.znamenatel * other.chislitel);
    }

    public Fraction div(int n) {
        if (n == 0) {
            throw new IllegalArgumentException("Деление на ноль невозможно!");
        }

        return new Fraction(this.chislitel, this.znamenatel * n);
    }
}
