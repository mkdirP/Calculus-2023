package Utils;

import Algorithm.AlgorithmManager;
import Equation.EquationManager;
import Utils.Input.InputSet;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class DataGetter {
    public static final String URL = "src/main/input.txt";
    public static InputSet getData (AlgorithmManager algorithmManager,
                             EquationManager equationManager) throws FileNotFoundException {
        Scanner scanner = new Scanner(System.in);
        Printer.println("Do you want to type data from console(1) or get data from file(2) ?");
        int type = scanner.nextInt();
        int t, a, b, e;
        double c, d;
        if(type == 1) {
            Printer.println("Do you want to solve linear equation(1) or system equation(2) ?");
            t = scanner.nextInt();
            if(t == 1) {
                Printer.printLinearAlgorithmList(algorithmManager.getLinearAlgorithms());
            } else {
                Printer.printSystemAlgorithmList(algorithmManager.getSystemAlgorithms());
            }
            Printer.println("Please choose your algorithm: ");
            a = scanner.nextInt();

            if(t == 1) {
                Printer.printLinearEquationList(equationManager.getLinearEquations());
            } else {
                Printer.printSystemEquationList(equationManager.getSystemEquations());
            }
            Printer.println("Please choose your Equation: ");
            b = scanner.nextInt();
            if(t == 1) {
                Printer.print("Type left point of range: ");
            } else {
                Printer.print("Type first root guessed:  ");
            }
            c = scanner.nextDouble();

            if(t == 1) {
                Printer.print("Type right point of range: ");
            } else {
                Printer.print("Type second root guessed:  ");
            }
            d = scanner.nextDouble();

            Printer.println("Dow you wanna write result to file(2 = yes) ?");
            e = scanner.nextInt();

            return new InputSet(t, a, b, c, d, e);
        } else if(type == 2) {
            Scanner fileScanner = new Scanner(new File(URL));
            String line = fileScanner.nextLine();
            String[] setOfValue = line.split(" ");
            t = Integer.parseInt(setOfValue[0]);
            a = Integer.parseInt(setOfValue[1]);
            b = Integer.parseInt(setOfValue[2]);
            c = Double.parseDouble(setOfValue[3]);
            d = Double.parseDouble(setOfValue[4]);
            e = Integer.parseInt(setOfValue[5]);

            return new InputSet(t, a, b, c, d, e);
        } else {
            Printer.print("Invalid type!");
        }

        return null;
    }
}
