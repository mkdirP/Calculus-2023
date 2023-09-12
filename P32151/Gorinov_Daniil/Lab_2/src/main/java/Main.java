import graphs.GraphPoints;
import tools.MathAndPrintTools;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    public static double[] eq;
    public static int N;

    private static Scanner getInfo() throws FileNotFoundException {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ввод данных из файла или с консоли? (Напишите 'file' или 'console' соответственно)");
        String str = scanner.nextLine();
        boolean isFile = false;
        while (!isFile && !str.equalsIgnoreCase("console")) {
            if (str.equalsIgnoreCase("file")) {
                isFile = true;
            } else {
                System.out.println("Некорректный ввод. Пожалуйста, повторите");
                str = scanner.nextLine();
            }
        }

        if (isFile) {
            System.out.println("Введите путь к файлу:");
            File file = new File(scanner.nextLine());
            scanner = new Scanner(file);
        } else {
            System.out.println("Введите параметры: точность, A и B");
        }
        return scanner;
    }

    public static void printResultToFile() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Вывести результат в отдельный файл?(YES/NO)");
        String answer = scanner.nextLine();
        boolean toFile = answer.equalsIgnoreCase("yes");
        if (toFile) {
            System.out.println("Введите имя файла:");
            String filename = scanner.nextLine();
            MathAndPrintTools.printToFile(filename);
        } else {
            System.out.println("Выход...");
            System.exit(0);
        }
    }

    public static void main(String[] args) {
        boolean transcendent = false;
        Scanner scanner = new Scanner(System.in);
        System.out.print("Выберите выражение из следующего списка:\n" +
                "1) 3x^5+x^4-0,4x^3+2,8x^2+10,4x-8\n" +
                "2) x^3+2,84x^2-5,606x-14,766\n" +
                "3) x^2-x-sin(x)\n" +
                "4) x^3-x+4\n" +
                "5) x1^2-2x2=0\n  3x1+3-x2^2=0\n" +
                "Ввод номера выражения: ");
        double newToneResult = 0.0;
        try {
            N = scanner.nextInt();
            switch (N) {
                case 1:
                    eq = new double[] {-8, 10.4, 2.8, -0.4, 1, 3};
                    break;
                case 2:
                    eq = new double[] {-14.766, -5.606, 2.84, 1};
                    break;
                case 3:
                    eq = new double[] {-1, -1, 1};
                    transcendent = true;
                    break;
                case 4:
                    eq = new double[] {4, -1, 0, 1};
                    break;
                case 5:
                    System.out.println("Введите параметры: точность, A и B");
                    double epsLocal = scanner.nextDouble();
                    double aLocal = scanner.nextDouble();
                    double bLocal = scanner.nextDouble();
                    newToneResult = MethodNewTon.initSolve(epsLocal, aLocal, bLocal);
                    printResultToFile();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Некорректный ввод");
                    System.exit(12);
                    break;
            }
        } catch (Exception e) {
            System.out.println("Ошибка ввода! Завершение работы программы...");
            System.exit(13);
        } finally {
            Scanner sc2 = new Scanner(System.in);
            System.out.println("Введите предварительные интервалы для изоляции корней: ");
            double a1 = sc2.nextDouble();
            double b1 = sc2.nextDouble();
            if (a1 > 1000000) {
                System.out.println("Левая граница превышает лимит в 1 млн. Число сокращено до максимально допустимого значения");
                a1 = 1000000;
            }
            if (b1 > 1000000) {
                System.out.println("Правая граница превышает лимит в 1 млн. Число сокращено до максимально допустимого значения");
                b1 = 1000001;
            }
            MathAndPrintTools.fillMap(a1, b1, eq, transcendent);
            if (newToneResult != 0.0) new GraphPoints(MathAndPrintTools.points, newToneResult);
        }

        try {
            scanner = getInfo();
        } catch (FileNotFoundException e) {
            System.out.println("Ошибка! Файл не был найден! Ввод параметров (точность, A и B) с консоли.");
            scanner = new Scanner(System.in);
        }

        double eps = scanner.nextDouble();
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();


        System.out.println("Выберите метод для нахождения решения:\n" +
                "1) Итерационный (iter)\n" +
                "2) Половинного деления (half)\n" +
                "3) Секущих (secant)");
        scanner = new Scanner(System.in);
        String str = scanner.nextLine();
        int i;
        while (true) {
            if (str.equalsIgnoreCase("iter")) {
                i = 1;
                break;
            }
            if (str.equalsIgnoreCase("half")) {
                i = 2;
                break;
            }
            if (str.equalsIgnoreCase("secant")) {
                i = 3;
                break;
            }
            System.out.println("Некорректный ввод. Пожалуйста, повторите");
            str = scanner.nextLine();
        }
        double answer = 0.0;
        switch (i) {
            case 1:
                answer = MethodSimpleIterations.initSolve(eq, a, b, eps, transcendent);
                break;
            case 2:
                MethodOfPartDiv method = new MethodOfPartDiv(eq, eps, transcendent);
                answer = method.findRightSolution(a, b);
                break;
            case 3:
                answer = MethodSecant.initSolve(eq, a, b, eps, transcendent);
                break;
        }

        new GraphPoints(MathAndPrintTools.points, answer);

        printResultToFile();
    }
}