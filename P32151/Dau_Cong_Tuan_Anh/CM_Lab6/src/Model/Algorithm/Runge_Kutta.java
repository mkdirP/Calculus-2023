package Model.Algorithm;

import IO.InputSet;
import Model.Function.Function;

public class Runge_Kutta implements Algorithm{
    private String algo = "Runge - Kytta";
    @Override
    public Double[][] execute(InputSet inputSet, Function func) {
        func.ResolveC(inputSet.getA(), inputSet.getY0());
        int n = (int) ((inputSet.getB()- inputSet.getA())/ inputSet.getH());
        Double[][] tb = new Double[n][5];
        for(int i = 0; i < n; ++i) {
            tb[i][0] = inputSet.getA() + i* inputSet.getH();
        }
        tb[0][1] = inputSet.getY0();
        for(int i = 1 ;i < n;++i) {
            Double k1 = func.ValueAt(tb[i - 1][0], tb[i - 1][1]);
            Double k2 = func.ValueAt(tb[i - 1][0] + inputSet.getH()/ 2,tb[i - 1][1] + k1/2 );
            Double k3 = func.ValueAt(tb[i - 1][0] + inputSet.getH()/ 2,tb[i - 1][1] + k2/2 );
            Double k4 = func.ValueAt(tb[i - 1][0] + inputSet.getH(), tb[i-1][1] + k3);
            tb[i][1] = tb[i - 1][1]
                    + (inputSet.getH()/6)
                    * (k1 + 2*k2 +2*k3 + k4);
        }

        for(int i = 0 ;i < n; ++i) {
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
