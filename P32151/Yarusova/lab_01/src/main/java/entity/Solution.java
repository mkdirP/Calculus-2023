package entity;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class Solution {

    double[] xVector;
    double[] errorVector;
    int iterations;

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("x vector:").append(System.lineSeparator());
        for (int i = 0; i < xVector.length; i++) {
            sb.append("x").append(i + 1).append(" = ").append(xVector[i]).append(System.lineSeparator());
        }
        sb.append("error vector:").append(System.lineSeparator());
        for (int i = 0; i < errorVector.length; i++) {
            sb.append("e").append(i + 1).append(" = ").append(errorVector[i]).append(System.lineSeparator());
        }
        sb.append("iterations: ").append(iterations);
        return sb.toString();
    }
}
