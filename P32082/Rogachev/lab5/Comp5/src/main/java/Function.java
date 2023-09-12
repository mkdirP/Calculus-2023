import static java.lang.Math.sin;
public class Function {
    public static double getFunction(double x, int num) {
        switch (num) {
            case 0 -> {
                return sin(x);
            }
            case 1 -> {
                return x * x + 5 * x + 3;
            }
            case 2 -> {
                return x;
            }
        }
        return 0;
    }
}
