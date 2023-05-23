package Utils.Input;

public class InputSet {
    private final int type;
    private final int orderOfAlgorithm;
    private final int orderOfEquation;
    private final double a;
    private final double b;
    private final int writeToFile;

    public InputSet (int type,
                     int orderOfAlgorithm,
                     int orderOfEquation,
                     double a,
                     double b, int writeToFile) {
        this.type= type;
        this.orderOfAlgorithm = orderOfAlgorithm;
        this.orderOfEquation = orderOfEquation;
        this. a = a;
        this.b = b;
        this.writeToFile = writeToFile;
    }

    public int getOrderOfAlgorithm() {
        return orderOfAlgorithm;
    }

    public int getOrderOfEquation() {
        return orderOfEquation;
    }

    public double getA() {
        return a;
    }

    public double getB() {
        return b;
    }

    public int getType() {
        return type;
    }

    public int getWriteToFile() {
        return writeToFile;
    }
}
