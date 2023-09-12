package org.example.dialog_sytem.dialogs;

import org.example.dialog_sytem.exceptions.DialogException;

import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class ChooseInputModeDialog extends DialogSequence{
    public static String READ_MODE_KEY = "read_mode";
    public static String INPUT_PATH_KEY = "path_in";
    public ChooseInputModeDialog() {
        super(
                new BoundedReadDialog<>(Integer.class, READ_MODE_KEY, 1, 2,
                        "1)Для ввода с клавиатуры %n2)Для ввода с файла"),
                new EqConditionDialog(
                        READ_MODE_KEY, 2,
                        new CustomDialog(context -> {
                            context.write("Введите путь до файла с входными данными");
                            context.read(String.class, INPUT_PATH_KEY);
                            try {
                                String fname = context.get(INPUT_PATH_KEY);
                                context.changeInputStream(new FileInputStream(fname));
                            } catch (FileNotFoundException e) {
                                throw new DialogException();
                            }
                        })
                )
        );
    }
}
