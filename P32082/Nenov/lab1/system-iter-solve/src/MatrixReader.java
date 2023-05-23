import matrix.Matrix;

import java.io.InputStream;
import java.util.Arrays;
import java.util.Scanner;

public class MatrixReader {
    private final Scanner scanner;
    private final Matrix matrix;

    public MatrixReader(Scanner scanner, int h, int w) {
        this.scanner = scanner;
        matrix = new Matrix(h, w);
        read();
    }

    private void read() {
        for (int i = 0; i < matrix.getHeight(); i++) {
            String line = scanner.nextLine();
            try {
                double[] matrixLine = Arrays
                        .stream(line.replace(",", ".").split(" "))
                        .map(item -> {
                            int ind = item.indexOf(".");
                            if (ind == -1)
                                return item;
                            return item.substring(0, Math.min(item.length(), ind+5));
                        })
                        .mapToDouble(Double::parseDouble)
                        .toArray();
                matrix.setLine(i, matrixLine);
            } catch (Exception e) {
                throw new NumberFormatException(String.format("Parsing error: %s", e.getMessage()));
            }
        }
    }

    public Matrix getResult() {
        return matrix;
    }
}
