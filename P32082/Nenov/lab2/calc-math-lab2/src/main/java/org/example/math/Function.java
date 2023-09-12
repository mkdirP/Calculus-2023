package org.example.math;

public abstract class Function {
    static final double DEFAULT_STEP = 0.001;
    public abstract double calculate(double x);

    public double derivative(double x) {
        return (calculate(x+DEFAULT_STEP)-calculate(x)) / DEFAULT_STEP;
    }

    public double secondDerivative(double x) {
        return (calculate(x+DEFAULT_STEP)-2*calculate(x)+calculate(x-DEFAULT_STEP)) / DEFAULT_STEP*DEFAULT_STEP;
    }

}
