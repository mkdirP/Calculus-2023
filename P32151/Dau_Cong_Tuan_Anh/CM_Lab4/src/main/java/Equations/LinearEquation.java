package Equations;

import Model.Equation;
import Utils.RoundNumber;

public class LinearEquation implements Equation {
    private Double a;
    private Double b;

    public LinearEquation(Double a, Double b) {
        this.a = a;
        this.b = b;
    }
    @Override
    public Double getValue(Double x) {
        return this.a * x + this.b;
    }

    @Override
    public String toString() {
        return "LinearEquation: " + RoundNumber.roundDouble(a) + "x + " + RoundNumber.roundDouble(b);
    }
}
