import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (true) {
            int numOfFunction = 0, input;
            double x0, y0, xn, h, eps;

            System.out.println("Это шестая лабораторная работа по Вычислительной математике");
            System.out.println("""
                    Введите:
                    0 - для выхода
                    1 - для ввода данных из консоли""");

            input = inputInt(in);

            switch (input) {
                case (1) -> {
                    while (true) {
                        System.out.println("""
                                    Введите номер функции:
                                    1 - y' = 2x - y
                                    2 - y' = y + (1 + x) * y
                                    3 - y' = y * x + x * y""");
                        numOfFunction = inputInt(in);
                        if (numOfFunction < 1 || numOfFunction > 3) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    while (true) {
                        System.out.println("Введите x0:");
                        x0 = inputDouble(in);
                        if (x0 == Double.MIN_VALUE) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    while (true) {
                        System.out.println("Введите xn:");
                        xn = inputDouble(in);
                        if (xn == Double.MIN_VALUE) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    if (x0 >= xn) {
                        System.out.println("Введите правильные границы x0 и xn (x0 < xn)");
                        continue;
                    }

                    while (true) {
                        System.out.println("Введите y0:");
                        y0 = inputDouble(in);
                        if (y0 == Double.MIN_VALUE) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    while (true) {
                        System.out.println("Введите h:");
                        h = inputDouble(in);
                        if (h == Double.MIN_VALUE) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    while (true) {
                        System.out.println("Введите eps:");
                        eps = inputDouble(in);
                        if (eps == Double.MIN_VALUE) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    System.out.println("Модифифцированный Эйлер " + ModifiedEulerMethod.modifiedEulerMethod(x0, y0, h, xn, numOfFunction));
                    System.out.println("Модифифцированный Эйлер+ " + ModifiedEulerMethod.solve(x0, y0, h, xn, eps, numOfFunction));
                    System.out.println("Рунге " + RungeKuttaMethod.rungeKuttaMethod(x0, y0, h, xn, numOfFunction));
                    System.out.println("Рунге+ " + RungeKuttaMethod.solve(x0, y0, h, xn, eps, numOfFunction));
                    double[] y1 = AdamsMethod.adamsMethod(x0, y0, h, xn, numOfFunction);
                    System.out.println("Адамс " + (y1 != null ? y1[y1.length - 1] : "Малый шаг"));
                    double[] y2 = AdamsMethod.solve(x0, y0, h, xn, eps, numOfFunction);
                    System.out.println("Адамс+ " + (y2 != null ? y2[y2.length - 1] : "Малый шаг"));
                    Chart.draw(y1, y2, x0, h);
                }
                case (0) -> {
                    System.out.println("Конец работы");
                    System.exit(0);
                }
                default -> {
                    System.out.println("Некорректный ввод");
                    continue;
                }
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
