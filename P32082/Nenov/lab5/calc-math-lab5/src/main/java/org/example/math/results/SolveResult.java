package org.example.math.results;

public class SolveResult {
    private final String error;
    private final double result;
    private final int iterations;

    public SolveResult(double result, int iterations) {
        this.result = result;
        this.iterations = iterations;
        error = null;
    }

    public SolveResult(String error) {
        this.result = 0;
        this.iterations = 0;
        if (error == null)
            error = "";
        this.error = error;
    }
    public boolean getSuccess() { return error == null; }
    public double getResult() { return result; }
    public String getError() { return error; }

    public int getIterations() {
        return iterations;
    }

    @Override
    public String toString() {
        if (getSuccess())
            return String.format("Итераций: %d Корень: %.3f", getIterations(), getResult());
        return "Невозможно решить уравнение: " + getError();
    }
}
