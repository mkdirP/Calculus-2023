package IO;

public class Result {
    private Double Result;
    private Integer Accuracy;
    private Double Error;
    public Result(Double Result, Integer Accuracy, Double Error) {
        this.Result = Result;
        this.Accuracy = Accuracy;
        this.Error = Error;
    }

    public void setResult(Double result) {
        Result = result;
    }

    public void setAccuracy(Integer accuracy) {
        Accuracy = accuracy;
    }

    public void setError(Double error) {
        Error = error;
    }

    public Integer getAccuracy() {
        return Accuracy;
    }

    public Double getResult() {
        return Result;
    }

    public Double getError() {
        return Error;
    }

    public void printResult() {
        System.out.println(this.toString());
    }

    @Override
    public String toString() {
        return "Result{" +
                "Result = " + Result +
                ", Accuracy = " + Accuracy +
                ", Error = " + Error +
                '}';
    }
}
