public class MatrixActions {
    public static double[][] matrixA;
    public static double[][] matrixB;
    public static double[][] matrixX1;
    public static double[][] matrixX2;
    public static double epsilon;
    public static int M;

    public static void setMatrixAandB(double[][] allMatrix) {
        matrixA = new double[allMatrix.length][allMatrix.length];
        matrixB = new double[allMatrix.length][1];

        for (int i = 0; i < allMatrix.length; i++) {
            for (int j = 0; j < allMatrix.length; j++) {
                matrixA[i][j] = allMatrix[i][j];
            }
            matrixB[i][0] = allMatrix[i][allMatrix.length];
        }
        preReversingLines();
    }

    public static void reverseLines(int i, int j) {
        double[] tmp = matrixA[i];
        matrixA[i] = matrixA[j];
        matrixA[j] = tmp;

        double tmpB = matrixB[i][0];
        matrixB[i][0] = matrixB[j][0];
        matrixB[j][0] = tmpB;
    }

    public static void searchLineWithNorma(int numberX) {
        double currentCoeff;
        double sumOfOther;

        for (int i = numberX; i < matrixA.length; i++) {
            currentCoeff = Math.abs(matrixA[i][numberX]);
            sumOfOther = 0;
            for (int j = 0; j < matrixA.length; j++) {
                sumOfOther += Math.abs(matrixA[i][j]);
            }
            sumOfOther -= currentCoeff;
            if (currentCoeff >= sumOfOther) {
                if (currentCoeff > sumOfOther) {
                    return;
                }
                reverseLines(numberX, i);
                return;
            }
        }
        System.out.println("Не получается переставить строчки так чтобы выполнилось диагональное преобладание");
        System.exit(4);
    }

    public static void preReversingLines() {
        for (int i = 0; i < matrixA.length; i++) {
            searchLineWithNorma(i);
        }
        System.out.println("НЕ ВЫПОЛНЕНО УСЛОВИЕ О ТОМ ЧТОБЫ ПРИ ЗАМЕНАХ СХОДИЛИСЬ ИТЕРАЦИИ");
        System.exit(5);
    }

    public static void initMatrixX1andX2() {
        matrixX2 = new double[matrixA.length][1];
        matrixX1 = new double[matrixA.length][1];
        for (int i = 0; i < matrixA.length; i++) {
            matrixX2[i][0] = matrixB[i][0] / matrixA[i][i];
        }
    }

    public static void iteration() {
        for (int i = 0; i < matrixA.length; i++) {
            matrixX1[i][0] = matrixX2[i][0];
        }

        double sumOther;
        for (int i = 0; i < matrixA.length; i++) {
            sumOther = 0;

            for (int j = 0; j < matrixA.length; j++) {
                if (j < i) {
                    sumOther += matrixA[i][j] * matrixX2[j][0] / matrixA[i][i];
                } else if (j > i) {
                    sumOther += matrixA[i][j] * matrixX1[j][0] / matrixA[i][i];
                }
            }

            matrixX2[i][0] = matrixB[i][0] / matrixA[i][i] - sumOther;
        }
    }

    public static boolean checkAllNewX() {
        for (int i = 0; i < matrixA.length; i++) {
            if (Math.abs(matrixX2[i][0] - matrixX1[i][0]) > epsilon) {
                return false;
            }
        }
        return true;
    }

    public static double[] startComputed() {
        int count = 0;

        while (true) {
            iteration();
            count++;
            if (checkAllNewX() || count >= M) {
                break;
            }
        }

        System.out.println("\nПосле очередной итерации");
        System.out.println("deltaX = " + String.format("%1$8.3f", matrixX2[0][0]));
        System.out.println("deltaY = " + String.format("%1$8.3f", matrixX2[1][0]));

        return new double[]{matrixX2[0][0], matrixX2[1][0]};
    }
}
