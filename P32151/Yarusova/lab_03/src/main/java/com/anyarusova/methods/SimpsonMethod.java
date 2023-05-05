package com.anyarusova.methods;

import com.anyarusova.entities.MethodData;

public class SimpsonMethod implements Method {
    @Override
    public double calculateIntegral(MethodData methodData) {
        double resultA = methodData.getEquation().apply(methodData.getA());
        if (Double.isInfinite(resultA) || Double.isNaN(resultA)) {
            resultA = methodData.getEquation().apply(methodData.getA() + methodData.getEpsilon());
        }
        double resultB = methodData.getEquation().apply(methodData.getB());
        if (Double.isInfinite(resultB) || Double.isNaN(resultB)) {
            resultB = methodData.getEquation().apply(methodData.getB() - methodData.getEpsilon());
        }
        double result =  resultA + resultB;
        double h = (methodData.getB() - methodData.getA()) / methodData.getN();
        for (int i = 1; i < methodData.getN(); i++) {
            double x = methodData.getEquation().apply(methodData.getA() + i * h);
            if (Double.isNaN(x) || Double.isInfinite(x)) {
                x = methodData.getEquation().apply(methodData.getA() + (i + 1) * h - methodData.getEpsilon());
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
