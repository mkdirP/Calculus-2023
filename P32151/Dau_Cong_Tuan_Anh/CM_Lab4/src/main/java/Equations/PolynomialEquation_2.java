package Equations;

import Model.Equation;
import Utils.RoundNumber;

public class PolynomialEquation_2 implements Equation {
    private Double a;
    private Double b;
    private Double c;
    public PolynomialEquation_2(Double a, Double b, Double c) {
        this.a  = a;
        this.b = b;
        this.c = c;
    }
    @Override
    public Double getValue(Double x) {
        return a*x*x + b*x + c;
    }

    @Override
    public String toString() {
        return "PolynomialEquation_2: " + RoundNumber.roundDouble(a)+" x^2 + "
                + RoundNumber.roundDouble(b) + " x +" +
                RoundNumber.roundDouble(c);
    }
}
