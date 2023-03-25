package entity;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class EquationData {

    Matrix aMatrix;
    double[] bVector;

    public static boolean isEquationValid(double[][] matrix, double[] freeMembers, int rows, int columns) {
        if ((rows <= 0) || (columns <= 0)) {
            return false;
        }
        if ((matrix == null) || (matrix.length != rows) || (matrix[0].length != columns) || (freeMembers == null) || (matrix.length != freeMembers.length)) {
            return false;
        }
        for (int i = 0; i < rows; i++) {
            if ((matrix[i] == null )|| (matrix[i].length != columns)) {
                return false;
            }
            for (int j = 0; j < columns; j++) {
                if (Double.isNaN(matrix[i][j])) {
                    return false;
                }
            }
            if (Double.isNaN(freeMembers[i])) {
                return false;
            }
        }
        return true;
    }
}
