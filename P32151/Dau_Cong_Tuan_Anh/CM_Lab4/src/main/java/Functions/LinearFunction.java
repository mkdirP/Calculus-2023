package Functions;

import Equations.LinearEquation;
import IO.InputSet;
import IO.OutputSet;
import Model.Function;
import Model.Point;

import java.util.List;

public class LinearFunction implements Function {
    private String name = "Linear function";

    @Override
    public OutputSet execute(InputSet inputSet) {
        Double a;
        Double b;
        Double SX = 0.0, SY = 0.0, SXX=0.0, SXY=0.0;
        List<Point> pointList = inputSet.getPointList();
        for(int i = 0 ;i < inputSet.getPointList().size(); ++i) {
            SX += pointList.get(i).getX();
            SY += pointList.get(i).getY();
            SXX += Math.pow(pointList.get(i).getX(), 2);
            SXY += pointList.get(i).getX()*pointList.get(i).getY();
        }

        a = (SXY* inputSet.getN() - SX*SY) / (SXX* inputSet.getN() - Math.pow(SX, 2));
        b = (SXX* SY - SX*SXY) / (SXX* inputSet.getN() - Math.pow(SX, 2));

        LinearEquation linearEquation = new LinearEquation(a, b);
        for(int i = 0 ;i < inputSet.getN(); ++i) {
            inputSet.getPointList().get(i).setF_x(
                    linearEquation.getValue(pointList.get(i).getX()));
            inputSet.getPointList().get(i).setError();
        }

        return new OutputSet( linearEquation, getR(inputSet), getS(inputSet), getDelta(inputSet));
    }

    @Override
    public String toString() {
        return "Linear Function";
    }
}
