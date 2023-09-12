import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (true) {
            int numOfFunction, numOfMethod, input, save;
            double a, b, eps;

            System.out.println("Это вторая лабораторная работа по Вычислительной математике");
            System.out.println("""
                    Введите:
                    0 - для выхода
                    1 - для ввода данных из консоли
                    2 - для ввода данных из файла""");

            input = inputInt(in);

            switch (input) {
                case (1):
                    while (true) {
                        System.out.println("""
                                Введите номер метода:
                                1 - Метод половинного деления
                                4 - Метод секущих
                                5 - Метод простой итерации
                                6 - Метод Ньютона для решение систем нелинейных уравнений""");
                        numOfMethod = inputInt(in);
                        if (!(numOfMethod == 1 || numOfMethod == 4 || numOfMethod == 5 || numOfMethod == 6)) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    if (numOfMethod != 6) {
                        while (true) {
                            System.out.println("""
                                    Введите номер функции:
                                    1 - x^3 + 2.28 * x^2 - 1.934 * x - 3.907
                                    2 - x^3 + 3 * x^2 + 3 * x + 1
                                    3 - cos(x)
                                    4 - x^3 - x + 4""");
                            numOfFunction = inputInt(in);
                            if (numOfFunction < 0 || numOfFunction > 4) {
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

                        ArrayList<Double> tmp = Function.checkRoots(a, b, numOfFunction);
                        if (tmp.size() != 3) {
                            System.out.println("На данном интервале не один корень(" + (tmp.size() - 2) + ")");
                            for (int i = 0; i < tmp.size() - 2; i++) {
                                System.out.println("(" + Math.ceil(tmp.get(i)) + " ; " + Math.floor(tmp.get(i + 2)) + ")");

                            }
                            continue;
                        }

                    } else {
                        while (true) {
                            System.out.println("""
                                    Введите номер функции:
                                    1 - |x^2 + y^2 = 4
                                        |y = 3 * x^2
                                    2 - |x^2 + y^2 = 1
                                        |y = x""");
                            numOfFunction = inputInt(in);
                            if (numOfFunction < 0 || numOfFunction > 2) {
                                System.out.println("Некорректный ввод");
                                continue;
                            }
                            break;
                        }

                        while (true) {
                            System.out.println("Введите x0:");
                            a = inputDouble(in);
                            if (a == Double.MIN_VALUE) {
                                System.out.println("Некорректный ввод");
                                continue;
                            }
                            break;
                        }

                        while (true) {
                            System.out.println("Введите y0:");
                            b = inputDouble(in);
                            if (b == Double.MIN_VALUE) {
                                System.out.println("Некорректный ввод");
                                continue;
                            }
                            break;
                        }
                    }

                    while (true) {
                        System.out.println("Введите погрешность [0,0001; 1]:");
                        eps = inputDouble(in);
                        if (eps < 0.0001 || eps > 1) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    while (true) {
                        System.out.println("0 - сохранить в файл\n" +
                                "1 - вывести ответ в консоль");
                        save = inputInt(in);
                        if (!(save == 1 || save == 0)) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }
                        break;
                    }

                    Graph chart = new Graph();

                    switch (numOfMethod) {
                        case (1) -> {
                            Method1 method1 = new Method1();
                            method1.solve(a, b, eps, numOfFunction, save);
                            chart.drawFunction(a, b, numOfFunction, numOfMethod);
                        }
                        case (4) -> {
                            SecantMethod method3 = new SecantMethod();
                            method3.solve(a, b, eps, numOfFunction, save);
                            chart.drawFunction(a, b, numOfFunction, numOfMethod);
                        }
                        case (5) -> {
                            SimpleIterationMethod method5 = new SimpleIterationMethod();
                            method5.solve(a, b, eps, numOfFunction, save);
                            chart.drawFunction(a, b, numOfFunction, 5);
                        }
                        case (6) -> {
                            NewtonMethod method6 = new NewtonMethod();
                            method6.solve(a, b, eps, numOfFunction, save);
                            chart.drawTwoFunction(numOfFunction);
                        }
                    }

                    break;
                case (2):
                    BufferedReader bufferedReader;
                    String name = "";

                    System.out.println("Введите имя файла:");
                    while (name.equals("")) {
                        name = in.nextLine();
                    }

                    try {
                        bufferedReader = new BufferedReader(new FileReader("src/main/resources/" + name));
                    } catch (FileNotFoundException e) {
                        System.out.println("Не удалось открыть файл");
                        continue;
                    }

                    try {
                        numOfMethod = Integer.parseInt(bufferedReader.readLine());
                    } catch (Exception e) {
                        System.out.println("Ошибка при чтении");
                        continue;
                    }
                    if (!(numOfMethod == 1 || numOfMethod == 4 || numOfMethod == 5 || numOfMethod == 6)) {
                        System.out.println("Некорректный ввод");
                        continue;
                    }

                    if (numOfMethod != 6) {
                        try {
                            numOfFunction = Integer.parseInt(bufferedReader.readLine());
                        } catch (Exception e) {
                            System.out.println("Ошибка при чтении");
                            continue;
                        }
                        if (numOfFunction < 0 || numOfFunction > 4) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }

                        try {
                            a = Double.parseDouble(bufferedReader.readLine());
                        } catch (Exception e) {
                            System.out.println("Ошибка при чтении");
                            continue;
                        }

                        try {
                            b = Double.parseDouble(bufferedReader.readLine());
                        } catch (Exception e) {
                            System.out.println("Ошибка при чтении");
                            continue;
                        }

                        if (a >= b) {
                            System.out.println("Введите правильные границы а и b (a < b)");
                            continue;
                        }

                        ArrayList<Double> tmp = Function.checkRoots(a, b, numOfFunction);
                        if (tmp.size() != 3) {
                            System.out.println("На данном интервале не один корень(" + (tmp.size() - 2) + ")");
                            for (int i = 0; i < tmp.size() - 2; i++) {
                                System.out.println("(" + tmp.get(i) + " ; " + tmp.get(i + 2) + ")");

                            }
                            continue;
                        }

                    } else {
                        try {
                            numOfFunction = Integer.parseInt(bufferedReader.readLine());
                        } catch (Exception e) {
                            System.out.println("Ошибка при чтении");
                            continue;
                        }
                        if (numOfFunction < 0 || numOfFunction > 2) {
                            System.out.println("Некорректный ввод");
                            continue;
                        }

                        try {
                            a = Double.parseDouble(bufferedReader.readLine());
                        } catch (Exception e) {
                            System.out.println("Ошибка при чтении");
                            continue;
                        }

                        try {
                            b = Double.parseDouble(bufferedReader.readLine());
                        } catch (Exception e) {
                            System.out.println("Ошибка при чтении");
                            continue;
                        }
                    }

                    try {
                        eps = Double.parseDouble(bufferedReader.readLine());
                    } catch (Exception e) {
                        System.out.println("Ошибка при чтении");
                        continue;
                    }
                    if (eps < 0.0001 || eps > 1) {
                        System.out.println("Некорректный ввод");
                        continue;
                    }

                    try {
                        save = Integer.parseInt(bufferedReader.readLine());
                    } catch (Exception e) {
                        System.out.println("Ошибка при чтении");
                        continue;
                    }

                    if (!(save == 1 || save == 0)) {
                        System.out.println("Некорректный ввод");
                        continue;
                    }

                    System.out.println("Прочитанные данные:\n" +
                            "Номер метода: " + numOfMethod + "\n" +
                            "Номер функции: " + numOfFunction + "\n" +
                            "a: " + a + "\n" +
                            "b: " + b + "\n" +
                            "Погрешность: " + eps + "\n" +
                            "Режим сохранения: " + save + "\n");

                    Graph chart1 = new Graph();

                    switch (numOfMethod) {
                        case (1) -> {
                            Method1 method1 = new Method1();
                            method1.solve(a, b, eps, numOfFunction, save);
                            chart1.drawFunction(a, b, numOfFunction, numOfMethod);
                        }
                        case (4) -> {
                            SecantMethod method4 = new SecantMethod();
                            method4.solve(a, b, eps, numOfFunction, save);
                            chart1.drawFunction(a, b, numOfFunction, numOfMethod);
                        }
                        case (5) -> {
                            SimpleIterationMethod method5 = new SimpleIterationMethod();
                            method5.solve(a, b, eps, numOfFunction, save);
                            chart1.drawFunction(a, b, numOfFunction, 5);
                        }
                        case (6) -> {
                            NewtonMethod method6 = new NewtonMethod();
                            method6.solve(a, b, eps, numOfFunction, save);
                            chart1.drawTwoFunction(numOfFunction);
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
