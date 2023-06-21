public class Function {
    public static double getFunction(double x, double y, int n) {
        if (n == 1) {
            return 2 * x - y;
        } else if (n == 2) {
            return y + (1 + x) * y;
        } else {
            return y * x + x * y;
        }
    }
}
