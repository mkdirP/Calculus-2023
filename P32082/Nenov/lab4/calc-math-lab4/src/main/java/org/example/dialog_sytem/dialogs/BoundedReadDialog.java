package org.example.dialog_sytem.dialogs;

public class BoundedReadDialog<T extends Comparable<T>> extends ReadDialog<T>{
    private final T lBound, rBound;
    private final String key;
    public BoundedReadDialog(Class<T> type, String key, T lBound, T rBound) {
        super(type, key);
        this.lBound = lBound;
        this.rBound = rBound;
        this.key = key;
    }

    public BoundedReadDialog(Class<T> type, String key, T lBound, T rBound, String message) {
        super(type, key, message);
        this.lBound = lBound;
        this.rBound = rBound;
        this.key = key;
    }

    @Override
    protected void action() {
        while (true) {
            super.action();
            T value = getContext().get(key);
            if (value == null || value.compareTo(lBound) < 0 || value.compareTo(rBound) > 0)
                getContext().write("Введенные данные выходят за допустимые границы!");
            else
                break;
        }
    }
}
