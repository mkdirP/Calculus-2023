package Manager;

import IO.InputSet;
import Model.Function.Function;
import Model.Function.firstFunction;
import Model.Function.secondFunction;
import Model.Interpolation.Gauss;
import Model.Interpolation.Lagrange;
import Model.Interpolation.Polynomial;

import java.util.List;

import static Utils.Print.printlnMessage;

public class AlgorithmManager {
    private final List<Polynomial> polynomialList;

    public AlgorithmManager() {
        polynomialList = List.of(new Gauss(),
                new Lagrange());
    }

    public Polynomial getAlgorithmByIndex(Integer ix) {
        return polynomialList.get(ix);
    }

    public Integer getSize() {
        return this.polynomialList.size();
    }

    public void printList() {
        printlnMessage("List of function: ");
        for (Integer i = 0; i < this.getSize(); ++i) {
            printlnMessage("function " + i + 1 + " " + this.getAlgorithmByIndex(i).toString());
        }
    }

    public List<Polynomial> getPolynomialList() {
        return this.polynomialList;
    }
}
