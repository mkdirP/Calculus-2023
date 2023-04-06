package Equation;

import Model.Equation;

public class FirstEquation implements Equation {
    private String Describe = "2X^3 - 3X^2 + 5X - 9";


    @Override
    public Double valueAt(Double x) {
        return 2*Math.pow(x, 3) - 3 * x * x + 5 * x - 9;
    }

    @Override
    public Double IntegralAt(Double x) {
        return 6*x*x - 6 * x + 5;
    }

    @Override
    public String toString() {
        return this.Describe;
    }
}
