package Model.Function;

public class firstFunction implements Function{
    private final String function = "sin(x)";
    @Override
    public Double valueAt(Double x) {
        return Math.sin(x);
    }

    @Override
    public String toString() {
        return this.function;
    }
}
