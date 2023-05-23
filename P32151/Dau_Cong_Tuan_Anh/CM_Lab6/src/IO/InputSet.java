package IO;

import java.util.Scanner;

import static Utils.Print.*;

public class InputSet {
    private Double y0;
    private Double h;
    private Double a;
    private Double b;
    private Double error;

    public InputSet(){

    }

    public InputSet(Double y0, Double h, Double a, Double b, Double error) {
        this.y0 = y0;
        this.h = h;
        this.a = a;
        this.b = b;
        this.error = error;
    }

    public Double getY0() {
        return y0;
    }

    public Double getH() {
        return h;
    }

    public Double getA() {
        return a;
    }

    public Double getB() {
        return b;
    }

    public Double getError() {
        return error;
    }
    public void setH(Double h) {
        this.h = h;
    }

    public static InputSet getInputByConsole(Scanner scanner) {
        printlnMessage("Please type Y_0: ");
        Double y0 = scanner.nextDouble();
        printlnMessage("Please type h: ");
        Double h = scanner.nextDouble();
        printlnMessage("Please type a: ");
        Double a = scanner.nextDouble();
        printlnMessage("Please type b: ");
        Double b = scanner.nextDouble();
        printlnMessage("Please type error: ");
        Double error = scanner.nextDouble();
        return new InputSet(y0, h, a, b, error);
    }
}
