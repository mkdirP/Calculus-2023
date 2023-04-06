package Equations;

import Model.Equation;
import Utils.RoundNumber;

public class LogarithmicEquation implements Equation {
    private Double a;
    private Double b;

    public LogarithmicEquation(Double a, Double b) {
        this.a = a;
        this.b = b;
    }

    @Override
    public Double getValue(Double x) {
        return a*Math.log(x) + b;
    }

    @Override
    public String toString() {
        return "LogarithmicEquation " + RoundNumber.roundDouble(a) + " * ln(x) + " + RoundNumber.roundDouble(b);
    }
}
