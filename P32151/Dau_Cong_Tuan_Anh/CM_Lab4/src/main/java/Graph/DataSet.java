package Graph;

import IO.InputSet;
import Model.Equation;
import Model.Function;
import Model.Point;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;

import java.util.List;

public class DataSet {
    public static XYSeries createSeriesFromFunction(Equation equation,
                                                    Double left,
                                                    Double right,
                                                    Double step) {
        final XYSeries ret = new XYSeries(equation.toString());
        for(double i = left; i < right; i += step) {
            ret.add(i, equation.getValue(i));
        }

        return ret;
    }

    public static XYSeries createSeriesFromPoints(InputSet inputSet) {
        final XYSeries ret = new XYSeries("Points");
        for(int i = 0;i < inputSet.getN();++i) {
            ret.add(inputSet.getPointList().get(i).getX(), inputSet.getPointList().get(i).getY());
        }

        return ret;
    }
}
