package Model.Interpolation;

import IO.InputSet;
import Model.Point;

import java.util.List;

public class Lagrange implements Polynomial{
    InputSet inputSet = null;
    public Lagrange() {

    }
    public Lagrange(InputSet inputSet) {
        this.inputSet = inputSet;
    }

    public void setInputSet(InputSet inputSet) {
        this.inputSet = inputSet;
    }

    @Override
    public Double predictValueAt(Double x) {
        List<Point> pointList = this.inputSet.getPointList();
        for(int i = 0 ;i < pointList.size(); ++i) {
            if(pointList.get(i).getX() == x) {
                return pointList.get(i).getY();
            }
        }
        Double mulAllX = 1.0;
        Double res = 0.0;
        for(int i = 0 ;i < pointList.size();++i) {
            mulAllX *= (x - pointList.get(i).getX());
        }
        for(int i =0 ; i < pointList.size(); ++i) {
            Double temp = mulAllX / (x - pointList.get(i).getX());
            for(int j = 0; j < i ; ++j) {
                temp /= (pointList.get(i).getX() - pointList.get(j).getX());
            }

            for(int j = i + 1; j < pointList.size() ; ++j) {
                temp /= (pointList.get(i).getX() - pointList.get(j).getX());
            }

            temp *= pointList.get(i).getY();
            res += temp;
        }

        return res;
    }

    @Override
    public String toString() {
        return "Lagrange";
    }
}
