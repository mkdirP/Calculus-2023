package org.example.math.eq_solve;

import org.example.math.Function;
import org.example.math.results.EquationResult;

public class HalfDivisionMethod extends EqSolveMethod {
    public HalfDivisionMethod(double accuracy, Function function) {
        super(accuracy, function);
    }

    @Override
    public EquationResult calculate(double a, double b) {
        double x;
        int iters = 0;
        do {
            x = (a+b) / 2;
            if (function.calculate(a) * function.calculate(x) >= 0)
                a = x;
            else
                b = x;
            iters++;
        } while (Math.abs(a-b) > accuracy && Math.abs(function.calculate(x)) > accuracy);
        return new EquationResult(x, iters, function);
    }

}
