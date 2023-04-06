package Manager;

import Model.Equation;
import Equation.FirstEquation;

import java.util.ArrayList;
import java.util.List;

public class EquationManager {
    private List<Equation> EquationList= new ArrayList<Equation>();
    public EquationManager() {
        this.EquationList = List.of(new FirstEquation());
    }

    public void addEquation(Equation equation) {
        this.EquationList.add(equation);
    }

    public Equation getEquation(Integer index) {
        return this.EquationList.get(index);
    }

    public void printList() {
        System.out.println("List of Equation: ");
        for(int i  = 0 ;i < EquationList.size(); ++i) {
            System.out.println(i + " : " + EquationList.get(i).toString());
        }
    }
}
