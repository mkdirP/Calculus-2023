package org.example.math.systems;

import org.example.math.results.SystemEquationResult;

public class NewtonMethodForSystems extends SystemSolveMethod{

    public NewtonMethodForSystems(double accuracy, MultiArgFunction[] function) {
        super(accuracy, function);
    }

    @Override
    protected SystemEquationResult[] calculate(double[] initApprox) {
        double[] pastResult = initApprox.clone();
        double[] xData = new double[functions.length];
        double[] diffs = new double[functions.length];
        boolean run = true;
        int iterations = 0;
        while (run) {
            for (int i = 0; i < functions.length; i++) {
                xData[i] = functions[i].calculate(pastResult);
                double derSum = 0;
                for (int j = 0; j < functions.length; j++) {
                    derSum += Math.abs(functions[i].derivative(pastResult, j));
                }
                if (derSum >= 1)
                    return new SystemEquationResult[] { new SystemEquationResult("Метод не сходится!") };
            }

            run = false;
            for (int i = 0; i < functions.length; i++) {
                diffs[i] = Math.abs(xData[i]-pastResult[i]);
                if (diffs[i] > accuracy)
                    run = true;
            }
            iterations++;
            pastResult = xData.clone();
        }
        SystemEquationResult[] results = new SystemEquationResult[xData.length];
        for (int i = 0; i < results.length; i++) {
            results[i] = new SystemEquationResult(xData[i], iterations,  diffs[i]);
        }
        return results;
    }
}
