import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class SecantMethod{
/*
    ArrayList<Double> a = new ArrayList<Double>();
    ArrayList<Double> b = new ArrayList<Double>();
    ArrayList<Double> fa = new ArrayList<Double>();
    ArrayList<Double> x = new ArrayList<Double>();
    ArrayList<Double> ab = new ArrayList<Double>();

    Scanner scanner = new Scanner(System.in);

    public void solve(double sa, double sb, double eps, int n, int save){
        System.out.println("f(a) = "+ Function.getFunction(sa, n));
        System.out.println("f``(a) = "+ Function.getDerivativeFunction2(sa, n));
        System.out.println("f(b) = "+ Function.getFunction(sb, n));
        System.out.println("f``(b) = "+ Function.getDerivativeFunction2(sb, n));
        if (Function.getFunction(sa, n) * Function.getDerivativeFunction2(sa, n) > 0) {
            System.out.println("x0 = "+ sa);
            a.add(sa);
            System.out.println("Введите x1:");
            double x1 = scanner.nextDouble();
            b.add(x1);
        } else  {
            System.out.println("x0 = "+ sb);
            a.add(sb);
            System.out.println("Введите x1:");
            double x1 = scanner.nextDouble();
            b.add(x1);
        }



        int check = 200;

        do {
            fa.add(b.get(b.size() - 1) - (b.get(b.size() - 1) - a.get(a.size() - 1)) /
                    (Function.getFunction(b.get(b.size() - 1), n) - Function.getFunction(a.get(a.size() - 1), n)) *
                    Function.getFunction(b.get(b.size() - 1), n));
            x.add(Function.getFunction(fa.get(fa.size() - 1), n));
            ab.add(Math.abs(fa.get(fa.size() - 1) - b.get(b.size() - 1)));
            a.add(b.get(b.size() - 1));
            b.add(fa.get(fa.size() - 1));
        } while (ab.get(ab.size() - 1) > eps && check-- > 0);

        fa.add(b.get(b.size() - 1) - (b.get(b.size() - 1) - a.get(a.size() - 1)) /
                (Function.getFunction(b.get(b.size() - 1), n) - Function.getFunction(a.get(a.size() - 1), n)) *
                Function.getFunction(b.get(b.size() - 1), n));
        x.add(Function.getFunction(fa.get(fa.size() - 1), n));
        ab.add(Math.abs(fa.get(fa.size() - 1) - b.get(b.size() - 1)));

        if (check <= 0) {
            System.out.println("Метод не сходится");
            return;
        }
        if (save == 1) {
            printConsole(n);
        } else {
            printFile(n);
        }
    }

    public void printConsole(int n) {
        System.out.println("+------------------------------------------------" +
                "-----------------------------------------------+\n");
        System.out.printf("|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|\n",
                "№", " xk-1", " xk", " xk+1", " f(x", " |xk+1 - xk| ");
        System.out.println("+---------------+---------------+---------------+" +
                "---------------+---------------+---------------+\n");

        for (int i = 0; i < a.size(); i++) {
            System.out.printf("|%-15d|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|\n",
                    i, a.get(i), fa.get(i), x.get(i), b.get(i), ab.get(i));
            System.out.println("+---------------+---------------+---------------+" +
                    "---------------+---------------+---------------+\n");
        }
        System.out.println("x = " + b.get(b.size() - 1) + " f(x) = " + Function.getFunction(b.get(b.size() - 1), n) + " n = " + a.size());
    }

    public void printFile(int n) {
        try {
            FileWriter fileWriter = new FileWriter("src/main/resources/method3-" + n + ".txt");
            fileWriter.write("+------------------------------------------------" +
                    "-----------------------------------------------+");
            fileWriter.write(String.format("|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|\n",
                    "№", " xk", " f(xk)", " f`(xk)", " xk+1", " |xk+1 - xk| "));
            fileWriter.write("+---------------+---------------+---------------+" +
                    "---------------+---------------+---------------+");
            for (int i = 0; i < fa.size(); i++) {
                fileWriter.write(String.format("|%-15d|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|\n",
                        i, a.get(i), fa.get(i), x.get(i), b.get(i), ab.get(i)));
                fileWriter.write("+---------------+---------------+---------------+" +
                        "---------------+---------------+---------------+");
            }
            System.out.println("x = " + b.get(b.size() - 1) + " f(x) = " + Function.getFunction(b.get(b.size() - 1), n) + " n = " + a.size());
        } catch (IOException e) {
            System.out.println("Не удалось сохранить");
        }
    }
*/
ArrayList<Double> a = new ArrayList<Double>();
    ArrayList<Double> b = new ArrayList<Double>();
    ArrayList<Double> fa = new ArrayList<Double>();
    ArrayList<Double> fa1 = new ArrayList<Double>();
    ArrayList<Double> ab = new ArrayList<Double>();

    public void solve(double sa, double sb, double eps, int n, int save) {
        System.out.println("f(a) = "+ Function.getFunction(sa, n));
        System.out.println("f``(a) = "+ Function.getDerivativeFunction2(sa, n));
        System.out.println("f(b) = "+ Function.getFunction(sb, n));
        System.out.println("f``(b) = "+ Function.getDerivativeFunction2(sb, n));
        if (Function.getFunction(sa, n) * Function.getDerivativeFunction2(sa, n) > 0) {
            System.out.println("x0 = "+ sa);
            a.add(sa);
        } else  {
            System.out.println("x0 = "+ sb);
            a.add(sb);
        }

        int check = 200;

        do {
            fa.add(Function.getFunction(a.get(a.size() - 1), n));
            fa1.add(Function.getDerivativeFunction1(a.get(a.size() - 1), n));
            b.add(a.get(a.size() - 1) - fa.get(fa.size() - 1) / fa1.get(fa1.size() - 1));
            ab.add(Math.abs(a.get(a.size() - 1) - b.get(b.size() - 1)));
            a.add(b.get(b.size() - 1));
        } while (ab.get(ab.size() - 1) > eps && check-- > 0);

        fa.add(Function.getFunction(a.get(a.size() - 1), n));
        fa1.add(Function.getDerivativeFunction1(a.get(a.size() - 1), n));
        b.add(a.get(a.size() - 1) - fa.get(fa.size() - 1) / fa1.get(fa1.size() - 1));
        ab.add(Math.abs(a.get(a.size() - 1) - b.get(b.size() - 1)));

        if (check <= 0) {
            System.out.println("Метод не сходится");
            return;
        }
        if (save == 1) {
            outputConsole(n);
        } else {
            outputFile(n);
        }
    }

    public void outputConsole(int n) {
        System.out.println("+------------------------------------------------" +
                "-----------------------------------------------+\n");
        System.out.printf("|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|\n",
                "№", " xk", " f(xk)", " f`(xk)", " xk+1", " |xk+1 - xk| ");
        System.out.println("+---------------+---------------+---------------+" +
                "---------------+---------------+---------------+\n");

        for (int i = 0; i < a.size(); i++) {
            System.out.printf("|%-15d|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|\n",
                    i, a.get(i), fa.get(i), fa1.get(i), b.get(i), ab.get(i));
            System.out.println("+---------------+---------------+---------------+" +
                    "---------------+---------------+---------------+\n");
        }
        System.out.println("x = " + b.get(b.size() - 1) + " f(x) = " + Function.getFunction(b.get(b.size() - 1), n) + " n = " + a.size());
    }

    public void outputFile(int n) {
        try {
            FileWriter fileWriter = new FileWriter("src/main/resources/method3-" + n + ".txt");
            fileWriter.write("+------------------------------------------------" +
                    "-----------------------------------------------+");
            fileWriter.write(String.format("|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|\n",
                    "№", " xk", " f(xk)", " f`(xk)", " xk+1", " |xk+1 - xk| "));
            fileWriter.write("+---------------+---------------+---------------+" +
                    "---------------+---------------+---------------+");
            for (int i = 0; i < fa.size(); i++) {
                fileWriter.write(String.format("|%-15d|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|\n",
                        i, a.get(i), fa.get(i), fa1.get(i), b.get(i), ab.get(i)));
                fileWriter.write("+---------------+---------------+---------------+" +
                        "---------------+---------------+---------------+");
            }
            System.out.println("x = " + b.get(b.size() - 1) + " f(x) = " + Function.getFunction(b.get(b.size() - 1), n) + " n = " + a.size());
        } catch (IOException e) {
            System.out.println("Не удалось сохранить");
        }
    }
}
