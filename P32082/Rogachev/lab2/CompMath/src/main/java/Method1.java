import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Method1 implements Method{
    ArrayList<Double> a = new ArrayList<Double>();
    ArrayList<Double> b = new ArrayList<Double>();
    ArrayList<Double> x = new ArrayList<Double>();
    ArrayList<Double> fa = new ArrayList<Double>();
    ArrayList<Double> fb = new ArrayList<Double>();
    ArrayList<Double> fx = new ArrayList<Double>();
    ArrayList<Double> ab = new ArrayList<Double>();

    public void solve(double sa, double sb, double eps, int n, int save) {
        int check = 200;

        a.add(sa);
        b.add(sb);
        ab.add(Math.abs(a.get(a.size() - 1) - b.get(b.size() - 1)));
        x.add((a.get(a.size() - 1) + b.get(b.size() - 1)) / 2);
        fa.add(Function.getFunction(a.get(a.size() - 1), n));
        fb.add(Function.getFunction(b.get(b.size() - 1), n));
        fx.add(Function.getFunction(x.get(x.size() - 1), n));

        while ((ab.get(ab.size() - 1) > eps || fx.get(fx.size() - 1) > eps)  && check-- > 0) {

            if (fa.get(fa.size() - 1) * fx.get(fx.size() - 1) > 0) {
                a.add(x.get(x.size() - 1));
                b.add(b.get(b.size() - 1));
            } else {
                b.add(x.get(x.size() - 1));
                a.add(a.get(a.size() - 1));
            }
            ab.add(Math.abs(a.get(a.size() - 1) - b.get(b.size() - 1)));
            x.add((a.get(a.size() - 1) + b.get(b.size() - 1)) / 2);
            fa.add(Function.getFunction(a.get(a.size() - 1), n));
            fb.add(Function.getFunction(b.get(b.size() - 1), n));
            fx.add(Function.getFunction(x.get(x.size() - 1), n));
        }

        if (check <= 0) {
            System.out.println("Метод не сходится");
            return;
        }

        if (save == 1) {
            printConsole();
        } else {
            printFile(n);
        }
    }

    public void printConsole() {
        System.out.println("+-------------------------------------------------" +
                "------------------------------------------------------------------------------+");
        System.out.printf("|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|\n",
                "№", "a", "b", "x", "F(a)", "F(b)", "F(x)", " |a - b| ");
        System.out.println("+---------------+---------------+---------------+" +
                "---------------+---------------+---------------+---------------+---------------+");

        for (int i = 0; i < a.size(); i++) {
            System.out.printf("|%-15d|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|\n",
                    i, a.get(i), b.get(i), x.get(i), fa.get(i), fb.get(i), fx.get(i), ab.get(i));
            System.out.println("|---------------+---------------+---------------+" +
                    "---------------+---------------+---------------+---------------+---------------|");
        }
        System.out.println("x = " + x.get(x.size() - 1) + " f(x) = " + fx.get(fx.size() - 1) + " n = " + a.size());
    }

    public void printFile(int n) {
        try {
            FileWriter fileWriter = new FileWriter("src/main/resources/method1-" + n + ".txt", false);
            fileWriter.write("+-------------------------------------------------" +
                    "------------------------------------------------------------------------------+\n");
            fileWriter.write(String.format("|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|\n",
                    "№", "a", "b", "x", "F(a)", "F(b)", "F(x)", "|a - b|"));
            fileWriter.write("+---------------+---------------+---------------+" +
                    "---------------+---------------+---------------+---------------+---------------+\n");
            for (int i = 0; i < fa.size(); i++) {
                fileWriter.write(String.format("|%-15d|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|\n",
                        i, a.get(i), b.get(i), x.get(i), fa.get(i), fb.get(i), fx.get(i), ab.get(i)));
                fileWriter.write("|---------------+---------------+---------------+" +
                        "---------------+---------------+---------------+---------------+---------------|\n");
            }
            fileWriter.flush();
            fileWriter.close();
        } catch (IOException e) {
            System.out.println("Не удалось сохранить");
        }
    }
}
