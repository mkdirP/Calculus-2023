package org.demetrius.Managers;

import org.demetrius.Data.Matrix;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;

public class MatrixManager {
    GenericCollectionManager<Matrix> matrices;

    public MatrixManager(){
        matrices = new GenericCollectionManager<>();
    }

    public MatrixManager(GenericCollectionManager<Matrix> matrices){
        this.matrices = matrices;
    }
    public void add(Matrix matrix){
        matrices.getCollection().add(matrix);
    }

    public ArrayList<Matrix> getMatrices() {
        return matrices.getCollection();
    }

    public void setMatrices(ArrayList<Matrix> matrices) {
        this.matrices = new GenericCollectionManager<>(matrices);
    }

    public void removeAllElements(){
        matrices.getCollection().clear();
    }

    public Matrix getHead(){
        return this.matrices.getCollection().get(matrices.length()-1);
    }

    public Matrix getTail(){
        return matrices.getCollection().get(0);
    }

    public int length(){
        try{
            return matrices.length();
        } catch (NullPointerException nullPointerException){
            return 0;
        }
    }



    public Matrix findById(int id){
        for(Matrix matrix: matrices.getCollection()){
            if(matrix.getId()==id){
                return matrix;
            }
        }
        return null;
    }
    public boolean existsById(int id){
        return findById(id) != null;
    }

    public void removeById(int id){
        if (existsById(id)) {
            matrices.getCollection().remove(findById(id));
        }
    }

    public void removeLast(){
        this.matrices.getCollection().remove(findById(matrices.length()));
    }

    public void replace(int id, double[][] matrix){
        Matrix currentMatrix = findById(id);
        if(currentMatrix!=null){
            currentMatrix.setMatrix(matrix);
        }
    }

    @Override
    public String toString(){
        String answer = "";
        answer+=("Displaying the elements of a collection...\n");
        for (Matrix matrix : matrices.getCollection()) {
            answer+=(String.format("Element with id: %d",matrix.getId())+"\n");
            answer+=matrix.toString()+"\n";
        }
        return answer;
    }
}



