package org.example.dialog_sytem.dialogs;

import org.example.dialog_sytem.exceptions.DialogException;

public class ReadDialog<T> extends CustomDialog{
    public ReadDialog(Class<T> type, String key) {
        super((context -> {
            boolean run = true;
            while (run) {
                try {
                    context.read(type, key);
                    run = false;
                } catch (DialogException ignored) {
                }
            }
        }));
    }

    public ReadDialog(Class<T> type, String key, String message) {
        super((context -> {
            boolean run = true;
            while (run) {
                try {
                    context.write(String.format(message));
                    context.read(type, key);
                    run = false;
                } catch (DialogException ignored) {
                }
            }
        }));
    }
}
