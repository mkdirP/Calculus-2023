package org.demetrius.util;

import org.demetrius.Commands.ICommand;
import org.demetrius.Managers.*;

import java.io.BufferedReader;
import java.io.PrintStream;
import java.util.ArrayList;

public class Environment {
    private MatrixManager matrixManager;
    private BufferedReader bufferedReader;
    private PrintStream printStream;
    private ArrayList<String> history;
    private ICommand[] commands;

    public MatrixManager getMatrixManager() {
        return matrixManager;
    }

    public void setMatrixManager(MatrixManager matrixManager) {
        this.matrixManager = matrixManager;
    }

    public ICommand[] getCommands() {
        return commands;
    }

    public void setCommands(ICommand[] commands) {
        this.commands = commands;
    }

    public Environment(MatrixManager matrixManager, BufferedReader bufferedReader, PrintStream printStream, ArrayList<String> history, ICommand[] commands){
        this.matrixManager = matrixManager;
        this.bufferedReader = bufferedReader;
        this.printStream = printStream;
        this.history = history;
        this.commands = commands;
    }

    public MatrixManager getCollectionManager() {
        return matrixManager;
    }

    public void setCollectionManager(MatrixManager matrixManager) {
        this.matrixManager = matrixManager;
    }

    public BufferedReader getBufferedReader() {
        return bufferedReader;
    }

    public void setBufferedReader(BufferedReader bufferedReader) {
        this.bufferedReader = bufferedReader;
    }

    public PrintStream getPrintStream() {
        return printStream;
    }

    public void setPrintStream(PrintStream printStream) {
        this.printStream = printStream;
    }

    public ArrayList<String> getHistory() {
        return history;
    }
    public void setHistory(ArrayList<String> history) {
        this.history = history;
    }

}
