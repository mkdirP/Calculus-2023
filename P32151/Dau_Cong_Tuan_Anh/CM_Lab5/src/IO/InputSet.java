package IO;

import Model.Function.Function;
import Manager.FunctionManager;
import Model.Point;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import static Utils.Print.*;

public class InputSet {
    List<Point> pointList = new ArrayList<>();

    public InputSet() {

    }

    public InputSet(List<Point> points) {
        this.pointList = points;
    }

    public InputSet getInputFromConsole(Scanner scanner) {
        printMessage("Please type n: ");
        Integer n = scanner.nextInt();
        List<Point> points = new ArrayList<>();
        for(int i = 0 ;i < n; ++i) {
            printlnMessage("Please type x and y :");
            Double x = scanner.nextDouble();
            Double y = scanner.nextDouble();
            points.add(new Point(x, y));
        }

        return new InputSet(points);
    }

    public InputSet getInputFromFile(Scanner scanner) {
        int n = Integer.parseInt(scanner.nextLine());
        List<Point> points = new ArrayList<>();
        for(int i = 0; i < n; ++i) {
            String t = scanner.nextLine();
            Double x = Double.parseDouble(t.split(" ")[0]);
            Double y = Double.parseDouble(t.split(" ")[1]);
            points.add(new Point(x, y));
        }
        return new InputSet(points);
    }

    public void setPointList(List<Point> pointList) {
        this.pointList = pointList;
    }

    public InputSet getInputByFunction(Scanner scanner, FunctionManager functionManager) {
        printlnMessage("Please type order of function: ");
        Integer order = scanner.nextInt();
        Function function = functionManager.getFunctionByIndex(order);
        printlnMessage("Please type h: ");
        Integer h = scanner.nextInt();
        printlnMessage("Please type a: ");
        Double a = scanner.nextDouble();
        printlnMessage("Please type b: ");
        Double b = scanner.nextDouble();
        List<Point> points = new ArrayList<>();
        for(Double i = a; i < b; i += h) {
            points.add(new Point((double) Math.round(i), (double) Math.round(function.valueAt(i))));
        }
        return new InputSet(points);
    }

    public Integer getSize() {
        return this.pointList.size();
    }

    public List<Point> getPointList() {
        return this.pointList;
    }


}
