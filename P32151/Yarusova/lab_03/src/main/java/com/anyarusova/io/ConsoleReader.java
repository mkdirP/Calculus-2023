package com.anyarusova.io;


import java.util.Scanner;
import java.util.function.Function;

public class ConsoleReader implements Reader {
    Scanner scanner = new Scanner(System.in);

    @Override
    public Function<Double, Double> chooseEquation() {
        System.out.println("Choose the equation:");
        System.out.println("1. 2x^3 - 2x^2 + 7x - 14 (default)");
        System.out.println("2. x^3 - 2x^2 + 3x - 4");
        System.out.println("3. sin x");
        System.out.println("4. cos x");
        System.out.println("5. x^2 - 2x + 1");
        int equation = scanner.nextInt();
        if (equation < 1 || equation > 5) {
            System.out.println("Invalid equation input");
            System.out.println("Equation = 1");
            equation = 1;
        }
        return switch (equation) {
            case 2 -> x -> Math.pow(x, 3) - 2 * Math.pow(x, 2) + 3 * x - 4;
            case 3 -> Math::sin;
            case 4 -> Math::cos;
            case 5 -> x -> Math.pow(x, 2) - 2 * x + 1;
            default -> x -> 2 * Math.pow(x, 3) - 2 * Math.pow(x, 2) + 7 * x - 14;
        };
    }

    @Override
    public Function<Double, Double> chooseExtraEquation() {
        System.out.println("Choose the equation:");
        System.out.println("1. 1 / sqrt(x) (default)");
        System.out.println("2. 1 / x");
        System.out.println("3. 1 / (1 - x^2)");
        int equation = scanner.nextInt();
        if (equation < 1 || equation > 5) {
            System.out.println("Invalid equation input");
            System.out.println("Equation = 1");
            equation = 1;
        }
        return switch (equation) {
            case 2 -> x -> 1 / x;
            case 3 -> x -> 1 / (1 - Math.pow(x, 2));
            default -> x -> 1 / Math.sqrt(x);
        };
    }

    @Override
    public int chooseMethod() {
        System.out.println("Choose the method:");
        System.out.println("1. Method of left rectangles (default)");
        System.out.println("2. Method of right rectangles");
        System.out.println("3. Method of middle rectangles");
        System.out.println("4. Method of trapezium");
        System.out.println("5. Method of Simpson");
        int method = scanner.nextInt();
        if (method < 1 || method > 5) {
            System.out.println("Invalid method input");
            System.out.println("Method = 1");
            method = 1;
        }
        return method;
    }

    @Override
    public double chooseEpsilon() {
        System.out.println("Choose epsilon");
        double epsilon = scanner.nextDouble();
        if (epsilon <= 0) {
            System.out.println("Invalid epsilon input (must be > 0)");
            System.out.println("Epsilon = 0.001");
            epsilon = 0.001;
        }
        return epsilon;
    }

    @Override
    public double chooseLeftBound() {
        System.out.println("Choose left bound");
        return scanner.nextDouble();
    }

    @Override
    public double chooseRightBound() {
        System.out.println("Choose right bound");
        return scanner.nextDouble();
    }
}
