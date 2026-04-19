import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int exercise = 0;
        int task = 0;

        while (true) {
            System.out.println("Введите номер задания:");
            if (sc.hasNextInt()) {
                exercise = sc.nextInt();
                break;
            } else {
                System.out.println("Ошибка! Пожалуйста, введите целое число");
                sc.next();
            }
        }

        while (true) {
            System.out.println("Введите номер задачи:");
            if (sc.hasNextInt()) {
                task = sc.nextInt();
                break;
            } else {
                System.out.println("Ошибка! Пожалуйста, введите целое число");
                sc.next();
            }
        }

        boolean valid = true;

        if (exercise == 1 && task == 2) {

            System.out.println("------------ Задача 1 | Задание 2 ------------");

            Person p1 = new Person("Клеопатра", 152);
            Person p2 = new Person("Пушкин", 167);
            Person p3 = new Person("Владимир", 189);

            System.out.println("Созданные люди:");
            System.out.println(p1);
            System.out.println(p2);
            System.out.println(p3);

        } else if (exercise == 1 && task == 3) {

            System.out.println("------------ Задача 1 | Задание 3 ------------");

            Name n1 = new Name(null, "Клеопатра", null);
            Name n2 = new Name("Пушкин", "Александр", "Сергеевич");
            Name n3 = new Name("Маяковский", "Владимир", null);

            System.out.println("Созданные имена:");
            System.out.println(n1);
            System.out.println(n2);
            System.out.println(n3);

        } else if (exercise == 2 && task == 2) {

            System.out.println("------------ Задача 2 | Задание 2 ------------");

            Name n1 = new Name(null, "Клеопатра", null);
            Name n2 = new Name("Пушкин", "Александр", "Сергеевич");
            Name n3 = new Name("Маяковский", "Владимир", null);

            PersonWithName p1 = new PersonWithName(n1, 152);
            PersonWithName p2 = new PersonWithName(n2, 167);
            PersonWithName p3 = new PersonWithName(n3, 189);

            System.out.println(p1);
            System.out.println(p2);
            System.out.println(p3);

        } else if (exercise == 3 && task == 3) {

            System.out.println("------------ Задача 3 | Задание 3 ------------");

            City a = new City("A");
            City b = new City("B");
            City c = new City("C");
            City d = new City("D");
            City e = new City("E");
            City f = new City("F");

            a.addPath(b, 5);
            a.addPath(f, 1);
            a.addPath(d, 6);
            b.addPath(a, 5);
            b.addPath(c, 3);
            c.addPath(b, 3);
            c.addPath(d, 4);
            d.addPath(a, 6);
            d.addPath(c, 4);
            d.addPath(e, 2);
            e.addPath(f, 2);
            f.addPath(b, 1);
            f.addPath(e, 2);

            System.out.println("Реализованная схема:");
            System.out.println(a);
            System.out.println(b);
            System.out.println(c);
            System.out.println(d);
            System.out.println(e);
            System.out.println(f);


        } else if (exercise == 4 && task == 8) {

            System.out.println("------------ Задача 4 | Задание 8 ------------");

            City a, b, c, d, e, f;

            Map<City, Integer> pathsA = new HashMap<>();
            Map<City, Integer> pathsB = new HashMap<>();
            Map<City, Integer> pathsC = new HashMap<>();
            Map<City, Integer> pathsD = new HashMap<>();
            Map<City, Integer> pathsE = new HashMap<>();
            Map<City, Integer> pathsF = new HashMap<>();

            a = new City("A");
            b = new City("B");
            c = new City("C");
            d = new City("D");
            e = new City("E");
            f = new City("F");

            pathsA.put(b, 5);
            pathsA.put(f, 1);
            pathsA.put(d, 6);

            pathsB.put(a, 5);
            pathsB.put(c, 3);

            pathsC.put(b, 3);
            pathsC.put(d, 4);

            pathsD.put(a, 6);
            pathsD.put(c, 4);
            pathsD.put(e, 2);

            pathsE.put(f, 2);

            pathsF.put(b, 1);
            pathsF.put(e, 2);

            a = new City("A", pathsA);
            b = new City("B", pathsB);
            c = new City("C", pathsC);
            d = new City("D", pathsD);
            e = new City("E", pathsE);
            f = new City("F", pathsF);

            System.out.println(a);
            System.out.println(b);
            System.out.println(c);
            System.out.println(d);
            System.out.println(e);
            System.out.println(f);

        } else if (exercise == 5 && task == 5) {

            System.out.println("------------ Задача 5 | Задание 5 ------------");

            Fraction f1 = new Fraction(1, 3);
            Fraction f2 = new Fraction(2, 3);
            Fraction f3 = new Fraction(4, 5);

            System.out.println(f1 + " + " + f2 + " = " + f1.sum(f2));
            System.out.println(f1 + " - " + f2 + " = " + f1.minus(f2));
            System.out.println(f1 + " * " + f2 + " = " + f1.multiply(f2));
            System.out.println(f1 + " / " + f2 + " = " + f1.div(f2));
            System.out.println(f1 + " - 1 = " + f1.minus(1));

            Fraction result = f1.sum(f2).div(f3).minus(5);
            System.out.println("(" + f1 + " + " + f2 + ") / " + f3 + " - 5 = " + result);

        } else {
            valid = false;
        }

        if (!valid) {
            System.out.println("Нет такой задачи!");
        }

        sc.close();
    }
}