package IO;

import Manager.EquationManager;
import Manager.MethodManager;
import Model.Equation;

import java.util.Scanner;

public class InputSet {
    public Integer equation ;
    public Integer method;

    public Double left;
    public Double right;
    public Integer n;
    public Double accuracy;

    public InputSet(Integer equation,
                    Integer method,
                    Double left,
                    Double right,
                    Integer n,
                    Double accuracy) {
        this.equation = equation;
        this.method = method;
        this.left = left;
        this.right = right;
        this.n = n;
        this. accuracy = accuracy;
    }

    public InputSet(){

    };

    public InputSet getInputSet(EquationManager equationManager, MethodManager methodManager, Scanner scanner) {
        equationManager.printList();
        System.out.println("Please choose one equation:");
        int equation = scanner.nextInt();
        methodManager.printList();
        System.out.println("Please choose one method: ");
        int method = scanner.nextInt();
        System.out.println("Please type left border");
        Double left = scanner.nextDouble();
        System.out.println("Please type right border:");
        Double right = scanner.nextDouble();
        System.out.println("Please type n: ");
        Integer n = scanner.nextInt();
        System.out.println("Please type accuracy: ");
        Double accuracy = scanner.nextDouble();
        return new InputSet(equation, method, left,right, n , accuracy);
    }

    @Override
    public String toString() {
        return "InputSet{" +
                "equation=" + equation +
                ", method=" + method +
                ", left=" + left +
                ", right=" + right +
                ", n=" + n +
                ", accuracy=" + accuracy +
                '}';
    }
}
