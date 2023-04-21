package org.example.math.eq_solve;

import org.example.math.Function;
import org.example.math.results.EquationResult;

public class NewtonMethod extends EqSolveMethod {
    final double CONV_CHECK_STEP = 0.005;
    public NewtonMethod(double accuracy, Function function) {
        super(accuracy, function);
    }

    @Override
    protected boolean convergence(double a, double b) {
        if (a > b) {
            double tmp = b;
            b = a;
            a = tmp;
        }
        double df = function.derivative(a);
        double ddf = function.secondDerivative(a);
//        for (double x = a; x < b; x+=CONV_CHECK_STEP) {
//            if ((df*function.derivative(x) <= 0) || (ddf*function.secondDerivative(x) < 0))
//                return false;
//        }
        return super.convergence(a, b);
    }

    @Override
    public EquationResult calculate(double a, double b) {
        double prX, fxDivDfx;
        double x;
        if (function.calculate(a)*function.secondDerivative(a) > 0)
            x = a;
        else
            x = b;
        int iters = 0;
        do {
            prX = x;
            fxDivDfx = (function.calculate(x)/ function.derivative(x));
            x = x - fxDivDfx;
            iters++;
        } while (Math.abs(x-prX) > accuracy && fxDivDfx > accuracy && Math.abs(function.calculate(x)) > accuracy);
        return new EquationResult(x, iters, function);
    }
}
