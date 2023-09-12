package Algorithm;

import Algorithm.Model.Interface.LinearAlgorithm;
import Algorithm.Model.Interface.SystemAlgorithm;
import Algorithm.SetAlgorithm.Linear.FixedPoint;
import Algorithm.SetAlgorithm.Linear.NewtonLinear;
import Algorithm.SetAlgorithm.Linear.Secant;
import Algorithm.SetAlgorithm.System.NewtonSystem;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class AlgorithmManager {
    private final List<LinearAlgorithm> linearAlgorithms;
    private final List<SystemAlgorithm> systemAlgorithms;

    public AlgorithmManager() {
        this.linearAlgorithms = List.of(
                new FixedPoint(),
                new NewtonLinear(),
                new Secant()
        );
        this.systemAlgorithms = List.of(
                new NewtonSystem()
        );
    }

    public LinearAlgorithm getLinearAlgorithmAt(int order) {
        return linearAlgorithms.get(order);
    }

    public SystemAlgorithm getSystemAlgorithmAt(int order) {
        return this.systemAlgorithms.get(order);
    }

    public List<LinearAlgorithm> getLinearAlgorithms() {
        return linearAlgorithms;
    }

    public List<SystemAlgorithm> getSystemAlgorithms() {
        return systemAlgorithms;
    }
}
