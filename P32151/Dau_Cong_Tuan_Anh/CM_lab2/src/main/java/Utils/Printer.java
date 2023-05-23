package Utils;

import Algorithm.Model.Interface.LinearAlgorithm;
import Algorithm.Model.Interface.SystemAlgorithm;
import Equation.Model.Interface.LinearEquation;
import Equation.Model.Interface.SystemEquation;
import Utils.Result.LinearResult;
import Utils.Result.SystemResult;

import java.util.List;

public class Printer {
    public static void print(String message) {
        System.out.print(message);
    }
    public static void println(String message) {
        System.out.println(message);
    }
    public static void printLinearEquationList(List<? extends LinearEquation> list) {
        println("List of linear equation: ");
        for (int i = 0; i< list.size(); ++i) {
            println("Equation " + i + " : " + list.get(i).getEquation());
        }
    }

    public static void printSystemEquationList(List<? extends SystemEquation> list) {
        println("List of system equation: ");
        for (int i = 0; i< list.size(); ++i) {
            println("Equations " + i + " : \n" + list.get(i).getSystemEquation());
        }
    }

    public static void printLinearAlgorithmList (List <? extends LinearAlgorithm> list) {
        println("List of linear algorithm: ");
        for (int i = 0; i< list.size(); ++i) {
            println("Algorithm " + i +" : " + list.get(i).getName());
        }
    }

    public static void printSystemAlgorithmList (List <? extends SystemAlgorithm> list) {
        println("List of system algorithm: ");
        for (int i = 0; i< list.size(); ++i) {
            println("Algorithm " + i +" : " + list.get(i).getName());
        }
    }

    public static void printLinearResult(LinearResult linearResult) {
        println("Result of program: ");
        println("Root: " + linearResult.getRoot());
        println("Error: " + linearResult.getError());
        println("Number of step: " + linearResult.getNumOfStep());
    }

    public static void printSystemResult(SystemResult systemResult) {
        println("Result of program: ");
        println("Root: " + systemResult.getRoot()[0] + " " + systemResult.getRoot()[1]);
        println("Error: " + systemResult.getError()[0] + " " + systemResult.getError()[1]);
        println("Number of step: " + systemResult.getStep());
    }

}
