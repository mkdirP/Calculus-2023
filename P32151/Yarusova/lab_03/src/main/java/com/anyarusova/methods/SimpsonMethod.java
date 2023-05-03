package com.anyarusova.methods;

import com.anyarusova.entities.MethodData;

public class SimpsonMethod implements Method {
    @Override
    public double calculateIntegral(MethodData methodData) {
        double result = methodData.getEquation().apply(methodData.getA()) + methodData.getEquation().apply(methodData.getB());
        double h = (methodData.getB() - methodData.getA()) / methodData.getN();
        for (int i = 1; i < methodData.getN(); i++) {
            double x = methodData.getEquation().apply(methodData.getA() + i * h);
            if (Double.isNaN(x) || Double.isInfinite(x)) {
                throw new IllegalArgumentException("Integral doesn't exist, function is not continuous in " + (methodData.getA() + i * h));
            } else {
                if (i % 2 == 0) {
                    result += 2 * x;
                } else {
                    result += 4 * x;
                }
            }
        }
        return result * h / 3;
    }
}
