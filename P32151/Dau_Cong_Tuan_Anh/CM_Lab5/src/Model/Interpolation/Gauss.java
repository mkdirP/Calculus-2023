package Model.Interpolation;

import IO.InputSet;
import Model.Point;

import java.util.List;

import static Utils.Print.*;

public class Gauss implements Polynomial{
    InputSet inputSet = null;
    Double[][] finiteDiffTable = null;

    public Gauss() {

    }
    public Gauss(InputSet inputSet) {
        this.inputSet = inputSet;
        this.setFiniteDiffTable(inputSet);
    }

    public void setInputSet(InputSet inputSet) {
        this.inputSet = inputSet;
    }

    public void setFiniteDiffTable(InputSet inputSet) {
        this.finiteDiffTable = this.getFiniteDiffTable(inputSet);
    }
    @Override
    public Double predictValueAt(Double x) {
        int iter = 0;
        List<Point> pointList = this.inputSet.getPointList();
        for(int i = 1 ;i < pointList.size(); ++i) {
            if(Math.abs(x - pointList.get(i).getX()) <
                            Math.abs(x - pointList.get(iter).getX()))
                iter = i;
        }

        Double h = Math.abs((pointList.get(1).getX() - pointList.get(0).getX()));
        if((x - pointList.get(iter).getX()) > 0)
            return firstCase(iter, (x - pointList.get(iter).getX())/h);
        return secondCase(iter, (x - pointList.get(iter).getX()) / h);

    }

    public Double firstCase(Integer iter, Double t) {
        double res = finiteDiffTable[iter][0] +
                finiteDiffTable[iter][1]
                        * t;
        for(int i = 2 ;i < this.inputSet.getSize(); i+= 1) {
            if(i %2 == 0) --iter;
            if(iter < 0) return res;
            Double s = 0.0;
            int temp = 1;
            for(int j = -i/2 ;j < i/2; ++j) {
                s *= (t + j);
                s /= temp++;
            }
            s*=finiteDiffTable[iter][i];
            res += s;
        }

        return res;
    }

    public Double secondCase(Integer iter, Double t) {
        if(iter == 0) return finiteDiffTable[iter][0];
        double res = finiteDiffTable[iter][0] +
                finiteDiffTable[--iter][1]
                        * t;
        for(int i = 2 ;i < this.inputSet.getSize(); i+= 1) {
            if(i % 2 == 1) --iter;
            if(iter < 0) return res;
            Double s = 0.0;
            int temp = 1;
            for(int j = -i/2 ;j < i/2; ++j) {
                s *= (t + j);
                s /= temp++;
            }
            s*=finiteDiffTable[iter][i];
            res += s;
        }

        return res;
    }

    @Override
    public String toString() {
        return "Gauss";
    }
}
