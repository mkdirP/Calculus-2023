package org.example.dialog_sytem.dialogs;

import org.example.dialog_sytem.AbstractDialog;
import org.example.dialog_sytem.DialogElement;

import java.util.ArrayList;
import java.util.List;

public class DialogSequence extends AbstractDialog {

    private final List<DialogElement> dialogs;
    public DialogSequence(DialogElement... elements) {
        dialogs = new ArrayList<>(List.of(elements));
    }

    public void add(DialogElement dialog) {
        dialogs.add(dialog);
    }

    @Override
    protected void action() {
        if (dialogs.size() == 0)
            return;
        dialogs.get(dialogs.size()-1).setNext(getNext());
        setNext(dialogs.get(0));
        for (int i = 0; i < dialogs.size()-1; i++) {
            dialogs.get(i).setNext(dialogs.get(i+1));
        }
    }
}
