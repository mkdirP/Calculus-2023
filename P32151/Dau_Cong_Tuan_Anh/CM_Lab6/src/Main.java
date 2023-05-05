import IO.InputSet;
import Manager.AlgorithmManager;
import Manager.FunctionManager;
import Model.Algorithm.Algorithm;
import Model.Function.Function;

import java.util.Scanner;

import static Utils.Print.*;
import Graph.Graph;
import org.jfree.chart.ui.UIUtils;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        InputSet inputSet = InputSet.getInputByConsole(scanner);
        AlgorithmManager algorithmManager = new AlgorithmManager();
        FunctionManager functionManager = new FunctionManager();

        algorithmManager.print();
        printlnMessage("Please choose one algorithm: ");
        int al= scanner.nextInt();
        Algorithm algorithm = algorithmManager.getAlgorithmList().get(al - 1);

        functionManager.print();
        printlnMessage("Please choose one function: ");
        int fc= scanner.nextInt();
        Function func = functionManager.getFunctionList().get(fc - 1);

        Double[][] res = algorithm.execute(inputSet, func);

        printTable(res, (int) ((inputSet.getB() - inputSet.getA())/ inputSet.getH()));

        Graph graph = new Graph("Graph", algorithm, inputSet, func);
        graph.pack();
        UIUtils.centerFrameOnScreen(graph);
        graph.setVisible(true);
    }
}