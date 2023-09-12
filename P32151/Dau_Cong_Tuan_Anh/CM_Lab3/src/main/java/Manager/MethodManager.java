package Manager;

import Equation.FirstEquation;
import Model.Method;
import Method.*;

import java.util.ArrayList;
import java.util.List;

public class MethodManager {
    private List<Method> MethodList= new ArrayList<Method>();
    public MethodManager() {
        this.MethodList = List.of(new RectangleMethod_Center(),
                                    new RectangleMethod_Left(),
                                    new RectangleMethod_Right(),
                                    new SimpsonMethod(),
                                    new TrapezoidMethod());
    }

    public void addMethod(Method method) {
        this.MethodList.add(method);
    }

    public Method getMethod(Integer index) {
        return this.MethodList.get(index);
    }

    public void printList() {
        System.out.println("List of Method: ");
        for(int i  = 0 ;i < MethodList.size(); ++i) {
            System.out.println(i + " : " + MethodList.get(i).toString());
        }
    }

}
