package com.anyarusova.methods;

import com.anyarusova.entities.MethodData;

import java.io.Console;

public class LeftRectangleMethod implements Method {
    @Override
    public double calculateIntegral(MethodData methodData) {
        double result = 0;
        double h = (methodData.getB() - methodData.getA()) / methodData.getN();
        for (int i = 0; i < methodData.getN(); i++) {
            double x = methodData.getEquation().apply(methodData.getA() + i * h);
            if (Double.isNaN(x) || Double.isInfinite(x)) {
                if (i == 0) {
                    result += methodData.getEquation().apply(methodData.getA() + methodData.getEpsilon());
                } else {
                    result += methodData.getEquation().apply(methodData.getA() + (i + 1) * h - methodData.getEpsilon());
                }
            } else {
                result += x;
            }
        }
        return result * h;
    }
}
