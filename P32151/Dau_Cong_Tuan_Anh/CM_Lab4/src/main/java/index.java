import Functions.FunctionManager;
import Graph.Graph;
import IO.InputSet;
import IO.OutputSet;
import Utils.print;
import org.jfree.ui.RefineryUtilities;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class index {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(System.in);
        Integer choose;
        print.printlnOutput("Do you want to set input by console(1) or File(2) ?");
        choose = scanner.nextInt();
        InputSet inputSet = new InputSet();
        if(choose == 2) {
            Scanner scanner_file = new Scanner(new File("src/main/java/input.txt"));
            inputSet = InputSet.getInputSetByFile(scanner_file);
        } else if(choose == 1) {
            inputSet = InputSet.getInputSetByConsole(scanner);
        }

        FunctionManager functionManager = new FunctionManager();
        List<OutputSet> outputSets = new ArrayList<>();
        for(int i = 0 ;i < functionManager.getFunctionList().size();++i) {
            outputSets.add(functionManager.getFunctionByIndex(i).execute(inputSet));
        }

        print.printListOutput("Output list", outputSets);

        Graph graph = new Graph("Graph", outputSets, inputSet);
        graph.pack();
        RefineryUtilities.centerFrameOnScreen(graph);
        graph.setVisible(true);
    }
}
