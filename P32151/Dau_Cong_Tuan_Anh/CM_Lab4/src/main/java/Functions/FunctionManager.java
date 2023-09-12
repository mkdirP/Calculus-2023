package Functions;

import Model.Function;
import Utils.print;

import java.util.ArrayList;
import java.util.List;

public class FunctionManager {

    private List<Function> functionList;

    public FunctionManager() {
        functionList = List.of(new LinearFunction(),
                                new PolynomialFunction_2(),
                                new PolynomialFunction_3(),
                                new ExponentialFunction(),
                                new LogarithmicFunction(),
                                new PowerFunction());
    }

    public Function getFunctionByIndex(Integer index) {
        return this.functionList.get(index);
    }

    public void printList() {
        print.printTable("List of Function", this.functionList);
    }

    public List<Function> getFunctionList (){
        return this.functionList;
    }
}
