package Utils;

public class RoundNumber {
    public static Double roundDouble(Double num) {
        return (double)((int) (num*1000))/1000;
    }
}
