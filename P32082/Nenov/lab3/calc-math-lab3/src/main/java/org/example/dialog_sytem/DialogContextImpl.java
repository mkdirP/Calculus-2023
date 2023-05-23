package org.example.dialog_sytem;

import org.example.dialog_sytem.exceptions.DialogException;
import org.example.dialog_sytem.exceptions.DialogInputException;

import java.io.InputStream;
import java.io.PrintStream;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;
import java.util.Scanner;

public class DialogContextImpl implements DialogContext{
    private Scanner scanner;
    private PrintStream output;
    private Map<String, Object> context;
    private boolean canWrite = true;
    public DialogContextImpl(InputStream stream, PrintStream printStream) {
        scanner = new Scanner(stream);
        output = printStream;
        context = new HashMap<>();
    }
    @Override
    public <T> void read(Class<T> type, String key) throws DialogException {
        context.put(key, parseSimpleValueFromString(scanner.next(), type));
    }

    @Override
    public <T> T get(String key) {
        if (context.containsKey(key))
            return (T) context.get(key);
        return null;
    }

    @Override
    public void write(String s) {
        if (canWrite)
            output.println(s);
    }

    @Override
    public void changeInputStream(InputStream inputStream) {
        scanner = new Scanner(inputStream);
    }

    @Override
    public void changeOutputStream(PrintStream stream) {
        output = stream;
    }

    @Override
    public void setCanWrite(boolean canWrite) {
        this.canWrite = canWrite;
    }

    @Override
    public void destroy() {
        context.clear();
        scanner.close();
        output.close();
    }

    @SuppressWarnings("unchecked")
    private <T> T parseSimpleValueFromString(String s, Class<T> valueType) throws DialogException {
        try {
            if (valueType == Integer.class || valueType == int.class) {
                return (T) Integer.valueOf(s);
            } else if (valueType == Double.class || valueType == double.class) {
                return (T) Double.valueOf(s);
            } else if (valueType == Long.class || valueType == long.class) {
                return (T) Long.valueOf(s);
            } else if (valueType == Boolean.class || valueType == boolean.class) {
                if (!Objects.equals(s, "true") && !Objects.equals(s, "false"))
                    throw new IllegalArgumentException();
                return (T) Boolean.valueOf(s);
            } else if (valueType == Float.class || valueType == float.class) {
                return (T) Float.valueOf(s);
            } else if (valueType == String.class) {
                return (T) s;
            }
        } catch (IllegalArgumentException e) {
            throw new DialogInputException();
        }
        throw new DialogInputException();
    }


}
