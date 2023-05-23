package Equations;

import Model.Equation;
import Utils.RoundNumber;

public class PowerEquation implements Equation {
    private Double a;
    private Double b;

    public PowerEquation(Double a, Double b) {
        this.a = a;
        this.b = b;
    }
    @Override
    public Double getValue(Double x) {
        return a*Math.pow(x, b);
    }

    @Override
    public String toString() {
        return "PowerEquation " + RoundNumber.roundDouble(a) + " *x^" + RoundNumber.roundDouble(b);
    }
}
