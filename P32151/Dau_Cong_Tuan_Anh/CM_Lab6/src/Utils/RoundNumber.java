package Utils;

public class RoundNumber {
    public static Double roundDouble(Double num) {
        return (double)((int) (num*10000))/10000;
    }
}
