import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (true) {
            int numOfFunction, numOfMethod, input, save;
            double a, b, eps;

            System.out.println("Это третья лабораторная работа по Вычислительной математике");
            System.out.println("""
                    Введите:
                    0 - для выхода
                    1 - для ввода данных из консоли""");

            input = inputInt(in);

            switch (input) {
                case (1):
                    while (true) {
                        System.out.println("""
                                Введите номер метода:
                                1 - Метод прямоугольников (левый)
                                2 - Метод прямоугольников (средний)
                                3 - Метод прямоугольников (правый)
                                4 - Метод трапеций
                                5 - Метод Симпсона""");
                        numOfMethod = inputInt(in);
                        if (numOfMethod < 1 || numOfMethod > 5) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    while (true) {
                        System.out.println("""
                                Введите номер функции:
                                1 - y = 4 * x^3 - 5 * x^2 + 6 * x - 71
                                2 - y = x^2 + x + 1
                                3 - y = 3 * x
                                4 - y = 1/x
                                5 - sign(x)""");
                        numOfFunction = inputInt(in);
                        if (numOfFunction < 1 || numOfFunction > 5) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    while (true) {
                        System.out.println("Введите a:");
                        a = inputDouble(in);
                        if (a == Double.MIN_VALUE) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    while (true) {
                        System.out.println("Введите b:");
                        b = inputDouble(in);
                        if (b == Double.MIN_VALUE) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    if (a >= b) {
                        System.out.println("Введите правильные границы а и b (a < b)");
                        continue;
                    }

                    while (true) {
                        System.out.println("Введите погрешность [0,0001; 1]:");
                        eps = inputDouble(in);
                        if (eps < 0.0001 || eps > 1.0) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    switch (numOfMethod) {
                        case (1) -> {
                            LeftRectangleMethod method1 = new LeftRectangleMethod();
                            method1.method1(a, b, eps, numOfFunction);
                        }
                        case (2) -> {
                            MidRectangleMethod method2 = new MidRectangleMethod();
                            method2.method2(a, b, eps, numOfFunction);
                        }
                        case (3) -> {
                            RightRectangleMethod method3 = new RightRectangleMethod();
                            method3.method3(a, b, eps, numOfFunction);
                        }
                        case (4) -> {
                            TrapesyMethod method4 = new TrapesyMethod();
                            method4.method4(a, b, eps, numOfFunction);
                        }
                        case (5) -> {
                            SimpsonMethod method5 = new SimpsonMethod();
                            method5.method5(a, b, eps, numOfFunction);
                        }
                    }

                    break;
                case (0):
                    System.out.println("Конец работы");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Некорректный ввод");
            }
        }
    }

    public static int inputInt(Scanner in) {
        int num;
        try {
            num = in.nextInt();
        } catch (Exception e) {
            if (!in.hasNextLine()) {
                System.out.println("Конец работы");
                System.exit(0);
            } else {
                System.out.println("Плохая строка");
            }
            in.nextLine();
            return -1;
        }
        return num;
    }

    public static double inputDouble(Scanner in) {
        double num;
        try {
            num = in.nextDouble();
        } catch (Exception e) {
            if (!in.hasNextLine()) {
                System.out.println("Конец работы");
                System.exit(0);
            } else {
                System.out.println("Плохая строка");
            }
            in.nextLine();
            return Double.MIN_VALUE;
        }
        return num;
    }

}
