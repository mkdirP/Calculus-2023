package org.example.dialog_sytem;

import java.util.function.Function;

public class CDPair {
    private final Function<DialogContext, Boolean> condition;
    private final DialogElement branch;
    public CDPair(Function<DialogContext, Boolean> condition, DialogElement branch) {
        this.condition = condition;
        this.branch = branch;
    }

    public DialogElement getBranch() {
        return branch;
    }

    public Function<DialogContext, Boolean> getCondition() {
        return condition;
    }
}
