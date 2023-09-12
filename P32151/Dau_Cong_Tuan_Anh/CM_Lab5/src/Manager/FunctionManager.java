package Manager;

import Model.Function.Function;
import Model.Function.firstFunction;
import Model.Function.secondFunction;

import java.util.List;

import static Utils.Print.*;

public class FunctionManager {
    private final List<Function> functionList;

    public FunctionManager() {
        functionList = List.of(new firstFunction(),
                                new secondFunction());
    }

    public Function getFunctionByIndex(Integer ix) {
        return functionList.get(ix);
    }

    public Integer getSize() {
        return this.functionList.size();
    }

    public void printList() {
        printlnMessage("List of function: ");
        for (Integer i = 0; i < this.getSize(); ++i) {
            printlnMessage("function " + i + 1 + " " + this.getFunctionByIndex(i).toString());
        }
    }

    public List<Function> getFunctionList() {
        return this.functionList;
    }
}
