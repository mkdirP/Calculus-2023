package org.example.dialog_sytem;

import org.example.dialog_sytem.exceptions.DialogException;

import java.io.InputStream;
import java.io.PrintStream;

public interface DialogContext {
    <T> void read(Class<T> type, String key) throws DialogException;
    void write(String s);
    <T> T get(String key);
    void changeInputStream(InputStream inputStream);
    void changeOutputStream(PrintStream stream);
    void setCanWrite(boolean canWrite);
    void destroy();
}
