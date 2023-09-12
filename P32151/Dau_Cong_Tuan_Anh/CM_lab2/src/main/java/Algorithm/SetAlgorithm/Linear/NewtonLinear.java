package Algorithm.SetAlgorithm.Linear;

import Algorithm.Model.Exception.ImplementRangeException;
import Algorithm.Model.Interface.LinearAlgorithm;
import Utils.Result.LinearResult;
import Equation.Model.Interface.LinearEquation;

public class NewtonLinear implements LinearAlgorithm {
    private final String name = "Newton(linear)";
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
        if(equation.resultAt(leftPoint) * equation.secondDerivative(leftPoint) <= 0
        && equation.resultAt(rightPoint )* equation.secondDerivative(rightPoint) <= 0)
            throw new ImplementRangeException();

        double x, f_x, f_1_x, x_1 = (equation.secondDerivative(leftPoint)
                * equation.secondDerivative(leftPoint)) > 0 ? leftPoint : rightPoint;

        do {
            x = x_1;
            f_x = equation.resultAt(x);
            f_1_x = equation.firstDerivative(x);
            x_1 = x - f_x / f_1_x;

            result.setRoot(x_1);
            result.setError(Math.abs(x - x_1));
            result.increaseStep();
        } while(Math.abs(x - x_1) >= ERROR);

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
