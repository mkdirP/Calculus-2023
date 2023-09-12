package Utils;

import IO.OutputSet;
import Model.Function;

import java.util.List;

public class print {
    public static void printlnOutput(String message) {
        System.out.println(message);
    }

    public static void printMessage(String message) {
        System.out.print(message);
    }

    public static void printError(String error) {
        System.err.print(error);
    }

    public static void printlnError(String error) {
        System.err.println(error);
    }

    public static void printTable(String name, List<Function> objectList) {
        printlnOutput("Table " + name + ": ");
        for(Object obj : objectList) {
            printlnOutput(obj.toString());
        }
    }

    public  static void printListOutput(String name, List<OutputSet> outputSets) {
        printlnOutput("Table " + name + ": ");
        for(OutputSet obj : outputSets) {
            obj.printResult();
        }
    }
}
