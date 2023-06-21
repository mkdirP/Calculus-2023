import java.util.LinkedList;

public class RungeKuttaMethod {
    public static double rungeKuttaMethod(double x0, double y0, double h, double xn, int n) {
        double y = y0;

        while (x0 < xn) {
            double k1 = h * Function.getFunction(x0, y, n);
            double k2 = h * Function.getFunction(x0 + h / 2, y + k1 / 2, n);
            double k3 = h * Function.getFunction(x0 + h / 2, y + k2 / 2, n);
            double k4 = h * Function.getFunction(x0 + h, y + k3, n);

            y += (k1 + 2 * k2 + 2 * k3 + k4) / 6;
            x0 += h;
        }

        return y;
    }

    public static double solve(double x0, double y0, double h, double xn, double eps, int num) {
        LinkedList<Double> x = new LinkedList<>();
        LinkedList<Double> y = new LinkedList<>();
        LinkedList<Double> y_runge = new LinkedList<>();

        x.addLast(x0);
        y.addLast(y0);
        y_runge.addLast(y0);


        while (x.getLast() < xn) {
            double k1 = h * Function.getFunction(x.getLast(), y_runge.getLast(), num);
            double k2 = h * Function.getFunction(x.getLast() + h / 2, y_runge.getLast() + k1 / 2, num);
            double k3 = h * Function.getFunction(x.getLast() + h / 2, y_runge.getLast() + k2 / 2, num);
            double k4 = h * Function.getFunction(x.getLast() + h, y_runge.getLast() + k3, num);

            y_runge.addLast(y_runge.getLast() + (k1 + 2 * k2 + 2 * k3 + k4) / 6);

            h /= 2;
            k1 = h * Function.getFunction(x.getLast(), y.getLast(), num);
            k2 = h * Function.getFunction(x.getLast() + h / 2, y.getLast() + k1 / 2, num);
            k3 = h * Function.getFunction(x.getLast() + h / 2, y.getLast() + k2 / 2, num);
            k4 = h * Function.getFunction(x.getLast() + h, y.getLast() + k3, num);

            y.addLast(y.getLast() + (k1 + 2 * k2 + 2 * k3 + k4) / 6);

            h *= 2;
            x.addLast(x.getLast() + h);

            if (h > 1e-4 && Math.abs(y_runge.getLast() - y.getLast()) > eps) {
                h /= 2;
                x.removeLast();
                y.removeLast();
                y_runge.removeLast();
            }
        }

        return y_runge.getLast();
    }
}
