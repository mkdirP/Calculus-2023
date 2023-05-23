package matrix;

import java.util.Arrays;

public class Matrix implements Cloneable{
    protected final double[][] data;
    private final int width, height;

    public Matrix(int n, int m) {
        data = new double[n][m];
        width = m;
        height = n;
    }

    public Matrix(double[][] array) {
        data = array.clone();
        height = array.length;
        width = array[0].length;
    }

    @Override
    public Matrix clone() {
        return new Matrix(data);
    }

    public void replaceLines(int i, int j) {
        if (i == j)
            return;
        double[] temp = data[i];
        data[i] = data[j];
        data[j] = temp;
    }

    public double get(int i, int j) {
        return data[i][j];
    }

    public void set(int i, int j, double value) {
        data[i][j] = value;
    }

    public void setLine(int i, double[] line) {
        if (line.length != data[0].length)
            throw new IllegalArgumentException("Incompatible line length!");
        data[i] = line.clone();
    }

    public double[] getLine(int i) {
        return data[i];
    }

    public double[][] getAll() {
        return data;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public double[] asPlainArray() {
        double[] array = new double[getHeight()*getWidth()];
        for (int i = 0; i < data.length; i++) {
            for (int j = 0; j < data[0].length; j++) {
                array[i*data[0].length + j] = data[i][j];
            }
        }
        return array;
    }

    public Matrix slice(int upperLeftX, int upperLeftY, int width, int height) {
        double[][] newData = new double[height][width];
        for (int i = upperLeftY; i < upperLeftY + height; i++) {
            System.arraycopy(data[i], upperLeftX, newData[i], 0, newData[0].length);
        }
        return new Matrix(newData);
    }

    public void multiply(double a) {
        for (int i = 0; i < data.length; i++) {
            for (int j = 0; j < data[0].length; j++) {
                data[i][j] *= a;
            }
        }
    }

    public void divide(double a) {
        for (int i = 0; i < data.length; i++) {
            for (int j = 0; j < data[0].length; j++) {
                data[i][j] /= a;
            }
        }
    }

    @Override
    public String toString() {
        StringBuilder stringBuilder = new StringBuilder();
        for (double[] datum : data) {
            stringBuilder.append(Arrays.toString(datum));
            stringBuilder.append('\n');
        }
        stringBuilder.deleteCharAt(stringBuilder.length()-1);
        return stringBuilder.toString();
    }
}
