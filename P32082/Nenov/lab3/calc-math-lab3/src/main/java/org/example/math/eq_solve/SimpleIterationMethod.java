package org.example.math.eq_solve;

import org.example.math.Function;
import org.example.math.results.EquationResult;

public class SimpleIterationMethod extends EqSolveMethod {
    final double CONV_CHECK_STEP = 0.005;
    private Function phi;
    public SimpleIterationMethod(double accuracy, Function function) {
        super(accuracy, function);
    }

    @Override
    protected boolean convergence(double a, double b) {
        if (a > b) {
            double tmp = b;
            b = a;
            a = tmp;
        }
        double maxDf = 0;
        for (double x = a; x < b; x+=0.01) {
            maxDf = Math.max(maxDf, Math.abs(function.derivative(x)));
        }
        double lambda = -1/maxDf;
        phi = new Function() {
            @Override
            public double calculate(double x) {
                return x + lambda*function.calculate(x);
            }
        };
        return super.convergence(a, b);
    }

    @Override
    public EquationResult calculate(double a, double b) {
        double prX;
        double x = a;
        int iters = 0;
        do {
            prX = x;
            x = phi.calculate(x);
            if (Math.abs(phi.derivative(x)) >= 1)
                return new EquationResult("Метод не сходится!");
            iters++;
        } while (Math.abs(x - prX) > accuracy);
        return new EquationResult(x, iters, function);
    }
}
