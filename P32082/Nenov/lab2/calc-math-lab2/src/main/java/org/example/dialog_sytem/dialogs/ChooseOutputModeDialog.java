package org.example.dialog_sytem.dialogs;

import org.example.dialog_sytem.exceptions.DialogException;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintStream;

public class ChooseOutputModeDialog extends DialogSequence{
    public static String DISPLAY_MODE_KEY = "display_mode";
    public static String OUTPUT_PATH_KEY = "path_out";

    public ChooseOutputModeDialog() {
        super(
                new BoundedReadDialog<>(Integer.class, DISPLAY_MODE_KEY, 1, 2,
                        "Введите число соответствующее желаемому способу вывода: %n1)В консоль %n2)В файл"),
                new EqConditionDialog(DISPLAY_MODE_KEY, 2,
                        new CustomDialog(context -> {
                            context.write("Введите путь до файла результатов работы программы");
                            context.read(String.class, OUTPUT_PATH_KEY);
                            try {
                                String fname = context.get(OUTPUT_PATH_KEY);
                                try {
                                    if (!new File(fname).createNewFile())
                                        throw new DialogException();
                                } catch (IOException e) {
                                    throw new DialogException();
                                }
                                PrintStream stream = new PrintStream(fname);
                                context.changeOutputStream(stream);
                            } catch (FileNotFoundException e) {
                                throw new RuntimeException(e);
                            }
                        })
                )
        );
    }
}
