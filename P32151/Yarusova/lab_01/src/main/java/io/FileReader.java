package io;

import entity.EquationData;
import entity.Matrix;
import entity.MethodData;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.Scanner;

public class FileReader implements Reader {

    private final String path;

    public FileReader(String path) {
        this.path = path;
    }


    @Override
    public MethodData read() {
        try (BufferedReader br = new BufferedReader(new java.io.FileReader(path))) {
            Scanner scanner = new Scanner(br);
            int rows = scanner.nextInt();
            int columns = scanner.nextInt();
            double[][] matrix = new double[rows][columns];
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < columns; j++) {
                    matrix[i][j] = scanner.nextDouble();
                }
            }
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
            double epsilon = scanner.nextDouble();
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
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
            return null;
        }
    }
}
