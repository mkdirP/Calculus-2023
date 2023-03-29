package Algorithm.SetAlgorithm.Linear;

import Algorithm.Model.Interface.LinearAlgorithm;
import Algorithm.Model.Exception.ImplementRangeException;
import Utils.Result.LinearResult;
import Equation.Model.Interface.LinearEquation;

public class Secant implements LinearAlgorithm {
    private final String name = "Secant";
    private double leftPoint;
    private double rightPoint;

    private LinearResult result = new LinearResult();

    @Override
    public void setRange(double a, double b) {
        this.leftPoint = a;
        this.rightPoint = b;
    }

    @Override
    public void execute(LinearEquation equation)
                        throws ImplementRangeException {
        // check if implement range is valid
        if(equation.resultAt(leftPoint) * equation.resultAt(rightPoint) > 0)
            throw new ImplementRangeException();

        double x, f_x;
        do {
            x = leftPoint // implement result
                    - (rightPoint - leftPoint)
                    / (equation.resultAt(rightPoint) - equation.resultAt(leftPoint))
                    * equation.resultAt(leftPoint);

            f_x = equation.resultAt(x);

            // save result of current step
            result.setRoot(x);
            result.setError(Math.abs(f_x));
            result.increaseStep();

            // change range for next step
            if(equation.resultAt(leftPoint)* equation.resultAt(x) < 0) {
                setRange(leftPoint, x);
            } else {
                setRange(x, rightPoint);
            }
        } while(Math.abs(f_x) >= ERROR);
    }

    @Override
    public LinearResult getResult() {
        return this.result;
    }

    @Override
    public String getName() {
        return this.name;
    }
}
