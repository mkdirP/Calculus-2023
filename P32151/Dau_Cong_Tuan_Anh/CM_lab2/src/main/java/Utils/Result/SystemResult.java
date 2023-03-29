package Utils.Result;

import java.util.Arrays;
import java.util.List;

public class SystemResult {
    private double root[] = {0, 0};
    private double error[] = {0, 0};
    private int step;

    public void setRoot(double x, double y) {
        root[0] = x;
        root[1] = y;
    }

    public void setError(double delta_x, double delta_y) {
        error[0]= delta_x;
        error[1] = delta_y;
    }

    public void increaseStep() {
        ++ step;
    }

    public double[] getRoot() {
        return root;
    }

    public double[] getError() {
        return error;
    }

    public int getStep() {
        return step;
    }

    @Override
    public String toString() {
        return "SystemResult{" +
                "root=" + Arrays.toString(root) +
                ", error=" + Arrays.toString(error) +
                ", step=" + step +
                '}';
    }
}
