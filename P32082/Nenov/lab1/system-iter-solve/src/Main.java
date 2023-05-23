import matrix.Matrix;
import matrix.QuadMatrix;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Введите \n1) Для ввода с консоли \n2) Для ввода с файла ");
        int mode = scanner.nextInt();
        InputStream inputStream;
        if (mode == 1) {
            System.out.println("Введите n и e через пробел, затем матрицу, начиная со следующей строки");
            inputStream = System.in;
        } else if (mode == 2) {
            System.out.println("Введите название файла.");
            String fileName = scanner.next();
            if (fileName.isEmpty())
                fileName = "matrix";
            try {
                inputStream = new FileInputStream(fileName);
            } catch (FileNotFoundException e) {
                System.out.println("Файл не найден!");
                return;
            }
        } else {
            return;
        }

        scanner = new Scanner(inputStream);
        String[] sizeAndPrecision = scanner.nextLine().replace(",", ".").split(" ");

        SimpleIterationMethod sim;
        try {
            int n = Integer.parseInt(sizeAndPrecision[0]);

            int dotInd = sizeAndPrecision[1].indexOf(".");
            if (dotInd+5 < sizeAndPrecision[1].length()) {
                sizeAndPrecision[1] = sizeAndPrecision[1].substring(0, dotInd + 5);
            }
            double precision = Double.parseDouble(sizeAndPrecision[1]);

            MatrixReader matrixReader =  new MatrixReader(scanner, n, n+1);
            QuadMatrix a = QuadMatrix.of(matrixReader.getResult().slice(0, 0, n, n));
            Matrix b = matrixReader.getResult().slice(n, 0, 1, n);
            sim = new SimpleIterationMethod(a, b, precision);
        } catch (NumberFormatException e) {
            System.out.println("Неверный формат данных!");
            return;
        }

        if (sim.compute()) {
            System.out.print("Результат: ");
            Arrays.stream(sim.getResult()).forEach( item -> System.out.printf("%.4f; ", item));
            System.out.println();

            System.out.print("Вектор погрешностей: ");
            Arrays.stream(sim.getResultErrors()).forEach(item -> System.out.printf("%.4f; ", item));
            System.out.println();

            System.out.printf("Итераций: %d", sim.getIterationsCount());
        }
        else
            System.out.println("Не обнаружено диагонального преобладания!");
    }
}