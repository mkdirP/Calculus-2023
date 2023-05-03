package com.anyarusova;

import com.anyarusova.entities.MethodData;
import com.anyarusova.io.ConsoleReader;
import com.anyarusova.methods.*;

import java.util.function.Function;

public class MainExtra {
    public static void main(String[] args) {
        ConsoleReader reader = new ConsoleReader();
        int n = 4;
        Function<Double, Double> equation = reader.chooseExtraEquation();
        int methodNum = reader.chooseMethod();
        double epsilon = reader.chooseEpsilon();
        double leftBound = reader.chooseLeftBound();
        double rightBound = reader.chooseRightBound();
        if (leftBound > rightBound) {
            System.out.println("Invalid bounds, left bound is greater than right bound");
            System.out.println("Swapping bounds");
            double temp = leftBound;
            leftBound = rightBound;
            rightBound = temp;
        }
        MethodData methodData = new MethodData(equation, leftBound, rightBound, epsilon, n);
        Method method;
        int k = 2;
        switch (methodNum) {
            case 2 -> method = new RightRectangleMethod();
            case 3 -> method = new MiddleRectangleMethod();
            case 4 -> method = new TrapeziumMethod();
            case 5 -> {
                method = new SimpsonMethod();
                k = 4;
            }
            default -> method = new LeftRectangleMethod();
        }
        if (methodData.getA() == methodData.getB()) {
            System.out.println("Integral value: 0");
            System.out.println("Number of intervals: 0");
            return;
        }
        if (Double.isNaN(methodData.getEquation().apply(methodData.getA())) || Double.isInfinite(methodData.getEquation().apply(methodData.getA())) ) {
            System.out.println("Integral doesn't exist, function is not continuous in " + methodData.getA());
            return;
        }
        if (Double.isNaN(methodData.getEquation().apply(methodData.getB())) || Double.isInfinite(methodData.getEquation().apply(methodData.getB())) ) {
            System.out.println("Integral doesn't exist, function is not continuous in " + methodData.getB());
            return;
        }
        double I0, I1;
        try {
            I1 = method.calculateIntegral(methodData);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
            return;
        }
        if (k == 2) {
            k = 3;
        } else {
            k = 15;
        }
        do {
            I0 = I1;
            methodData.setN(methodData.getN() *  2);
            try {
                I1 = method.calculateIntegral(methodData);
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
                return;
            }
        } while (Math.abs(I0 - I1) / k > methodData.getEpsilon());
        System.out.println("Integral value: " + I1);
        System.out.println("Number of intervals: " + methodData.getN());
    }


}
