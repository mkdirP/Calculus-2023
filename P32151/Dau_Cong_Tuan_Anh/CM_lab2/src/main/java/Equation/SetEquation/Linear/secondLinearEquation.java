package Equation.SetEquation.Linear;

import Equation.Model.Interface.LinearEquation;

public class secondLinearEquation implements LinearEquation {
    private String equation = "x^3 - x + 4";
    @Override
    public double resultAt(double x) {
        return Math.pow(x, 3) - x + 4;
    }

    @Override
    public double firstDerivative(double x) {
        return 3 * Math.pow(x, 2) - 1;
    }

    @Override
    public double secondDerivative(double x) {
        return 6 * x;
    }

    @Override
    public String getEquation() {
        return this.equation;
    }
}
