package org.demetrius.MathPackage;

import org.demetrius.Data.Matrix;

import java.math.BigDecimal;

public class FromGauss {
    public static double[][] moveLines(double[][] matrixArray){
        for (int i = 0; i < matrixArray.length; i++) {
            if (matrixArray[i][i]==0){
                for (int j = 0; j < matrixArray.length; j++) {
                    if(matrixArray[j][i]!=0){
                        for (int k = 0; k < matrixArray.length+1; k++) {
                            matrixArray[i][k]+=matrixArray[j][k];
                        }
                        break;
                    }
                }
            }
        }
        return matrixArray;
    }


    public static double[][] forwardStroke(double[][] matrixArray){
        double c;
        matrixArray = moveLines(matrixArray);
        for (int i = 0; i < matrixArray.length; i++) {
            for (int j = i+1; j < matrixArray.length ; j++) {
                if(matrixArray[i][i]==0){
                    for (int k = i; k <matrixArray.length ; k++) {
                        if(matrixArray[k][i]!=0){
                            for (int l = 0; l < matrixArray.length+1; l++) {
                                matrixArray[i][l]+=matrixArray[k][l];
                            }
                        }
                    }
                }
                c = matrixArray[j][i]/matrixArray[i][i];
                for (int k = matrixArray.length; k >=i ; k--) {
                    matrixArray[j][k] -=c*matrixArray[i][k];
                }
            }
        }
        return matrixArray;
    }

    public static BigDecimal determinant(double[][] matrixArray){
        matrixArray = forwardStroke(matrixArray);
        BigDecimal determinant = BigDecimal.valueOf(1);
        double tmp = 0;
        // finding determinant and creating diagonal of ones
        for (int i = 0; i < matrixArray.length; i++) {
            tmp = matrixArray[i][i];
            determinant = determinant.multiply(BigDecimal.valueOf(tmp));
        }
        return determinant;
    }


    public static double[][] diagonalMatrix(double[][] matrixArray){
        matrixArray = forwardStroke(matrixArray);
        double tmp = 0;
        // finding determinant and creating diagonal of ones
        for (int i = 0; i < matrixArray.length; i++) {
            tmp = matrixArray[i][i];
            for (int j = 0; j < matrixArray.length+1; j++) {
                matrixArray[i][j]/=tmp;
            }
        }
        return matrixArray;
    }

    public static double[] reverseStroke(double[][] matrixArray){
        matrixArray = diagonalMatrix(matrixArray);
        double[] allX = new double[matrixArray.length];
        allX[matrixArray.length-1] = matrixArray[matrixArray.length-1][matrixArray.length];
        for (int i = matrixArray.length-2; i >=0 ; i--) {
            allX[i] = matrixArray[i][matrixArray.length];
            for (int j = i+1; j < matrixArray.length ; j++) {
                allX[i]-=matrixArray[i][j]*allX[j];
            }
        }
        return allX;
    }

    public static double[] residualVectors(double[][] originalMatrix, double[][] matrixArray){
        double [] allX = reverseStroke(matrixArray);
        double[] residualVectors = new double[allX.length];
        double leftPart = 0;
        for (int i = 0; i < originalMatrix.length; i++) {
            for (int j = 0; j < originalMatrix.length; j++) {
                leftPart+=allX[j]*originalMatrix[i][j];
            }
            residualVectors[i] =  originalMatrix[i][originalMatrix.length]-leftPart;
            leftPart = 0;
        }
        return residualVectors;
    }
}
