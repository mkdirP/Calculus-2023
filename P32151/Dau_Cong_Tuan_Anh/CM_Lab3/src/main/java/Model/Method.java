package Model;

import IO.InputSet;
import IO.Result;

public interface Method {
    public Result execute(Equation equation,
                          Double left,
                          Double right,
                          Integer n,
                          Double accuracy);
    public Double error(Equation equation, Double left, Double right,  Integer n);

    public Integer numOfStep(Equation equation,Double left, Double right, Double Accuracy);

    public Double calculate(Equation equation ,
                            Double left,
                            Double right,
                            Integer n);
}
