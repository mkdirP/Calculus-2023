package org.example.math.systems;

public class EquationSystem {
    private final MultiArgFunction[] system;

    public EquationSystem(MultiArgFunction... functions) {
        system = functions;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("\n--\n");
        for (int i = 0; i < system.length; i++) {
            sb.append("| ");
            sb.append(system[i].toString());
            sb.append("\n");
        }
        sb.append("--");
        return sb.toString();
    }
}
