package Manager;

import Model.Function.FirstFunction;
import Model.Function.Function;
import Model.Function.SecondFunction;
import Model.Function.ThirdFunction;

import java.util.List;

import static Utils.Print.*;

public class FunctionManager {
    private List<Function> functionList;

    public FunctionManager() {
        this.functionList = List.of(
                new FirstFunction(),
                new SecondFunction(),
                new ThirdFunction());
    }

    public List<Function> getFunctionList() {
        return functionList;
    }

    public void setFunctionList(List<Function> functionList) {
        this.functionList = functionList;
    }

    public void print() {
        printlnMessage("List Of Function: ");
        for(int i = 0 ;i < functionList.size(); ++i) {
            printlnMessage(i + 1 + " : " + functionList.get(i).toString());
        }
    }
}
