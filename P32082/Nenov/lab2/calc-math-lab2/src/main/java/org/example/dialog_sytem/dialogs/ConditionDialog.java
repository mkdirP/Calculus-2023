package org.example.dialog_sytem.dialogs;

import org.example.dialog_sytem.AbstractDialog;
import org.example.dialog_sytem.CDPair;
import org.example.dialog_sytem.DialogContext;
import org.example.dialog_sytem.DialogElement;

import java.util.function.Function;

public class ConditionDialog extends AbstractDialog {
    private final CDPair[] pairs;
    public ConditionDialog(CDPair... pairs) {
        this.pairs = pairs;
    }

    @Override
    protected void action() {
        for (CDPair pair : pairs) {
            if (pair.getCondition().apply(getContext())) {
                pair.getBranch().setNext(getNext());
                setNext(pair.getBranch());
                return;
            }
        }
    }
}
