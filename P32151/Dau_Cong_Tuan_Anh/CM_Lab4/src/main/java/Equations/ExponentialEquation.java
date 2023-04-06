package Equations;

import Model.Equation;
import Model.Function;
import Utils.RoundNumber;

public class ExponentialEquation implements Equation {
    private Double a;
    private Double b;
    public ExponentialEquation(Double a, Double b) {
        this.a = a;
        this.b = b;
    }

    @Override
    public Double getValue(Double x) {
        return a* Math.pow(Math.E,x*b);
    }

    @Override
    public String toString() {
        return "ExponentialEquation " + RoundNumber.roundDouble(a) + "* x^" +RoundNumber.roundDouble(b);
    }
}
