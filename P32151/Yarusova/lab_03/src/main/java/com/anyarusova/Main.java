package com.anyarusova;

import com.anyarusova.entities.MethodData;
import com.anyarusova.io.ConsoleReader;
import com.anyarusova.methods.*;

import java.util.function.Function;

public class Main {
    public static void main(String[] args) {
        ConsoleReader reader = new ConsoleReader();
        int n = 4;
        Function<Double, Double> equation = reader.chooseEquation();
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
        double I0, I1 = method.calculateIntegral(methodData);
        if (k == 2) {
            k = 3;
        } else {
            k = 15;
        }
        do {
            I0 = I1;
            methodData.setN(methodData.getN() *  2);
            I1 = method.calculateIntegral(methodData);
        } while (Math.abs(I0 - I1) / k > methodData.getEpsilon());
        System.out.println("Integral value: " + I1);
        System.out.println("Number of intervals: " + methodData.getN());
    }
}