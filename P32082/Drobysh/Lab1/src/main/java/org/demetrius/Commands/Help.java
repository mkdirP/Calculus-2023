package org.demetrius.Commands;

import org.demetrius.util.Environment;

public class Help implements ICommand{
    @Override
    public void execute(Environment environment, String message) {
        for (int i = 0 ; i < environment.getCommands().length; i++){
            environment.getPrintStream().println(environment.getCommands()[i].getDescription());
        }
    }

    @Override
    public String getName() {
        return "help";
    }

    @Override
    public String getDescription() {
        return "help : Display help for available commands.";
    }
}