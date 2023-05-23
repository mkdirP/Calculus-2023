package Graph;

import IO.InputSet;
import Model.Interpolation.Polynomial;
import Model.Point;
import org.jfree.data.xy.XYSeries;

import java.util.Comparator;
import java.util.List;

public class DataSet {
    public static XYSeries createSeriesFromFunction(Polynomial polynomial,
                                                    Double left,
                                                    Double right,
                                                    Double step) {
        final XYSeries ret = new XYSeries(polynomial.toString());
        for(double i = left; i < right; i += step) {
            ret.add(i, polynomial.predictValueAt(i));
        }

        return ret;
    }

    public static XYSeries createSeriesFromPoints(InputSet inputSet) {
        final XYSeries ret = new XYSeries("Points");
        for(int i = 0;i < inputSet.getSize();++i) {
            ret.add(inputSet.getPointList().get(i).getX(), inputSet.getPointList().get(i).getY());
        }
        return ret;
    }
}
