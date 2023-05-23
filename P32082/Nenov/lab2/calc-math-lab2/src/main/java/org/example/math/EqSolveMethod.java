package org.example.math;

import org.example.math.results.EquationResult;

public abstract class EqSolveMethod {
    protected final double accuracy;
    protected final Function function;
    public EqSolveMethod(double accuracy, Function function) {
        this.accuracy = accuracy;
        this.function = function;
    }

    public abstract EquationResult calculate(double a, double b);

    protected boolean convergence(double a, double b) {
        return rootInRange(a, b);
    }

    public final EquationResult solve(double a, double b) {
        if (!convergence(a, b)) {
            return new EquationResult("В данном диапазоне нет корня или метод не сходится!");
        }
        return calculate(a, b);
    }

    public final boolean rootInRange(double a, double b) {
        double fa = function.calculate(a);
        double fb = function.calculate(b);
        return !(fa*fb > 0 || (fa >= 0 && fb >= 0));
    }
}
