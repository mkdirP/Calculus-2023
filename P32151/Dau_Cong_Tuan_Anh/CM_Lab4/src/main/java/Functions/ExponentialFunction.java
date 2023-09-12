package Functions;

import Equations.ExponentialEquation;
import IO.InputSet;
import IO.OutputSet;
import Model.Function;

public class ExponentialFunction implements Function {
    @Override
    public OutputSet execute(InputSet inputSet) {
        Integer n = inputSet.getN();
        double[] x = new double[n];
        double[] y  = new double[n];
        double[] f_x = new double[n];

        for(int i = 0; i < n; ++i) {
            x[i] = inputSet.getPointList().get(i).getX();
            y[i] = Math.log(inputSet.getPointList().get(i).getY());
        }

        Double SX = 0.0, SY = 0.0, SXX=0.0, SXY=0.0;
        for(int i = 0 ;i < n; ++i) {
            SX += x[i];
            SY += y[i];
            SXX += Math.pow(x[i], 2);
            SXY += x[i]*y[i];
        }

        double a = (SXY* inputSet.getN() - SX*SY) / (SXX* inputSet.getN() - Math.pow(SX, 2));
        double b = (SXX* SY - SX*SXY) / (SXX* inputSet.getN() - Math.pow(SX, 2));

        ExponentialEquation equation = new ExponentialEquation(Math.pow(Math.E,b), a);

        for(int i = 0 ;i < n; ++i) {
            inputSet.getPointList().get(i).setF_x(equation.getValue(inputSet.getPointList().get(i).getX()));
            inputSet.getPointList().get(i).setError();
        }

        return new OutputSet( equation, getR(inputSet), getS(inputSet), getDelta(inputSet));
    }

    @Override
    public String toString() {
        return "Exponential Function";
    }
}
