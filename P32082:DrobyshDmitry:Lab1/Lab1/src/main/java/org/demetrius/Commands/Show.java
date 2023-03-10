package org.demetrius.Commands;

import org.demetrius.Managers.MatrixManager;
import org.demetrius.util.Environment;

public class Show implements ICommand{

    @Override
    public void execute(Environment environment, String message) {
        MatrixManager matrixManager = environment.getCollectionManager();
        if(matrixManager.length()>0){
            environment.getPrintStream().println(matrixManager.toString());
            environment.getPrintStream().println("Finished successfully");
        }
        else {
            environment.getPrintStream().println("Collection is empty");
        }

    }

    @Override
    public String getName() {
        return "show";
    }

    @Override
    public String getDescription() {
        return "show : print to standard output all elements of the collection in string representation.";
    }
}



