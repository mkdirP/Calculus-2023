import java.util.LinkedList;

public class ModifiedEulerMethod {
    public static double modifiedEulerMethod(double x0, double y0, double h, double x, int n) {
        double y = y0;

        while (x0 < x) {
            double k1 = Function.getFunction(x0, y, n);
            double k2 = Function.getFunction(x0 + h, y + h * k1, n);

            y += h * (k1 + k2) / 2;
            x0 += h;
        }

        return y;
    }

    public static double solve(double x0, double y0, double h, double xn, double eps, int num) {
        LinkedList<Double> x = new LinkedList<>();
        LinkedList<Double> y = new LinkedList<>();
        LinkedList<Double> y1 = new LinkedList<>();

        x.addLast(x0);
        y.addLast(y0);
        y1.addLast(y0);


        while (x.getLast() < xn) {
            double k1 = h * Function.getFunction(x.getLast(), y1.getLast(), num);
            double k2 = h * Function.getFunction(x.getLast() + h, y1.getLast() + k1 * h, num);

            y1.addLast(y1.getLast() + (k1 + k2) / 2);

            h /= 2;
            k1 = h * Function.getFunction(x.getLast(), y.getLast(), num);
            k2 = h * Function.getFunction(x.getLast() + h, y.getLast() + k1 * h, num);

            y.addLast(y.getLast() + (k1 + k2) / 2);

            h *= 2;
            x.addLast(x.getLast() + h);

            if (h > 1e-4 && Math.abs(y1.getLast() - y.getLast()) > eps) {
                h /= 2;
                x.removeLast();
                y.removeLast();
                y1.removeLast();
            }
        }

        return y1.getLast();
    }
}
