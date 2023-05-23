package Model.Function;

public class secondFunction implements Function{
    private final String function = "2x + 3";
    @Override
    public Double valueAt(Double x) {
        return 2 * x + 3;
    }

    @Override
    public String toString() {
        return this.function;
    }
}
