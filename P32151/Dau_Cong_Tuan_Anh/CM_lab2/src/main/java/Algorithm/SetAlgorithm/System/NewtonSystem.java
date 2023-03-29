package Algorithm.SetAlgorithm.System;

import Algorithm.Model.Exception.ImplementFirstValuesException;
import Algorithm.Model.Interface.SystemAlgorithm;
import Equation.Model.Interface.SystemEquation;
import Utils.Printer;
import Utils.Result.SystemResult;

public class NewtonSystem implements SystemAlgorithm {
    private final String name = "Newton(system) ";
    private double x;
    private double y;

    private SystemResult result = new SystemResult();

    @Override
    public void ImplementFirstValue(double x, double y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public void execute(SystemEquation equation)
                    throws ImplementFirstValuesException {
        double f_x, f_y, g_x, g_y, delta_x, delta_y, f, g;

        do{
            f_x = equation.derivativeFxForX(x, y);
            f_y = equation.derivativeFxForY(x, y);
            g_x = equation.derivativeGxForX(x, y);
            g_y = equation.derivativeGxForY(x, y);

            f = -equation.FxAt(x, y);
            g = -equation.GxAt(x, y);

            // check if equation have root with given value or not
            // throw exception if we cannot find root with given root
            if(f_x * g_y - f_y * g_x == 0)
                throw new ImplementFirstValuesException();
            delta_x = (f * g_y - g * f_y) / (f_x * g_y - f_y * g_x);
            delta_y = (f_x * g - g_x * f) / (f_x * g_y - f_y * g_x);

            // set value of x and y for next loop step
            x += delta_x;
            y += delta_y;

//            Printer.println(delta_x + " " + delta_y + " " + f_x + " " + f_y + " " +g_x + " " +g_y + " " + f + " " + g +"\n");

            // save result of cur0rent step
            result.setRoot(x, y);
            result.setError(Math.abs(delta_x), Math.abs(delta_y));
            result.increaseStep();
        } while(Math.abs(delta_x) >= ERROR || Math.abs(delta_y) >= ERROR);
    }

    @Override
    public SystemResult getResult() {
        return this.result;
    }

    @Override
    public String getName() {
        return this.name;
    }
}
