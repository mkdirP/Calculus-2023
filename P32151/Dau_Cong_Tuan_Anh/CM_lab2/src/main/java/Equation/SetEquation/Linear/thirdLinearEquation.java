package Equation.SetEquation.Linear;

import Equation.Model.Interface.LinearEquation;

public class thirdLinearEquation implements LinearEquation {
    private String equation = "2x + sin(x)";
    @Override
    public double resultAt(double x) {
        return Math.sin(x) + 2 * x;
    }

    @Override
    public double firstDerivative(double x) {
        return 2 + Math.cos(x);
    }

    @Override
    public double secondDerivative(double x) {
        return -Math.sin(x);
    }

    @Override
    public String getEquation() {
        return equation;
    }
}
