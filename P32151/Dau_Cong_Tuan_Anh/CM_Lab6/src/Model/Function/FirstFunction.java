package Model.Function;

public class FirstFunction implements Function{
    private String func = "2x";
    private Double C;
    @Override
    public Double ValueAt(Double x, Double y) {
        return 2 * x;
    }

    @Override
    public Double yAt(Double x) {
        return x*x + C;
    }

    @Override
    public void ResolveC(Double x, Double y) {
        C = y - x * x;
    }

    @Override
    public String toString() {
        return func;
    }
}
