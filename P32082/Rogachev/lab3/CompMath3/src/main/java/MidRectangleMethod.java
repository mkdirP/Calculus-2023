public class MidRectangleMethod {
    public void method2(double sa, double sb, double eps, int num) {
        int n = 4;
        double x, x1 = solve(sa, sb, n, num);

        do {
            x = x1;
            n *= 2;
            x1 = solve(sa, sb, n, num);
        } while (Math.abs(x1 - x) / 3.0 > eps);

        if(Double.isInfinite(x1) || Double.isNaN(x1)){
            System.out.println("Интеграл не существует");
        }
        else {
            System.out.println("I = " + x1 + "\nn = " + n + "\nПогрешность: " + Math.abs(x1 - x) / 3.0);
        }
    }

    public double solve(double sa, double sb, int n, int num) {
        double h = (sb - sa) / n, ans = 0;

        for (double i = sa; i < sb; i += h) {
            ans += Function.getFunction(i + h / 2.0, num) * h;
        }

        return ans;
    }


}
