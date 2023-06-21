import java.util.ArrayList;

public class Methods {
    public static double lagrange(ArrayList<Point> points, double solve) {
        double ans = 0.0;

        for (int i = 0; i < points.size(); i++) {
            double basis = 1.0;

            for (int j = 0; j < points.size(); j++) {
                if (i != j) {
                    basis *= (solve - points.get(j).getX()) / (points.get(i).getX() - points.get(j).getX());
                }
            }

            ans += points.get(i).getY() * basis;
        }

        return ans;
    }

    public static double[] finiteDifferences(ArrayList<Point> points) {
        int n = points.size();
        double[][] table = new double[n][n];
        for (int i = 0; i < n; i++) {
            table[i][0] = points.get(i).getY();
        }
        for (int j = 1; j < n; j++) {
            for (int i = 0; i < n - j; i++) {
                table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (points.get(i + j).getX() - points.get(i).getX());
            }
        }
        double[] result = new double[n];
        for (int i = 0; i < n; i++) {
            result[i] = table[0][i];
        }
        return result;
    }

    public static double newtonPolynomial(ArrayList<Point> points, double solve) {
        double[] d = finiteDifferences(points);
        double result = d[0];
        double product = 1;
        for (int i = 1; i < points.size(); i++) {
            product *= (solve - points.get(i - 1).getX());
            result += d[i] * product;
        }
        return result;
    }

    public static double stirlingScheme(ArrayList<Point> point, double solve){
        int n = point.size();
        double[][] d = new double[n][n];
        for (int i = 0; i < n; i++) {
            d[i][0] = point.get(i).getY();
        }
        for (int j = 1; j < n; j++) {
            for (int i = j; i < n; i++) {
                d[i][j] = (d[i][j - 1] - d[i - 1][j - 1]) / (point.get(i).getX() - point.get(i - j).getX());
            }
        }
        double f = d[n - 1][n - 1];
        for (int j = n - 2; j >= 0; j--) {
            f = d[j][j] + (solve - point.get(j).getX()) * f;
        }
        return f;
    }

    public static double besselScheme(ArrayList<Point> point, double solve){
        int n = point.size();
        double p = 0.0;
        double t = (n - point.get(0).getX()) / (point.get(1).getX() - point.get(0).getX());

        for (int k = 0; k < n; k++) {
            double sum = 0.0;

            for (int j = 0; j <= k; j++) {
                double prod = 1.0;

                for (int i = 0; i <= k; i++) {
                    if (i != j) {
                        prod *= (t - i) / (j - i);
                    }
                }

                sum += point.get(j).getY() * prod;
            }

            double prod2 = 1.0;

            for (int i = 0; i < n; i++) {
                if (i != k) {
                    prod2 *= (t - i) / (k - i);
                }
            }

            p += sum * prod2;
        }

        return p;
    }


}

