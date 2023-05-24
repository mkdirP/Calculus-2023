package io;

import entity.EquationData;
import entity.Matrix;
import entity.MethodData;

import java.util.Scanner;

public class ConsoleReader implements Reader {

    @Override
    public MethodData read() {
        System.out.println("Reading from console");
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter number of rows");
        int rows = scanner.nextInt();
        System.out.println("Enter number of columns");
        int columns = scanner.nextInt();
        double[][] matrix = new double[rows][columns];
        System.out.println("Enter matrix of a coefficients");
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix[i][j] = scanner.nextDouble();
            }
        }
        System.out.println("Enter vector of free members");
        double[] freeMembers = new double[rows];
        for (int i = 0; i < rows; i++) {
            freeMembers[i] = scanner.nextDouble();
        }
        EquationData equationData;
        if (EquationData.isEquationValid(matrix, freeMembers, rows, columns)) {
            equationData = new EquationData(new Matrix(matrix), freeMembers);
        } else {
            System.out.println("Invalid equation input");
            return null;
        }
        System.out.println("Enter epsilon");
        double epsilon = scanner.nextDouble();
        System.out.println("Enter max number of iterations");
        int maxIterations = scanner.nextInt();
        scanner.close();
        if (epsilon <= 0) {
            System.out.println("Invalid epsilon input");
            return null;
        }
        if (maxIterations <= 0) {
            System.out.println("Invalid max iterations input");
            return null;
        }
        return new MethodData(equationData, epsilon, maxIterations);
    }
}
