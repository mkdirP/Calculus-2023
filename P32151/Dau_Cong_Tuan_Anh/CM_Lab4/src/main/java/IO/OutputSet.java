package IO;

import Model.Equation;
import Utils.RoundNumber;

import static Utils.print.*;

public class OutputSet {
    private Double R;
    private Double S;
    private Double delta;
    private Equation Equation;
    public OutputSet( Equation Equation, Double R, Double S, Double delta) {
        this.R = R;
        this.Equation = Equation;
        this.S =S;
        this.delta = delta;
    }

    public Equation getEquation() {
        return this.Equation;
    }

    public void printResult() {
        printlnOutput("Equation: "+ Equation);
        printlnOutput("R^2: " + RoundNumber.roundDouble(R));
        printlnOutput("S: " + RoundNumber.roundDouble(S));
        printlnOutput("Delta: " + RoundNumber.roundDouble(delta));
    }
}
