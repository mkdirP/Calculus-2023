import matrix.Matrix;
import matrix.QuadMatrix;

import java.util.Arrays;

public class SimpleIterationMethod {
    private Matrix b;
    private QuadMatrix a;
    private final double precision;
    private double[] resultErrors;
    private int iterationsCount;
    private double[] results;
    public SimpleIterationMethod(QuadMatrix coefficients, Matrix numbers, double precision) {
        this.a = coefficients;
        this.b = numbers;
        this.precision = precision;
    }

    public double[] getResultErrors() {
        return resultErrors;
    }

    /*
    * Returns True if dominance found / False, if not.
    * If dominance has found, matrix saves into object variable.
    * */
    private boolean permutations(QuadMatrix coeffs, Matrix numbs, int ind) {
        // if branch ended
        if (ind == coeffs.size() - 1) {
            boolean result = checkDiagDominance(coeffs);
            if (result) {
                a = coeffs;
                b = numbs;
            }
            return result;
        }
        // else
        for (int i = ind; i < coeffs.size(); i++)
        {
            coeffs.replaceLines(i, ind);
            numbs.replaceLines(i, ind);
            if (permutations(coeffs, numbs, ind + 1))
                return true;
            coeffs.replaceLines(i, ind);
            numbs.replaceLines(i, ind);
        }
        return false;
    }

    public boolean diagonalDominance() {
        return permutations(a.clone(), b.clone(), 0);
    }

    private static boolean checkDiagDominance(QuadMatrix matrix) {
        boolean success = true;
        boolean anyStrict = false;

        for (int i = 0; i < matrix.size(); i++) {
            double sum = matrix.sumModules(i) - matrix.get(i, i);
            double value = Math.abs(matrix.get(i, i));
            if (value < sum) {
                success = false;
                break;
            }
            anyStrict = anyStrict || value > sum;
        }
        return success && anyStrict;
    }

    private double[] computeIteration(double[] results) {
        double[] newResult = new double[results.length];

        for (int i = 0; i < a.size(); i++) {
            double temp = 0;
            for (int j = 0; j < a.size(); j++) {
                if (j == i)
                    continue;
                temp += (a.get(i, j) / a.get(i ,i)) * results[j];
            }
            newResult[i] = b.get(i, 0) - temp;
        }
        return newResult;
    }

    public boolean compute() {
        if (!diagonalDominance())
            return false;
        b.divide(a.get(0, 0));
        iterationsCount = 0;

        results = b.asPlainArray();
        double error = Double.MAX_VALUE;
        double[] diff = null;
        while (error > precision) {
            diff = results.clone();
            results = computeIteration(results);
            for (int i = 0; i < results.length; i++) {
                diff[i] = Math.abs(results[i] - diff[i]);
            }
            error = Arrays.stream(diff).max().orElseThrow();
            iterationsCount++;
        }
        resultErrors = diff;
        return true;
    }

    public double[] getResult() {
        return results;
    }

    public int getIterationsCount() {
        return iterationsCount;
    }

}
