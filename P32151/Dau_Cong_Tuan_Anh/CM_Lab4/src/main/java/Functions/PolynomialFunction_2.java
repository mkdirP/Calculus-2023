package Functions;

import Equations.LinearEquation;
import Equations.PolynomialEquation_2;
import IO.InputSet;
import IO.OutputSet;
import Jama.Matrix;
import Model.Equation;
import Model.Function;
import Model.Point;
import Utils.print;

import java.util.List;

public class PolynomialFunction_2 implements Function {

    @Override
    public OutputSet execute(InputSet inputSet) {
        double[][] matrix = {{0.0, 0.0,0.0}, {0.0, 0.0,0.0}, {0.0, 0.0,0.0}};
        double[] res = {0.0, 0.0, 0.0};
        matrix[0][0] = inputSet.getN();
        for(int i = 0 ;i < matrix[0][0];++i) {
            matrix[0][1] += Math.pow(inputSet.getPointList().get(i).getX(), 1);
            matrix[0][2] += Math.pow(inputSet.getPointList().get(i).getX(), 2);
            matrix[1][2] += Math.pow(inputSet.getPointList().get(i).getX(), 3);
            matrix[2][2] += Math.pow(inputSet.getPointList().get(i).getX(), 4);
            res[0] += inputSet.getPointList().get(i).getY();
            res[1] += Math.pow(inputSet.getPointList().get(i).getX(), 1) * inputSet.getPointList().get(i).getY();
            res[2] += Math.pow(inputSet.getPointList().get(i).getX(), 2) * inputSet.getPointList().get(i).getY();
        }

        matrix[1][0] = matrix[0][1];
        matrix[1][1] = matrix[0][2];
        matrix[2][0] = matrix[1][1];
        matrix[2][1] = matrix[1][2];

//        for(int i = 0 ;i < 3; ++i) {
//            for(int j = 0 ;j < 3;++j) {
//                print.printMessage(matrix[i][j] + " ");
//            }
//            print.printMessage(res[i] + "\n");
//        }
        Matrix A = new Matrix(matrix);
        Matrix B = new Matrix(3, 1);
        B.set(0,0,res[0]);
        B.set(1,0,res[1]);
        B.set(2,0,res[2]);
        Matrix X = A.solve(B);

        PolynomialEquation_2 equation_2 = new PolynomialEquation_2(X.get(2, 0), X.get(1,0), X.get(0, 0));
        for(int i = 0; i < inputSet.getN();++i) {
            inputSet.getPointList().get(i).setF_x(equation_2.getValue(inputSet.getPointList().get(i).getX()));
            inputSet.getPointList().get(i).setError();
        }

        return new OutputSet( equation_2, getR(inputSet), getS(inputSet), getDelta(inputSet));

    }

    @Override
    public String toString() {
        return "Polynomial Function 2nd";
    }
}
