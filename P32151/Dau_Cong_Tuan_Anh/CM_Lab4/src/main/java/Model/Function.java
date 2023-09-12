package Model;

import IO.InputSet;
import IO.OutputSet;

public interface Function {
    public OutputSet execute(InputSet inputSet);

    public default Double getR(InputSet inputSet) {
        Double a = 0.0, b = 0.0;
        for(int i = 0 ;i < inputSet.getN(); ++i) {
            a += Math.pow(inputSet.getPointList().get(i).getError(), 2);
            b+= Math.pow(inputSet.getPointList().get(i).getF_x(), 2);
        }
        b = b*(inputSet.getN() - 1)/ inputSet.getN();
        return 1 - a / b;
    }

    public default Double getS(InputSet inputSet) {
        double s = 0;
        for(int i = 0; i < inputSet.getN();++i) {
            s += Math.pow(inputSet.getPointList().get(i).getError(), 2);
        }

        return s;
    }

    public default Double getDelta(InputSet inputSet) {
        Double ret = getS(inputSet);
        ret/= inputSet.getN();
        ret = Math.sqrt(ret);
        return ret;
    }
}
