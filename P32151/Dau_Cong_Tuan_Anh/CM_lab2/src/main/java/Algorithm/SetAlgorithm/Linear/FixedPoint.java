package Algorithm.SetAlgorithm.Linear;

import Algorithm.Model.Exception.ImplementRangeException;
import Algorithm.Model.Interface.LinearAlgorithm;
import Utils.Result.LinearResult;
import Equation.Model.Interface.LinearEquation;

public class FixedPoint implements LinearAlgorithm {
    private String name = "Fixed Point";
    private double leftPoint;
    private double rightPoint;
    private LinearResult result = new LinearResult();

    private double lambda;

    public FixedPoint() {
    }

    @Override
    public void setRange(double a, double b) {
        this.leftPoint = a;
        this.rightPoint = b;
    }

    @Override
    public void execute(LinearEquation equation)
                    throws ImplementRangeException {
        if(equation.resultAt(leftPoint) * equation.resultAt(rightPoint) >= 0)
            throw new ImplementRangeException();

        lambda = Math.max(Math.abs(equation.firstDerivative(leftPoint)),
                Math.abs(equation.firstDerivative(rightPoint)));

        if(lambda == 0
        || 1 - 1/lambda* equation.firstDerivative(leftPoint) > 1
        || 1 - 1/lambda* equation.firstDerivative(rightPoint) > 1)
                                    throw new ImplementRangeException();

        double x, x_1 = leftPoint, f_x_1;
        do{
            x = x_1;
            x_1 = x - 1/lambda * equation.resultAt(x);
            f_x_1 = equation.resultAt(x_1);

            result.setRoot(x_1);
            result.setError(Math.abs(x_1 - x));
            result.increaseStep();
        } while (Math.abs(x_1 - x) >= ERROR );
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
