import Algorithm.AlgorithmManager;
import Algorithm.Model.Exception.ImplementFirstValuesException;
import Algorithm.Model.Exception.ImplementRangeException;
import Algorithm.Model.Interface.LinearAlgorithm;
import Algorithm.Model.Interface.SystemAlgorithm;
import Equation.EquationManager;
import Equation.Model.Interface.LinearEquation;
import Equation.Model.Interface.SystemEquation;
import Equation.SetEquation.System.secondSystemEquation;
import Graphic.Drawer;
import Utils.DataGetter;
import Utils.Input.InputSet;
import Utils.Printer;

import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class index {
    public static void main(String[] args) throws IOException {
        AlgorithmManager algorithmManager = new AlgorithmManager();
        EquationManager equationManager = new EquationManager();
        Drawer draw = new Drawer("Graph");
        try {
            InputSet inputSet = DataGetter.getData(algorithmManager, equationManager);
            assert inputSet != null;
            if(inputSet.getType() == 1) {
                LinearAlgorithm linearAlgorithm = algorithmManager
                        .getLinearAlgorithmAt(inputSet.getOrderOfAlgorithm());
                LinearEquation linearEquation = equationManager
                        .getLinearEquationAt(inputSet.getOrderOfEquation());
                linearAlgorithm.setRange(inputSet.getA(), inputSet.getB());
                linearAlgorithm.execute(linearEquation);
                Printer.printLinearResult(linearAlgorithm.getResult());
                if(inputSet.getWriteToFile() == 2) {
                    BufferedWriter writer = new BufferedWriter(new FileWriter("src/main/output.txt"));
                    writer.write(linearAlgorithm.getResult().toString());
                    writer.close();
                }
                draw.drawLinearEquation(linearEquation,
                        inputSet.getA(),
                        inputSet.getB(),
                        linearAlgorithm.getResult().getRoot(),
                        0);
            } else {
                SystemAlgorithm systemAlgorithm = algorithmManager
                        .getSystemAlgorithmAt(inputSet.getOrderOfAlgorithm());
                SystemEquation systemEquation = equationManager
                        .getSystemEquationAt(inputSet.getOrderOfEquation());
                systemAlgorithm.ImplementFirstValue(inputSet.getA(), inputSet.getB());
                systemAlgorithm.execute(systemEquation);
                Printer.printSystemResult(systemAlgorithm.getResult());
                if(inputSet.getWriteToFile() == 2) {
                    BufferedWriter writer = new BufferedWriter(new FileWriter("src/main/output.txt"));
                    writer.write(systemAlgorithm.getResult().toString());
                    writer.close();
                }
                draw.drawSystemEquation(systemEquation,
                        systemAlgorithm.getResult().getRoot()[0],
                        systemAlgorithm.getResult().getRoot()[1]);
            }
            draw.pack();
            draw.setVisible(true);
        } catch (FileNotFoundException e) {
            Printer.print("File path is incorrect!");
            System.exit(0);
        } catch (ImplementRangeException e) {
            Printer.print("Range is unexpected!");
            System.exit(0);
        } catch (ImplementFirstValuesException e) {
            Printer.print("Guessed value is unexpected!");
            System.exit(0);
        }
    }
}
