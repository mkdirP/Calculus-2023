package com.anyarusova.methods;

import com.anyarusova.entities.MethodData;

public class RightRectangleMethod implements Method {
    @Override
    public double calculateIntegral(MethodData methodData) {
        double result = 0;
        double h = (methodData.getB() - methodData.getA()) / methodData.getN();
        for (int i = 1; i <= methodData.getN(); i++) {
            double x = methodData.getEquation().apply(methodData.getA() + i * h);
            if (Double.isNaN(x) || Double.isInfinite(x)) {
                x = methodData.getEquation().apply(methodData.getA() + (i + 1) * h - methodData.getEpsilon());
            } else {
                result += x;
            }
        }
        return result * h;
    }
}
