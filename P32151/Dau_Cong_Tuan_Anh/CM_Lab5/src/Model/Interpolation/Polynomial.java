package Model.Interpolation;

import IO.InputSet;
import Model.Point;
import Utils.RoundNumber;

import java.util.List;

public interface Polynomial {
    public default Double[][] getFiniteDiffTable(InputSet inputSet) {
        List<Point> pointList = inputSet.getPointList();
        int n = inputSet.getSize();
        Double[][] x = new Double[n][n];

        for(int i = 0; i < n; ++i) {
            for(int j = 0 ;j < n; ++j) {
                x[i][j] = 0.0;
            }
        }
        for(int i = 0 ;i < n; ++i) {
            x[i][0]= pointList.get(i).getY();
        }
        for(int i = n - 1; i >= 0; --i) {
            for(int j = 0;j < i;++j) {
                x[j][n -  i] = RoundNumber.roundDouble(x[j + 1][n -  i - 1] - x[j][n - i - 1]);
            }
        }

        return x;
    }



    public Double predictValueAt(Double x) ;
}
