package method;

import entity.EquationData;
import entity.Matrix;
import entity.MethodData;
import entity.Solution;

public class GaussSeidelMethod {

    public Solution solve(MethodData data) {
        EquationData equationData = data.getEquationData();
        Matrix matrix = equationData.getAMatrix();
        if (matrix.getRows() != matrix.getColumns()) {
            throw new IllegalArgumentException("Matrix must be square");
        }
        int n = matrix.getRows();
        double[] xVector;
        double[] xPrevVector = new double[n];
        double[] errorVector;
        int iterations = 0;

        if (!checkDiagonalDominance(matrix)) {
            if (!tryToMakeDiagonallyDominant(equationData)) {
                throw new IllegalArgumentException("Matrix must be diagonally dominant");
            }
        }

        changeEquation(equationData);

        if (!checkMatrixNorm(equationData.getAMatrix())) {
            throw new IllegalArgumentException("Matrix must have norm less than 1");
        }

        xVector = equationData.getBVector().clone();
        do {
            System.arraycopy(xVector, 0, xPrevVector, 0, n);
            for (int i = 0; i < n; i++) {
                double sum = 0;
                for (int j = 0; j < n; j++) {
                    if (i != j) {
                        sum += equationData.getAMatrix().getMatrix()[i][j] * xVector[j];
                    }
                }
                xVector[i] = equationData.getBVector()[i] + sum;
            }
            errorVector = calculateError(xVector, xPrevVector);
            iterations++;
        } while (!checkError(errorVector, data.getEpsilon()) && iterations < data.getMaxIterations());

        if (iterations == data.getMaxIterations()) {
            throw new IllegalArgumentException("Max iterations reached");
        }

        return new Solution(xVector, errorVector, iterations);
    }

    private boolean checkDiagonalDominance(Matrix matrix) {
        double[][] m = matrix.getMatrix();
        int n = matrix.getRows();
        for (int i = 0; i < n; i++) {
            double sum = 0;
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    sum += Math.abs(m[i][j]);
                }
            }
            if (Math.abs(m[i][i]) < sum) {
                return false;
            }
        }
        return true;
    }

    private boolean tryToMakeDiagonallyDominant(EquationData data) {
        double[][] m = data.getAMatrix().getMatrix();
        int n = data.getAMatrix().getRows();
        double[] b = data.getBVector();
        for (int i = 0; i < n; i++) {
            double sum = 0;
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    sum += Math.abs(m[i][j]);
                }
            }

            if (Math.abs(m[i][i]) < sum) {
                int maxIndex = i;
                for (int j = i + 1; j < n; j++) {
                    double max = m[j][0];
                    int maxIndex2 = 0;
                    for (int k = 1; k < n; k++) {
                        if (Math.abs(m[j][k]) > Math.abs(max)) {
                            max = m[j][k];
                            maxIndex2 = k;
                        }
                    }
                    if (maxIndex2 == i) {
                        maxIndex = j;
                        break;
                    }
                }
                if (maxIndex == i) {
                    return false;
                }
                double[] temp = m[i];
                m[i] = m[maxIndex];
                m[maxIndex] = temp;
                double tempB = b[i];
                b[i] = b[maxIndex];
                b[maxIndex] = tempB;
            }
        }
        data.getAMatrix().setMatrix(m);
        data.setBVector(b);

        return checkDiagonalDominance(data.getAMatrix());
    }

    private void changeEquation(EquationData equationData) {
        Matrix matrix = equationData.getAMatrix();
        double[][] a = matrix.getMatrix();
        double[] b = equationData.getBVector();
        int n = matrix.getRows();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j) {
                    a[i][j] = -a[i][j] / a[i][i];
                }
            }
            b[i] /= a[i][i];
            a[i][i] = 0;
        }
        equationData.getAMatrix().setMatrix(a);
        equationData.setBVector(b);
    }

    private boolean checkMatrixNorm(Matrix matrix) {
        double[][] a = matrix.getMatrix();
        int n = matrix.getRows();
        double norm = 0;
        for (int i = 0; i < n; i++) {
            double sum = 0;
            for (int j = 0; j < n; j++) {
                sum += Math.abs(a[i][j]);
            }
            if (sum > norm) {
                norm = sum;
            }
        }
        return norm < 1;
    }

    private boolean checkError(double[] errorVector, double epsilon) {
        for (double error : errorVector) {
            if (error > epsilon) {
                return false;
            }
        }
        return true;
    }

    private double[] calculateError(double[] x, double[] xPrev) {
        double[] errorVector = new double[x.length];
        for (int i = 0; i < x.length; i++) {
            errorVector[i] = Math.abs(x[i] - xPrev[i]);
        }
        return errorVector;
    }
}
