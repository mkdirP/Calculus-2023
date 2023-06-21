import static java.lang.Math.pow;

public class AdamsMethod {
    public static double[] adamsMethod(double x0, double y0, double h, double x, int num) {
        int n = (int) ((x - x0) / h);
        double[] y = new double[n + 1];
        double[] xArr = new double[n + 1];
        y[0] = y0;
        xArr[0] = x0;

        if (n < 4) {
            return null;
        }

        for (int i = 0; i < 4; i++) {
            y[i + 1] = RungeKuttaMethod.rungeKuttaMethod(xArr[i], y[i], h, xArr[i] + h, num);
            xArr[i + 1] = xArr[i] + h;
        }

        for (int i = 4; i <= n; i++) {
            double k1 = Function.getFunction(xArr[i - 1], y[i - 1], num) - Function.getFunction(xArr[i - 2], y[i - 2], num);
            double k2 = k1 + Function.getFunction(xArr[i - 3], y[i - 3], num) - Function.getFunction(xArr[i - 2], y[i - 2], num);
            double k3 = k2 + 2 * Function.getFunction(xArr[i - 3], y[i - 3], num) - Function.getFunction(xArr[i - 2], y[i - 2], num) - Function.getFunction(xArr[i - 4], y[i - 4], num);

            y[i] = y[i - 1] + h * Function.getFunction(xArr[i - 1], y[i - 1], num) + (pow(h, 2) / 2) * k1 +
                    (5 * pow(h, 3) / 12) * k2 + (3 * pow(h, 4) / 8) * k3;

            xArr[i] = xArr[i - 1] + h;
        }

        return y;
    }

    public static double[] solve(double x0, double y0, double h, double x, double eps, int num) {
        int n = (int) ((x - x0) / h);
        double[] y = new double[n + 1];
        double[] xArr = new double[n + 1];
        y[0] = y0;
        xArr[0] = x0;

        if (n < 4) {
            return null;
        }

        for (int i = 0; i < 4; i++) {
            y[i + 1] = RungeKuttaMethod.solve(xArr[i], y[i], h, xArr[i] + h, eps, num);
            xArr[i + 1] = xArr[i] + h;
        }

        for (int i = 4; i <= n; i++) {
            y[i] = y[i - 1] + h * (55 * Function.getFunction(xArr[i - 1], y[i - 1], num) - 59 * Function.getFunction(xArr[i - 2], y[i - 2], num) +
                    37 * Function.getFunction(xArr[i - 3], y[i - 3], num) - 9 * Function.getFunction(xArr[i - 4], y[i - 4], num)) / 24;
            xArr[i] = xArr[i - 1] + h;

            double t = Double.MIN_VALUE;
            while (Math.abs(t - y[i]) > eps) {
                t = y[i];
                y[i] = y[i - 1] + h * (9 * Function.getFunction(xArr[i], t, num) + 19 * Function.getFunction(xArr[i - 1], y[i - 1], num) -
                        5 * Function.getFunction(xArr[i - 2], y[i - 2], num) + Function.getFunction(xArr[i - 3], y[i - 3], num)) / 24;
            }
        }

        return y;
    }
}
