package entity;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class MethodData {

    EquationData equationData;
    double epsilon;
    int maxIterations;
}
