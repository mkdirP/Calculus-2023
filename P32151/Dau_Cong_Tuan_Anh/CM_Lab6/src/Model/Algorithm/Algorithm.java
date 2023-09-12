package Model.Algorithm;

import IO.InputSet;
import Model.Function.Function;
import Model.Point;

import java.util.List;

public interface Algorithm {
    public Double[][] execute(InputSet inputSet, Function func);
}
