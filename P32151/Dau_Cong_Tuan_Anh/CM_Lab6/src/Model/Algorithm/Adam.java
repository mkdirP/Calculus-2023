package Model.Algorithm;

import IO.InputSet;
import Model.Function.Function;

public class Adam implements Algorithm{
    private final String algo = "Adam";
    @Override
    public Double[][] execute(InputSet inputSet, Function func) {
        func.ResolveC(inputSet.getA(), inputSet.getY0());
        int n = (int) ((inputSet.getB()- inputSet.getA())/ inputSet.getH());
        Double[][] tb = new Double[n][5];
        for(int i = 0; i < n; ++i) {
            tb[i][0] = inputSet.getA() + i* inputSet.getH();
        }
        tb[0][1] = inputSet.getY0();
        tb[0][2] = func.ValueAt(tb[0][0] , tb[0][1]);
        tb[0][3] = func.yAt(tb[0][0]);
        tb[0][4] = Math.abs(tb[0][1] - tb[0][3]);
        for(int i = 1; i < n;++i) {
            Double[] f = new Double[4];
            f[0] = func.ValueAt(tb[i-1][0], tb[i-1][1]);
            if(i == 1) f[1] = 0.0;
            else f[1] = func.ValueAt(tb[i-2][0], tb[i-2][1]);
            if(i <= 2) f[2] = 0.0;
            else f[2] = func.ValueAt(tb[i-3][0], tb[i-3][1]);
            if(i <= 3) f[3] = 0.0;
            else f[3] = func.ValueAt(tb[i-4][0], tb[i-4][1]);
            Double deltaFx = f[0] - f[1];
            Double deltaFx1 = f[0] - 2*f[1] + f[2];
            Double deltaFx2 = f[0] - 3*f[1] + 3*f[2] - f[3];
            tb[i][1] = tb[i-1][1]
                    + inputSet.getH() * func.ValueAt(tb[i-1][0], tb[i-1][1])
                    + Math.pow(inputSet.getH(), 2) / 2 * deltaFx
                    + 5* Math.pow(inputSet.getH(), 3)/12 * deltaFx1
                    + 3* Math.pow(inputSet.getH(), 4)/8 * deltaFx2;
        }

        for(int i = 1; i < n; ++i) {
            tb[i][2] = func.ValueAt(tb[i][0], tb[i][1]);
            tb[i][3] = func.yAt(tb[i][0]);
            tb[i][4] = Math.max(tb[i - 1][4], Math.abs(tb[i][3] - tb[i][1]));
        }

        return tb;
    }

    @Override
    public String toString() {
        return this.algo;
    }
}
