package org.example.math;

import org.example.math.results.EquationResult;

public class SecantMethod extends NewtonMethod{
    public SecantMethod(double accuracy, Function function) {
        super(accuracy, function);
    }

    @Override
    public EquationResult calculate(double a, double b) {
        double prX, x;
        if (function.calculate(a)*function.secondDerivative(a) > 0) {
            prX = a;
            x = b;
        }
        else {
            prX = b;
            x = a;
        }
        int iters = 0;
        do {
            double tmp = x;
            x = x - (x-prX)/(function.calculate(x)-function.calculate(prX)) * function.calculate(x);
            prX = tmp;
            iters++;
        } while (Math.abs(x-prX) > accuracy && Math.abs(function.calculate(x)) > accuracy);
        return new EquationResult(x, iters, function);
    }
}
