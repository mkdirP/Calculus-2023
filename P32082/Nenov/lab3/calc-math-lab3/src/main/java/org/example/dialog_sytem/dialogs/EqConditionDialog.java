package org.example.dialog_sytem.dialogs;

import org.example.dialog_sytem.AbstractDialog;
import org.example.dialog_sytem.DialogElement;

import java.util.HashMap;
import java.util.Map;

public class EqConditionDialog extends AbstractDialog {
    private final String key;
    private final Map<Object, DialogElement> branches;

    public EqConditionDialog(String valueKey, Map<Object, DialogElement> conditionBranches) {
        key = valueKey;
        branches = conditionBranches;
    }

    public EqConditionDialog(String valueKey, Object equals, DialogElement branch) {
        key = valueKey;
        branches = new HashMap<>();
        branches.put(equals, branch);
    }

    @Override
    protected void action() {
        Object value = getContext().get(key);
        if (value == null || !branches.containsKey(value))
            return;
        branches.get(value).setNext(getNext());
        setNext(branches.get(value));
    }
}
