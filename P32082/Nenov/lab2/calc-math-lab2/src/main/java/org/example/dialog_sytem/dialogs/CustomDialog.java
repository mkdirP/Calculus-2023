package org.example.dialog_sytem.dialogs;

import org.example.dialog_sytem.AbstractDialog;
import org.example.dialog_sytem.DialogContext;

import java.util.function.Consumer;

public class CustomDialog extends AbstractDialog {
    private final Consumer<DialogContext> action;
    public CustomDialog(Consumer<DialogContext> action) {
        this.action = action;
    }

    @Override
    protected void action() {
        action.accept(getContext());
    }

}
