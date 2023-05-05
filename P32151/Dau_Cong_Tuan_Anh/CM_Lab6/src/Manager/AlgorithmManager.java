package Manager;

import Model.Algorithm.Adam;
import Model.Algorithm.AdvancedEuler;
import Model.Algorithm.Algorithm;
import Model.Algorithm.Runge_Kutta;

import java.util.List;

import static Utils.Print.printlnMessage;

public class AlgorithmManager {
    private List<Algorithm> algorithmList;

    public AlgorithmManager() {
        algorithmList = List.of(
                new AdvancedEuler(),
                new Runge_Kutta(),
                new Adam());
    }

    public void setAlgorithmList(List<Algorithm> algorithmList) {
        this.algorithmList = algorithmList;
    }

    public List<Algorithm> getAlgorithmList() {
        return algorithmList;
    }

    public void print() {
        printlnMessage("List of Algorithm: ");
        for(int i = 0; i < algorithmList.size(); ++i) {
            printlnMessage(i + 1 + " : " + algorithmList.get(i).toString());
        }
    }
}
