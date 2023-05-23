package Model.Function;

public class ThirdFunction implements Function{
    private String func = "2y*sin(x)";
    private Double C;
    @Override
    public Double ValueAt(Double x, Double y) {
        return 2 * y * Math.sin(x);
    }

    @Override
    public Double yAt(Double x) {
        return C*Math.pow(Math.E, -2*Math.cos(x));
    }

    @Override
    public void ResolveC(Double x, Double y) {
        C = y / (Math.pow(Math.E, -2 * Math.cos(x)));
    }

    @Override
    public String toString() {
        return func;
    }
}
