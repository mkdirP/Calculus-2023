package Equation;

import Equation.Model.Interface.LinearEquation;
import Equation.Model.Interface.SystemEquation;
import Equation.SetEquation.Linear.firstLinearEquation;
import Equation.SetEquation.Linear.secondLinearEquation;
import Equation.SetEquation.Linear.thirdLinearEquation;
import Equation.SetEquation.System.firstSystemEquation;
import Equation.SetEquation.System.secondSystemEquation;

import java.util.List;

public class EquationManager {
    private final List<LinearEquation> linearEquations;
    private final List<SystemEquation> systemEquations;

    public EquationManager (){
        linearEquations = List.of(
                new firstLinearEquation(),
                new secondLinearEquation(),
                new thirdLinearEquation()
        );
        systemEquations = List.of(
            new firstSystemEquation(),
                new secondSystemEquation()
        );
    }

    public LinearEquation getLinearEquationAt(int order) {
        return linearEquations.get(order);
    }

    public SystemEquation getSystemEquationAt(int order) {
        return systemEquations.get(order);
    }

    public List<LinearEquation> getLinearEquations() {
        return linearEquations;
    }

    public List<SystemEquation> getSystemEquations() {
        return systemEquations;
    }
}
