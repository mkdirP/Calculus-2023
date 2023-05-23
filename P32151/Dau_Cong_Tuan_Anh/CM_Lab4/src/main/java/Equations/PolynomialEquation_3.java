package Equations;

import Model.Equation;
import Utils.RoundNumber;

public class PolynomialEquation_3 implements Equation {
    private Double a;
    private Double b;
    private Double c;
    private Double d;
    public PolynomialEquation_3(Double a, Double b, Double c, Double d) {
        this.a  = a;
        this.b = b;
        this.c = c;
        this.d = d;
    }
    @Override
    public Double getValue(Double x) {
        return a*x*x*x + b*x*x + c*x + d;
    }

    @Override
    public String toString() {
        return "PolynomialEquation_3: " + RoundNumber.roundDouble(a)+" x^3 + " +
                RoundNumber.roundDouble(b) + " x^2 +" +
                RoundNumber.roundDouble(c)+ " x + " +
                RoundNumber.roundDouble(d);
    }
}
