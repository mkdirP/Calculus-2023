package org.example.dialog_sytem.dialogs;

public class SayDialog extends CustomDialog {

    public SayDialog(String message, Object... args) {
        super((context -> context.write(String.format(message, args))));
    }
}
