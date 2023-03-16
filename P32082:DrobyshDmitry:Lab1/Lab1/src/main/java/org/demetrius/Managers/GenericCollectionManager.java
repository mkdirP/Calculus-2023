package org.demetrius.Managers;

import org.demetrius.Data.Matrix;

import java.util.ArrayList;
import java.util.Iterator;

public class GenericCollectionManager<T>{

    private ArrayList<T> collection;
    private int id;


    public ArrayList<T> getCollection() {
        return collection;
    }

    public void setCollection(ArrayList<T> collection) {
        this.collection = collection;
    }


    public GenericCollectionManager() {
        this.collection = new ArrayList<T>();
    }

    public GenericCollectionManager(ArrayList<T> collection) {
        this.collection = collection;
    }

    public GenericCollectionManager(ArrayList<T> collection, int id) {
        this.collection = collection;
        this.id = id;
    }


    public int length(){
            return this.collection.size();
    }

    public void removeAllElements(){
        collection.clear();
    }

}
