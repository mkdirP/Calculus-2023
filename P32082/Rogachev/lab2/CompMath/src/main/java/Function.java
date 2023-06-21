import java.util.ArrayList;
// Класс для вычисления значений функций
public class Function {
    public static double getFunction(double x, int n) {
        if (n == 1) {
            return 3 * Math.pow(x, 3) + 1.7 * Math.pow(x, 2) - 15.42 * x + 6.89;
        } else if (n == 2) {
            return Math.pow(x, 3) + 3 * Math.pow(x, 2) + 3 * x + 1;
        } else if (n == 3) {
            return Math.cos(x);
        } else {
            return Math.pow(x, 3) - x + 4;
        }
    }

    public static double getFiFunction(double x, double a, double b, int n) {
        double lambda = -1.0 / getMaxValue(a, b, n);

        if (getDerivativeFunction1(x, n) * getMaxValue(a, b, n) < 0) {
            lambda = -lambda;
        }
        return x + lambda * getFunction(x, n);
    }

    public static double getDerivativeFunction1(double x, int n) {
        if (n == 1) {
            return 3 * 3 * Math.pow(x, 2) + 2 * 1.7 * x - 15.42;
        } else if (n == 2) {
            return 3 * Math.pow(x, 2) + 6 * x + 3;
        } else if (n == 3) {
            return -Math.sin(x);
        } else {
            return 3 * Math.pow(x, 2) - 1;
        }
    }

    public static double getFiDerivativeFunction1(double x, double a, double b, int n) {
        double lambda = -1.0 / getMaxValue(a, b, n);

        if (getDerivativeFunction1(x, n) * getMaxValue(a, b, n) < 0) {
            lambda = -lambda;
        }

        return 1 + lambda * getDerivativeFunction1(x, n);
    }
    public static double getDerivativeFunction2(double x, int n) {
        if (n == 1) {
            return 6 * 3 * x + 2 * 1.7;
        } else if (n == 2) {
            return 6 * x + 6;
        } else if (n == 3) {
            return -Math.cos(x);
        } else {
            return 6 * x;
        }
    }

    public static ArrayList<Double> checkRoots(double a, double b, int n) {
        ArrayList<Double> ans = new ArrayList<Double>();
        ans.add(a);

        double min = Math.min(Math.abs((a - b) / 10000), 0.5);
        for (double i = a; i <= b - min; i += min) {
            double tmp = getFunction(i, n) * getFunction(i + Math.min(Math.abs((a - b) / 10002), 0.5), n);
            if (tmp <= 0.0) {
                ans.add(i);
            }
        }

        ans.add(b);
        return ans;
    }

    private static double getMaxValue(double a, double b, int n) {
        if (Math.abs(getDerivativeFunction1(a, n)) > Math.abs(getDerivativeFunction1(b, n))) {
            return getDerivativeFunction1(a, n);
        } else {
            return getDerivativeFunction1(b, n);
        }
        // return Math.max(Math.abs(getDerivativeFunction1(a, n)), Math.abs(getDerivativeFunction1(b, n)));
    }

    public static double getDerivativeMaxValue(double a, double b, int n) {
        return Math.max(Math.abs(getFiDerivativeFunction1(a, a, b, n)), Math.abs(getFiDerivativeFunction1(b, a, b, n)));
    }
}