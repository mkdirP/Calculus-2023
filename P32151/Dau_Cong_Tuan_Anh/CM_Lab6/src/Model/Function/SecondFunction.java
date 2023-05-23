package Model.Function;

public class SecondFunction implements Function{
    private String func = " y + (1+x)y^2";
    private Double C;
    @Override
    public Double ValueAt(Double x, Double y) {
        return y + (1 + x)*y*y;
    }

    @Override
    public Double yAt(Double x) {
        return 1/(-x + C/(Math.pow(Math.E, x)));
    }

    @Override
    public void ResolveC(Double x, Double y) {
        C = (1/y + x) * Math.pow(Math.E, x);
    }

    @Override
    public String toString() {
        return func;
    }
}
