package org.example.dialog_sytem;

import org.example.dialog_sytem.exceptions.DialogException;

import java.util.ArrayList;
import java.util.List;

public interface DialogElement {

    DialogElement getNext();
    void setNext(DialogElement dialog);
    void play(DialogContext context) throws DialogException;
}
