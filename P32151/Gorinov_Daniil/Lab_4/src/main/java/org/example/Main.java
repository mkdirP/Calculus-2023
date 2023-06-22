package org.example;

import org.example.approximation.*;

import java.io.*;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Stream;

public class Main {
    private static BufferedReader reader;
    private static double[][] functionTable;

    public static void main(String[] args) throws IOException {
        Approximator approximator = new Approximator();
        init();
        List<ApproximationResult> results = new ArrayList<>();

        results.add(approximator.linearApproximation(functionTable));
        results.add(approximator.squareApproximation(functionTable));
        results.add(approximator.exponentialApproximation(functionTable));
        results.add(approximator.logarithmicApproximation(functionTable));
        results.add(approximator.powerApproximation(functionTable));
        results.add(approximator.cubicApproximation(functionTable));

        results.forEach(System.out::println);

        results.sort(Comparator.comparingDouble(ApproximationResult::getDeviation));

        for (ApproximationResult res : results) {
            GraphFrame frame = new GraphFrame(res.getType().name());
            frame.graph(functionTable[0][0] - 2, functionTable[functionTable.length - 1][0] + 2, res.getFunction());
        }
    }

    private static void init() throws IOException {
        initInput();
        initOutput();
        initFunction();
    }

    private static void initFunction() throws IOException {
        System.out.println("Введите количество пар (x, y) (не менее 8)");
        int pairs = readIntegerInput(6);
        functionTable = new double[pairs][2];
        initValues(pairs);
    }

    private static void initValues(int pairs) throws IOException {
        int i = 0;
        while (i < pairs) {
            try {
                double[] pair = Stream.of(reader.readLine().split(" ")).mapToDouble(Double::parseDouble).toArray();
                if (pair.length != 2) {
                    System.err.println("Ожидается два числа в строке.");
                    continue;
                }
                functionTable[i] = pair;
                i++;
            } catch (NumberFormatException e) {
                System.err.println("Некорректный ввод, попробуйте снова.");
            }
        }
    }

    private static void initInput() throws IOException {
        reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Введите название файла или 0 для ввода с клавиатуры: ");
        String input = reader.readLine();
        if (!input.equals("0")) {
            while (true) {
                try {
                    reader = new BufferedReader(new FileReader(input));
                    break;
                } catch (FileNotFoundException e) {
                    System.out.println("Файл не был найден или его не получилось создать. Попробуйте снова. ");
                    input = reader.readLine();
                }
            }
        }
    }

    private static void initOutput() throws IOException {
        PrintWriter writer = new PrintWriter(System.out);
        System.out.println("Введите название файла или 0 для вывода в консоль: ");
        String output = reader.readLine();
        if (!output.equals("0")) {
            while (true) {
                try {
                    writer = new PrintWriter(new FileWriter(output));
                    break;
                } catch (FileNotFoundException e) {
                    System.out.println("Файл не был найден. Попробуйте снова.  ");
                }
            }
        }
    }

    private static int readIntegerInput(int min) throws IOException {
        int value;
        while (true) {
            try {
                value = Integer.parseInt(reader.readLine());
                if (value < min) {
                    System.err.println("Значение должно быть >= " + min + ". Попробуйте снова.");
                    continue;
                }
                break;
            } catch (NumberFormatException e) {
                System.err.println("Ожидается целочисленное значение. Пробуйте снова.");
            }
        }
        return value;
    }
}
