package Utils.Result;

public class LinearResult {
    private double root;
    private double error;
    private int numOfStep;
    public LinearResult() {
        root = 0;
        error = 0;
        numOfStep = 0;
    }

    public LinearResult(double root,
                        double error) {
        this.root = root;
        this.error = error;
    }

    public void increaseStep() {
        ++this.numOfStep;
    }

    public void setRoot(double newRoot) {
        this.root = newRoot;
    }

    public void setError(double newError) {
        this.error = newError;
    }

    public void resetStep() {
        this.numOfStep = 0;
    }

    public double getRoot() {
        return root;
    }

    public double getError() {
        return error;
    }

    public int getNumOfStep() {
        return numOfStep;
    }

    @Override
    public String toString() {
        return "LinearResult{" +
                "root=" + root +
                ", error=" + error +
                ", numOfStep=" + numOfStep +
                '}';
    }
}
