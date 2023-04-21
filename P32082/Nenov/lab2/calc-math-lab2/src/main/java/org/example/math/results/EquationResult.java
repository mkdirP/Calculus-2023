package org.example.math.results;

import org.example.math.Function;

public class EquationResult extends SolveResult{
    private Function function;
    public EquationResult(double result, int iterations, Function function) {
        super(result, iterations);
        this.function = function;
    }

    public EquationResult(String error) {
        super(error);
    }

    @Override
    public String toString() {
        if (getSuccess())
            return super.toString() + String.format(" Значение функции в корне %.3f", function.calculate(getResult()));
        return super.toString();
    }
}
