package Model.Algorithm;

import IO.InputSet;
import Model.Function.Function;
import Model.Point;

import java.util.List;

public class AdvancedEuler implements Algorithm{
    private final String algo = "Advanced Euler";

    @Override
    public Double[][] execute(InputSet inputSet, Function func) {
        func.ResolveC(inputSet.getA(), inputSet.getY0());
        int n = (int) ((inputSet.getB()- inputSet.getA())/ inputSet.getH());
        Double[][] tb = new Double[n][5];
        for(int i = 0; i < n; ++i) {
            tb[i][0] = inputSet.getA() + i * inputSet.getH();
        }
        tb[0][1] = inputSet.getY0();
        for(int i = 1; i < n; ++i) {
            Double fxy = func.ValueAt(tb[i-1][0], tb[i - 1][1]);
            tb[i][1] = tb[i- 1][1] +
                    (inputSet.getH()/2) *
                            (fxy + func.ValueAt(tb[i][0],tb[i-1][1] + inputSet.getH()) *fxy);
        }

        for(int i = 0 ;i < n;++i) {
            tb[i][2] = func.ValueAt(tb[i][0], tb[i][1]);
            tb[i][3] = func.yAt(tb[i][0]);
            tb[i][4] = Math.abs((Math.pow(tb[i][1], inputSet.getH())
                    - Math.pow(tb[i][1], inputSet.getH() / 2))
                    /(Math.pow(2, i + 1) - 1));
        }
        return tb;
    }

    @Override
    public String toString() {
        return this.algo;
    }
}
