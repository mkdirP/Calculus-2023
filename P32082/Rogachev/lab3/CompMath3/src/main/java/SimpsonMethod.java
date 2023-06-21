public class SimpsonMethod {

    public void method5(double sa, double sb, double eps, int num) {
        int n = 4;
        double x, x1 = solve(sa, sb, n, num);

        do {
            x = x1;
            n *= 2;
            x1 = solve(sa, sb, n, num);
        } while (Math.abs(x1 - x) / 15.0 > eps);

        if(Double.isInfinite(x1) || Double.isNaN(x1)){
            System.out.println("Интеграл не существует");
        }

        else {
            System.out.println("I = " + x1 + "\nn = " + n + "\nПогрешность: " + Math.abs(x1 - x) / 15.0);
        }
    }

    public double solve(double sa, double sb, int n, int num) {
        double h = (sb - sa) / n, ans = Function.getFunction(sa, num) + Function.getFunction(sb, num);
        boolean flag = true;

        for (double i = sa + h; i < sb; i += h) {
            if (flag) {
                ans += Function.getFunction(i, num) * 4.0;
            } else {
                ans += Function.getFunction(i, num) * 2.0;
            }
            flag = !flag;
        }

        return ans * h / 3.0;
    }
}
