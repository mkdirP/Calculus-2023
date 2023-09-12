import IO.InputSet;
import IO.Result;
import Manager.EquationManager;
import Manager.MethodManager;
import Model.Equation;
import Model.Method;

import java.util.Scanner;

public class index {
    public static void main(String[] args) {
        EquationManager equationManager = new EquationManager();
        MethodManager methodManager = new MethodManager();
        Scanner scanner = new Scanner(System.in);
        InputSet inputSet = new InputSet().getInputSet(equationManager, methodManager, scanner);
        Equation equation = equationManager.getEquation(inputSet.equation);
        Method method = methodManager.getMethod(inputSet.method);
        Result result = method.execute(equation, inputSet.left, inputSet.right, inputSet.n, inputSet.accuracy);
        result.printResult();
    }
}
