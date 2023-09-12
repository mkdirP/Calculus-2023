package Algorithm.Model.Interface;

import Algorithm.Model.Exception.ImplementRangeException;
import Utils.Result.LinearResult;
import Equation.Model.Interface.LinearEquation;

public interface LinearAlgorithm {
    final double ERROR = 0.01;

    public void setRange(double a, double b);
    public void execute(LinearEquation equation) throws ImplementRangeException;

    public LinearResult getResult();

    public String getName();
}
