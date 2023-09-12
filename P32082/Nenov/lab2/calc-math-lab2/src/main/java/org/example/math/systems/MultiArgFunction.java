package org.example.math.systems;

public abstract class MultiArgFunction {
    static final double DEFAULT_STEP = 0.001;
    public abstract double calculate(double... x);

    public double derivative(double[] x, int argIndex) {
        double[] withInc = x.clone();
        withInc[argIndex] += DEFAULT_STEP;
        return (calculate(withInc)-calculate(x)) / DEFAULT_STEP;
    }

}
