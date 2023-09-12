package org.example.math.results;

public class SystemEquationResult extends SolveResult {
    private double fault;
    public SystemEquationResult(double result, int iterations, double fault) {
        super(result, iterations);
        this.fault = fault;
    }

    public SystemEquationResult(String error) {
        super(error);
    }

    @Override
    public String toString() {
        if (getSuccess())
            return super.toString() + String.format(" Погрешность: %.3f", fault);
        return super.toString();
    }
}
