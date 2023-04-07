package org.demetrius.Commands;

import org.demetrius.Managers.MatrixManager;
import org.demetrius.util.Environment;

public class Clean implements ICommand{
    @Override
    public void execute(Environment environment, String message) {
        MatrixManager matrixManager = environment.getCollectionManager();
        matrixManager.removeAllElements();
        environment.getPrintStream().println("Collection cleaned!");
    }

    @Override
    public String getName() {
        return "clean";
    }

    @Override
    public String getDescription() {
        return "clean : clear the collection";
    }
}
