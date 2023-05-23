package Functions;

import Equations.PolynomialEquation_2;
import Equations.PolynomialEquation_3;
import IO.InputSet;
import IO.OutputSet;
import Jama.Matrix;
import Model.Function;

public class PolynomialFunction_3 implements Function {

    @Override
    public OutputSet execute(InputSet inputSet) {
        double[][] matrix = {{0.0, 0.0,0.0, 0.0}, {0.0, 0.0,0.0, 0.0}, {0.0, 0.0,0.0, 0.0},{0.0, 0.0,0.0, 0.0} };
        double[] res = {0.0, 0.0, 0.0, 0.0};
        matrix[0][0] = inputSet.getN();
        for(int i = 0 ;i < matrix[0][0];++i) {
            matrix[0][1] += Math.pow(inputSet.getPointList().get(i).getX(), 1);
            matrix[0][2] += Math.pow(inputSet.getPointList().get(i).getX(), 2);
            matrix[0][3] += Math.pow(inputSet.getPointList().get(i).getX(), 3);
            matrix[1][3] += Math.pow(inputSet.getPointList().get(i).getX(), 4);
            matrix[2][3] += Math.pow(inputSet.getPointList().get(i).getX(), 5);
            matrix[3][3] += Math.pow(inputSet.getPointList().get(i).getX(), 6);
            res[0] += inputSet.getPointList().get(i).getY();
            res[1] += Math.pow(inputSet.getPointList().get(i).getX(), 1) * inputSet.getPointList().get(i).getY();
            res[2] += Math.pow(inputSet.getPointList().get(i).getX(), 2) * inputSet.getPointList().get(i).getY();
            res[3] += Math.pow(inputSet.getPointList().get(i).getX(), 3) * inputSet.getPointList().get(i).getY();
        }

        matrix[1][0] = matrix[0][1];
        matrix[1][1] = matrix[0][2];
        matrix[1][2] = matrix[0][3];
        matrix[2][0] = matrix[1][1];
        matrix[2][1] = matrix[1][2];
        matrix[2][2] = matrix[1][3];
        matrix[3][0] = matrix[2][1];
        matrix[3][1] = matrix[2][2];
        matrix[3][2] = matrix[2][3];
        Matrix A = new Matrix(matrix);
        Matrix B = new Matrix(4, 1);
        B.set(0,0,res[0]);
        B.set(1,0,res[1]);
        B.set(2,0,res[2]);
        B.set(3, 0, res[3]);
        Matrix X = A.solve(B);

        PolynomialEquation_3 equation_3 = new PolynomialEquation_3(X.get(3, 0), X.get(2,0), X.get(1, 0), X.get(0,0));
        for(int i = 0; i < inputSet.getN();++i) {
            inputSet.getPointList().get(i).setF_x(equation_3.getValue(inputSet.getPointList().get(i).getX()));
            inputSet.getPointList().get(i).setError();
        }

        return new OutputSet( equation_3, getR(inputSet), getS(inputSet), getDelta(inputSet));
    }

    @Override
    public String toString() {
        return "Polynomial Function 3rd";
    }
}
