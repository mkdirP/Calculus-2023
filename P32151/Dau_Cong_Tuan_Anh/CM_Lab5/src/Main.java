import IO.InputSet;
import Manager.FunctionManager;
import Model.Interpolation.Gauss;
import Model.Interpolation.Lagrange;
import Model.Interpolation.Polynomial;
import Model.Point;
import Utils.RoundNumber;
import Graph.*;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.List;
import java.util.Scanner;

import org.jfree.chart.ui.*;

import static Utils.Print.*;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(System.in);
        printlnMessage("Choose way to import input set:");
        printList(List.of("By console", "By file", "By function"));
        Integer choice = scanner.nextInt();
        InputSet inputSet = new InputSet();


        switch(choice) {
            case 1:
                inputSet = inputSet.getInputFromConsole(new Scanner(System.in));
                break;
            case 2:
                inputSet = inputSet.getInputFromFile(new Scanner(new File("src/test.txt")));
                break;
            case 3:
                inputSet = inputSet.getInputByFunction(new Scanner((System.in)), new FunctionManager());
                break;
            default:
                printlnError("Option is not available!");
                return;
        }
        checkInput(inputSet);

        printlnMessage("Choose algorithm:");
        printList(List.of("Lagrange", "Gauss"));
        Integer algo = scanner.nextInt();
        Polynomial polynomial = null;
        if(algo == 1) {
            polynomial = new Lagrange(inputSet);
        } else if(algo == 2) {
            polynomial = new Gauss(inputSet);
        } else {
            printlnError("Option is not available!");
            return;
        }
        printlnMessage("Finite different table: ");
        printTable(polynomial.getFiniteDiffTable(inputSet), inputSet.getSize());
        printlnMessage("Type point: ");
        Double in = scanner.nextDouble();
        printlnMessage("Result: " + RoundNumber.roundDouble(polynomial.predictValueAt(in)));

        Graph graph = new Graph("Graph", polynomial, inputSet);
        printMessage("2");
        graph.pack();
        printMessage("3");
        UIUtils.centerFrameOnScreen(graph);
        printMessage("2");
        graph.setVisible(true);
    }
    public static void checkInput(InputSet inputSet) {
        List<Point> pointList = inputSet.getPointList();
        int t = 1;
        while(t < pointList.size()) {
            if(pointList.get(t).getX().equals(pointList.get(t - 1).getX())) pointList.remove(t);
            else ++t;
        }

        inputSet.setPointList(pointList);
    }
};

