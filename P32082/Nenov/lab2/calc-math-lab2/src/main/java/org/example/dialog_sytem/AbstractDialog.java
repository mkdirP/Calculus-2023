package org.example.dialog_sytem;

import org.example.dialog_sytem.exceptions.DialogException;

public abstract class AbstractDialog implements DialogElement {
    private DialogContext context;
    private DialogElement next;

    @Override
    public void setNext(DialogElement dialog) {
        next = dialog;
    }

    @Override
    public DialogElement getNext() {
        return next;
    }

    public DialogContext getContext() {
        return context;
    }

    private void playNext() throws DialogException {
        if (getNext() != null)
            getNext().play(context);
    }

    protected abstract void action();

    @Override
    public final void play(DialogContext context) throws DialogException {
        this.context = context;
        action();
        playNext();
    }
}
