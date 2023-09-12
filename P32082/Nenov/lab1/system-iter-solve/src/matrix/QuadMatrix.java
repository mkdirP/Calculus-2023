package matrix;

public class QuadMatrix extends Matrix{

    public QuadMatrix(int size) {
        super(size, size);
    }

    public QuadMatrix(double[][] data) {
        super(data);
    }

    public int size() {
        return getWidth();
    }

    public double sumModules(int line) {
        double sum = 0;
        for (int i = 0; i < size(); i++) {
            sum += Math.abs(data[line][i]);
        }
        return sum;
    }

    public static QuadMatrix of(Matrix matrix) {
        if (matrix.getHeight() == matrix.getWidth())
            return new QuadMatrix(matrix.data);
        return null;
    }

    @Override
    public QuadMatrix clone() {
        return new QuadMatrix(data);
    }
}
