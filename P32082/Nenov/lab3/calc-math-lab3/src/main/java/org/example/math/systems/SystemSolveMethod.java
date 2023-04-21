package org.example.math.systems;

import org.example.math.results.SystemEquationResult;

public abstract class SystemSolveMethod {
    protected final double accuracy;
    protected final MultiArgFunction[] functions;
    public SystemSolveMethod(double accuracy, MultiArgFunction[] system) {
        this.accuracy = accuracy;
        this.functions = system;
    }

    public MultiArgFunction[] getSystem() {
        return functions;
    }

    protected abstract SystemEquationResult[] calculate(double[] initApprox);

    public final SystemEquationResult[] solve(double[] initApprox) {
        return calculate(initApprox);
    }

}
