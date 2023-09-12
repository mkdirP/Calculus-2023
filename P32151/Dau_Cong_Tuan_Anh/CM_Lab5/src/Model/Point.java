package Model;

import java.util.Comparator;

public class Point implements Comparator {
    private Double x;
    private Double y;

    public Point(Double x, Double y) {
        this.x = x;
        this.y = y;
    }

    public Double getX() {
        return x;
    }

    public Double getY() {
        return y;
    }

    public void setX(Double x) {
        this.x = x;
    }

    public void setY(Double y) {
        this.y = y;
    }

    @Override
    public String toString() {
        return "Point{" +
                "x=" + x +
                ", y=" + y +
                '}';
    }
    @Override
    public int compare(Object o1, Object o2) {
        Point a = (Point) o1;
        Point b = (Point) o2;
        if(a.getX() == b.getX()) return 1;
        return 0;
    }
}
