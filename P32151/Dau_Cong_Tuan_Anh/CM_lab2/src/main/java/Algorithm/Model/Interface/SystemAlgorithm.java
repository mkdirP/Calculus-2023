package Algorithm.Model.Interface;

import Algorithm.Model.Exception.ImplementFirstValuesException;
import Equation.Model.Interface.SystemEquation;
import Utils.Result.SystemResult;

public interface SystemAlgorithm {
    final double ERROR = 0.01;

    public void ImplementFirstValue(double x, double y);

    public void execute(SystemEquation equation) throws ImplementFirstValuesException;

    public SystemResult getResult();

    public String getName();
}
