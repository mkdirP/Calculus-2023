import tools.MathAndPrintTools;

public class MethodNewTon {
    public static double X_0;
    public static double X_1;
    public static double Y_0;
    public static double Y_1;
    public static double deltaX;
    public static double deltaY;
    public static double[][] matrix_for_lab_1 = new double[2][3];
    public static double precision;

    public static void search_dx_dy() {
        matrix_for_lab_1[0][0] = 2 * X_0;
        matrix_for_lab_1[0][1] = -2;
        matrix_for_lab_1[0][2] = 2 * Y_0 - X_0 * X_0;
        matrix_for_lab_1[1][0] = 3;
        matrix_for_lab_1[1][1] = -2 * Y_0;
        matrix_for_lab_1[1][2] = -3 + Y_0 * Y_0 - 3 * X_0;
    }

    public static double initSolve(double precision, double a, double b) {
        double[] tmp = new double[2];
        X_0 = a;
        Y_0 = b;
        MethodNewTon.precision = precision;

        String header = "Начальные данные:\nX_0 = " + X_0 + "\nY_0 = " + Y_0;
        System.out.println(header);

        int counter = 0;
        while (true) {
            counter++;
            search_dx_dy();
            MatrixActions.setMatrixAandB(matrix_for_lab_1);
            MatrixActions.initMatrixX1andX2();
            tmp = MatrixActions.startComputed();
            deltaX = tmp[0];
            deltaY = tmp[1];
            X_1 = X_0 + deltaX;
            Y_1 = Y_0 + deltaY;
            if (check() || counter > 20) {
                break;
            }
            X_0 = X_1;
            Y_0 = Y_1;
        }

        String finalResult = "\n\nПрошло итераций = " + counter + "\n" +
                "X = " + String.format("%1$8.3f", X_1) + "; \nY = " + String.format("%1$8.3f;", Y_1) + "\n" +
                "Вектор погрешностей:" + "\n" +
                "for X: " + String.format("%1$8.3f", (X_1 - X_0)) + "\n" +
                "for Y: " + String.format("%1$8.3f", (Y_1 - Y_0));

        System.out.println(finalResult);
        MathAndPrintTools.toFileResult.append(finalResult);
        return X_1;
    }

    public static boolean check() {
        return (Math.abs(X_1 - X_0) <= precision || Math.abs(Y_1 - Y_0) <= precision);
    }
}
