package Utils;

import java.util.List;

public class Print {
    public static void printMessage(String s) {
        System.out.print(s);
    }

    public static void printlnMessage(String s) {
        System.out.println(s);
    }

    public static void printError(String s) {
        System.err.print(s);
    }

    public static void printlnError(String s) {
        System.err.println(s);
    }

    public static void printList(List<String> lstr) {
        for(Integer i = 0; i < lstr.size(); ++i) {
            printlnMessage(i + 1 + " : " + lstr.get(i));
        }
    }

    public static void printTable(Double[][] x, int n) {
        System.out.format("%-15s%-15s%-15s%-15s%-15s", "x", "y", "fxy","y_exact", "error");
        printlnMessage("");
        for(int i = 0 ;i <n; ++i) {
            for(int j = 0 ;j < n; ++j) {
                System.out.format("%-15s", String.valueOf(RoundNumber.roundDouble(x[i][j])));
            }
            printlnMessage("");
        }
    }
}
