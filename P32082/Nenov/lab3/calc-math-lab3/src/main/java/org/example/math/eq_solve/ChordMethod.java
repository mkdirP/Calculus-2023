package org.example.math.eq_solve;

import org.example.math.Function;
import org.example.math.results.EquationResult;

public class ChordMethod extends EqSolveMethod {

    public ChordMethod(double accuracy, Function function) {
        super(accuracy, function);
    }

    @Override
    public EquationResult calculate(double a, double b) {
        double prX;
        double x = a;
        int iters = 0;
        do {
            prX = x;
            x = (a*function.calculate(b) - b* function.calculate(a)) / (function.calculate(b)- function.calculate(a));
//            System.out.printf("%d) %.3f | %.3f | %.3f | %.3f %.3f | %.3f | %.3f %n", iters+1, a, b, x, function.calculate(a),
//                    function.calculate(b), function.calculate(x), Math.abs(x - prX));
            iters++;
            if (function.calculate(a) * function.calculate(x) < 0)
                a = x;
            else
                b = x;
        } while (Math.abs(x - prX) > accuracy && Math.abs(a-b) > accuracy && Math.abs(function.calculate(x)) > accuracy);
        return new EquationResult(x, iters, function);
    }
}
