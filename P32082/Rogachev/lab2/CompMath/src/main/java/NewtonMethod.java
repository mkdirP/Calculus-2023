import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class NewtonMethod{

    ArrayList<Double> a = new ArrayList<Double>();
    ArrayList<Double> b = new ArrayList<Double>();

    ArrayList<Double> da = new ArrayList<Double>();
    ArrayList<Double> db = new ArrayList<Double>();
    ArrayList<Double> fa = new ArrayList<Double>();
    ArrayList<Double> fb = new ArrayList<Double>();

    public void solve(double sa, double sb, double eps, int n, int save) {
        int check = 200;
        Pair<Double, Double> x;

        a.add(sa);
        b.add(sb);

        if (n == 1) {
            do {
                x = solve(2 * a.get(a.size() - 1), 2 * b.get(b.size() - 1),
                        4 - Math.pow(a.get(a.size() - 1), 2) - Math.pow(b.get(b.size() - 1), 2),
                        -6 * a.get(a.size() - 1), 1,
                        3 * Math.pow(a.get(a.size() - 1), 2) - b.get(b.size() - 1));
                db.add(x.value());
                da.add(x.key());
                a.add(a.get(a.size() - 1) + da.get(da.size() - 1));
                b.add(b.get(b.size() - 1) + db.get(db.size() - 1));
                fa.add(Math.pow(a.get(a.size() - 1), 2) + Math.pow(b.get(b.size() - 1), 2) - 4);
                fb.add(3 * Math.pow(a.get(a.size() - 1), 2) - b.get(b.size() - 1));
            } while (Math.max(Math.abs(da.get(da.size() - 1)), Math.abs(db.get(db.size() - 1))) > eps && check-- > 0);
        } else {
            do {
                x = solve(2 * a.get(a.size() - 1), 2 * b.get(b.size() - 1),
                        1 - Math.pow(a.get(a.size() - 1), 2) - Math.pow(b.get(b.size() - 1), 2),
                        -1, 1,
                        a.get(a.size() - 1) - b.get(b.size() - 1));
                da.add(x.key());
                db.add(x.value());
                a.add(a.get(a.size() - 1) + da.get(da.size() - 1));
                b.add(b.get(b.size() - 1) + db.get(db.size() - 1));
                fa.add(Math.pow(a.get(a.size() - 1), 2) + Math.pow(b.get(b.size() - 1), 2) - 1);
                fb.add(a.get(a.size() - 1) - b.get(b.size() - 1));
            } while (Math.max(Math.abs(da.get(da.size() - 1)), Math.abs(db.get(db.size() - 1))) > eps && check-- > 0);
        }

        if (check <= 0) {
            System.out.println("Алгоритм не сходится");
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
                "--------------------------------------------------------------+");
        System.out.printf("|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|\n",
                "№", "x", "y", "dx", "dy", "f(x+dx,y+dy)", "g(x+dx,y+dy)");
        System.out.println("+---------------+---------------+---------------+" +
                "---------------+---------------+---------------+---------------+");

        for (int i = 0; i < fa.size(); i++) {
            System.out.printf("|%-15d|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|\n",
                    i, a.get(i), b.get(i), da.get(i), db.get(i), fa.get(i), fb.get(i));
            System.out.println("|---------------+---------------+---------------+" +
                    "---------------+---------------+---------------+---------------|");
        }
        System.out.println("x = " + a.get(a.size() - 1) + " y = " + b.get(b.size() - 1) +
                "\nf(x) = " + fa.get(fa.size() - 1) + " g(x) = " + fb.get(fa.size() - 1) + "\nn = " + a.size());
    }

    public void printFile(int n) {
        try {
            FileWriter fileWriter = new FileWriter("src/main/resources/method6-" + n + ".txt");
            fileWriter.write("+-------------------------------------------------" +
                    "--------------------------------------------------------------+\n");
            fileWriter.write(String.format("|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|%-15s|\n",
                    "№", "x", "y", "dx", "dy", "f(x+dx,y+dy)", "g(x+dx,y+dy)"));
            fileWriter.write("+---------------+---------------+---------------+" +
                    "---------------+---------------+---------------+---------------+\n");
            for (int i = 0; i < fa.size(); i++) {
                fileWriter.write(String.format("|%-15d|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|%-15.5f|\n",
                        i, a.get(i), b.get(i), da.get(i), db.get(i), fa.get(i), fb.get(i)));
                fileWriter.write("|---------------+---------------+---------------+" +
                        "---------------+---------------+---------------+---------------|\n");
            }
        } catch (IOException e) {
            System.out.println("Не удалось сохранить");
        }
    }

    public Pair<Double, Double> solve(double x1, double y1, double a1, double x2, double y2, double a2) {
        double d = x1 * y2 - x2 * y1;

        return new Pair<>((a1 * y2 - a2 * y1) / d, (x1 * a2 - x2 * a1) / d);
    }
}

