package ru.sayranov.main;

import ru.sayranov.geography.City_2_1_10;
import ru.sayranov.geography.City_2_6_5;
import ru.sayranov.geography.Route_2_2_5;
import ru.sayranov.math.Fraction_2_1_4;
import ru.sayranov.math.Fraction_2_4_2;
import ru.sayranov.math.Fraction_2_3_1;
import ru.sayranov.math.PowerCalc_2_7_3;

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

        if (exercise == 1 && task == 4) {
            System.out.println("------------ Задача 1 | Задание 4 ------------");

            Fraction_2_1_4 f1 = new Fraction_2_1_4(1, 2);
            Fraction_2_1_4 f2 = new Fraction_2_1_4(3, 4);
            Fraction_2_1_4 f3 = new Fraction_2_1_4(-2, 5);
            Fraction_2_1_4 f4 = new Fraction_2_1_4(2, -5);

            System.out.println("f1 = " + f1);
            System.out.println("f2 = " + f2);
            System.out.println("f3 = " + f3);
            System.out.println("f4 = " + f4);

            System.out.println("\nОперации:");
            System.out.println("f1 + f2 = " + f1.sum(f2));
            System.out.println("f1 - f2 = " + f1.minus(f2));
            System.out.println("f1 * f2 = " + f1.multiply(f2));
            System.out.println("f1 / f2 = " + f1.div(f2));

            System.out.println("\nОперации с целыми:");
            System.out.println("f1 - 1 = " + f1.minus(1));
            System.out.println("f2 * 2 = " + f2.multiply(2));
            System.out.println("f3 / 2 = " + f3.div(2));
        } else if (exercise == 1 && task == 10) {
            System.out.println("------------ Задача 1 | Задание 10 ------------");

            City_2_1_10 perm = new City_2_1_10("Пермь");
            City_2_1_10 moscow = new City_2_1_10("Москва");
            City_2_1_10 kazan = new City_2_1_10("Казань");

            perm.addPath(moscow, 1400);
            perm.addPath(kazan, 600);
            moscow.addPath(kazan, 800);

            moscow.addPath(perm, 1400);

            System.out.println("Сети дорог:");
            System.out.println(perm);
            System.out.println(moscow);
            System.out.println(kazan);

            System.out.println("\nУдаляем дорогу Пермь-Казань...");
            perm.removePath(kazan);

            System.out.println(perm);
            System.out.println(kazan);

        } else if (exercise == 2 && task == 5) {
            System.out.println("------------ Задача 2 | Задание 5 ------------");

            City_2_1_10 a = new City_2_1_10("A");
            City_2_1_10 b = new City_2_1_10("B");
            City_2_1_10 c = new City_2_1_10("C");
            City_2_1_10 d = new City_2_1_10("D");
            City_2_1_10 e = new City_2_1_10("E");
            City_2_1_10 f = new City_2_1_10("F");

            a.addPath(b, 5);
            a.addPath(f, 1);
            a.addPath(d, 6);
            b.addPath(c, 3);
            c.addPath(d, 4);
            d.addPath(e, 2);
            e.addPath(f, 2);
            f.addPath(b, 1);

            Route_2_2_5 route = new Route_2_2_5(f, d);
            System.out.println("Маршрут из F в D:");
            System.out.println(route);

        } else if (exercise == 3 && task == 1) {
            System.out.println("------------ Задача 3 | Задание 1 ------------");

            Fraction_2_3_1 a = new Fraction_2_3_1(1, 2);
            Fraction_2_3_1 b = new Fraction_2_3_1(3, 4);

            System.out.println("a = " + a);
            System.out.println("b = " + b);
            System.out.println("a + b = " + a.sum(b));
            System.out.println("a - b = " + a.minus(b));
            System.out.println("a * b = " + a.multiply(b));
            System.out.println("a / b = " + a.div(b));

//            попробуем унаследовать и получаем ошибку компиляции:
//            class MutableFraction extends ru.sayranov.math.Fraction_2_3_1 {  }

        } else if (exercise == 4 && task == 2) {
            System.out.println("------------ Задача 4 | Задание 2 ------------");

            Number n = new Fraction_2_4_2(2, 5);
            System.out.println("Number (2/5) как double: " + n.doubleValue());
            System.out.println("Number (2/5) как float:  " + n.floatValue());
            System.out.println("Number (2/5) как int:    " + n.intValue());
            System.out.println("Number (2/5) как long:   " + n.longValue());

            System.out.println();
        } else if (exercise == 5 && task == 1) {
            System.out.println("------------ Задача 5 | Задание 1 ------------");

            System.out.println("2 + 3/5 + 2.3 = " +
                    Sum_2_5_1.sum(2, new Fraction_2_4_2(3, 5), 2.3));

            System.out.println("3.6 + 49/12 + 3 + 3/2 = " +
                    Sum_2_5_1.sum(3.6, new Fraction_2_4_2(49, 12), 3, new Fraction_2_4_2(3, 2)));

            System.out.println("1/3 + 1 = " +
                    Sum_2_5_1.sum(new Fraction_2_4_2(1, 3), 1));
        } else if (exercise == 6 && task == 5) {
            System.out.println("------------ Задача 6 | Задание 5 ------------");

            City_2_6_5 city1 = new City_2_6_5("Москва");
            City_2_6_5 city2 = new City_2_6_5("Санкт-Петербург");
            City_2_6_5 city3 = new City_2_6_5("Казань");

            city1.addPath(city2, 100);
            city1.addPath(city3, 200);

            City_2_6_5 city4 = new City_2_6_5("Владивосток");
            city4.addPath(city2, 100);
            city4.addPath(city3, 200);

            System.out.println(city1.equals(city4)); // true

        } else if (exercise == 7 && task == 3) {
            if (args.length < 2) {
                System.out.println("Использование: java Main <X> <Y>");
                return;
            }

            double result = PowerCalc_2_7_3.power(args[0], args[1]);
            System.out.println(args[0] + " ^ " + args[1] + " = " + result);
        } else {
            valid = false;
        }

        if (!valid) {
            System.out.println("Нет такой задачи!");
        }
    }
}
