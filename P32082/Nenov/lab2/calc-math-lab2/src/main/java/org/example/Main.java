package org.example;

import org.example.dialog_sytem.DialogContext;
import org.example.dialog_sytem.DialogContextImpl;
import org.example.dialog_sytem.DialogElement;
import org.example.dialog_sytem.dialogs.*;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        DialogContext dialogContext = new DialogContextImpl(System.in, System.out);
        DialogElement dialog = new DialogSequence(
                // READ MODE
                new ChooseInputModeDialog(),

                // SYSTEM OR ONE EQ
                new BoundedReadDialog<>(Integer.class, "eq_type", 1, 2,
                        "1) Решить систему уравнений %n2) Решить уравнение"),
                // EQUATION INFO
                new EqConditionDialog("eq_type", Map.of(
                        1, Dialogs.askForEqSystem(),
                        2, Dialogs.askForEq()
                    )
                ),

                // OUTPUT MODE
               new ChooseOutputModeDialog(),

                // SOLVING
                new EqConditionDialog("eq_type", Map.of(
                        1, Dialogs.solveEqSystem(),
                        2, Dialogs.solveEq()
                    )
                )
        );

        try {
            dialog.play(dialogContext);
        } catch (Exception e) {
            e.printStackTrace();
        }
        dialogContext.destroy();
    }

}