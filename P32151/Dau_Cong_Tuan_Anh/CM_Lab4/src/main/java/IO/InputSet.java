package IO;

import Model.Point;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import static Utils.print.*;

public class InputSet {
    private Integer n;
    private List<Point> pointList;

    public InputSet(Integer n, List<Point> points) {
        this.n = n;
        this.pointList = points;
    }

    public InputSet() {

    }

    public void setN(Integer n) {
        this.n = n;
    }

    public void setPointList(List<Point> pointList) {
        this.pointList = pointList;
    }

    public Integer getN() {
        return n;
    }

    public List<Point> getPointList() {
        return pointList;
    }

    public static InputSet getInputSetByConsole(Scanner scanner) {
        printlnOutput("Please type n: ");
        Integer n = scanner.nextInt();
        List<Point> points = new ArrayList<>();
        for(int i = 0 ;i < n; ++i) {
            printlnOutput("Please type x and y :");
            Double x = scanner.nextDouble();
            Double y = scanner.nextDouble();
            points.add(new Point(x, y));
        }

        return new InputSet(n, points);
    }

    public static InputSet getInputSetByFile(Scanner scanner) {
        int n = Integer.parseInt(scanner.nextLine());
        List<Point> points = new ArrayList<>();
        for(int i = 0; i < n; ++i) {
            String t = scanner.nextLine();
            Double x = Double.parseDouble(t.split(" ")[0]);
            Double y = Double.parseDouble(t.split(" ")[1]);
            points.add(new Point(x, y));
        }
        return new InputSet(n, points);
    }
}
