package Model;

public class Point {
    private Double x;
    private Double y;
    private Double f_x;
    private Double error;

    public Point(Double x,
                 Double y,
                 Double f_x,
                 Double error) {
        this.x = x;
        this.y = y;
        this.f_x = f_x;
        this.error = error;
    }

    public Point(Double x,
                 Double y) {
        this.x = x;
        this.y = y;
    }

    public void setX(Double x) {
        this.x = x;
    }

    public void setY(Double y) {
        this.y = y;
    }

    public void setF_x(Double f_x) {
        this.f_x = f_x;
    }

    public void setError() {
        this.error = this.f_x - this.y;
    }

    public Double getX() {
        return x;
    }

    public Double getY() {
        return y;
    }

    public Double getF_x() {
        return f_x;
    }

    public Double getError() {
        return error;
    }
}
