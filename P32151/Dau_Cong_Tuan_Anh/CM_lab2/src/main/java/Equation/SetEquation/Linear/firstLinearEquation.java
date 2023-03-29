package Equation.SetEquation.Linear;

import Equation.Model.Interface.LinearEquation;

public class firstLinearEquation implements LinearEquation {
    private final String formula = "x^3 - 3.125x^2 - 3.5x + 2.458";
    @Override
    public double resultAt(double x) {
        return Math.pow(x, 3) - 3.125* Math.pow(x, 2) - 3.5 * x + 2.458;
    }

    @Override
    public double firstDerivative(double x) {
        return 3* Math.pow(x, 2) - 6.25 * x - 3.5;
    }

    @Override
    public double secondDerivative(double x) {
        return 6 * x - 6.25;
    }

    @Override
    public String getEquation() {
        return this.formula;
    }
}
