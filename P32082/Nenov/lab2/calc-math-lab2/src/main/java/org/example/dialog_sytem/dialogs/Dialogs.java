package org.example.dialog_sytem.dialogs;

import org.example.Charts;
import org.example.dialog_sytem.DialogElement;
import org.example.dialog_sytem.exceptions.DialogException;
import org.example.math.*;
import org.example.math.EqSolveMethod;
import org.example.math.results.EquationResult;
import org.example.math.results.SystemEquationResult;
import org.example.math.systems.EquationSystem;
import org.example.math.systems.SimpleSystemIterMethodForSystems;

import static org.example.math.Equations.*;

public class Dialogs {

    public static DialogElement askForEq() {
        return new DialogSequence(
                new EqConditionDialog("read_mode", 1,
                        new SayDialog("Введите номер уравнения, корень которого хотите найти%n" +
                                "1) %s %n2) %s %n3) %s", func5.toString(), func22.toString(), myFunc.toString()
                        )
                ),
                new BoundedReadDialog<>(Integer.class, "eq_id", 1, 3),
                new EqConditionDialog("read_mode", 1,
                        new SayDialog("Введите номер метода решения%n" +
                                "1) Половинного деления %n2) Ньютона %n3) Простых итераций")
                ),
                new BoundedReadDialog<>(Integer.class, "eq_method", 1, 3),
                new EqConditionDialog("read_mode", 1,
                        new SayDialog("Введите через пробел <прогрешность> <левую границу> <правую границу>")
                ),
                new ReadDialog<>(Double.class, "eq_accuracy"),
                new ReadDialog<>(Double.class, "eq_a"),
                new ReadDialog<>(Double.class, "eq_b")
        );
    }

    public static DialogElement askForEqSystem() {
        return new DialogSequence(
                new EqConditionDialog("read_mode", 1,
                        new SayDialog("Введите номер системы уравнений, корень которого хотите найти%n" +
                                "1) %s %n2) %s", new EquationSystem(system1), new EquationSystem(system2)
                        )
                ),
                new BoundedReadDialog<>(Integer.class, "eq_id", 1, 3),

                new EqConditionDialog("read_mode", 1,
                        new SayDialog("Введите через пробел <прогрешность> " +
                                "<начальное приближение x1> <начальное приближение x2>")
                ),
                new ReadDialog<>(Double.class, "eq_accuracy"),
                new ReadDialog<>(Double.class, "eq_approx1"),
                new ReadDialog<>(Double.class, "eq_approx2")
        );
    }

    public static DialogElement solveEq() {
        return new CustomDialog((context -> {
            int eqId = context.get("eq_id");
            int eqMethod = context.get("eq_method");
            double accuracy = context.get("eq_accuracy");
            double a = context.get("eq_a");
            double b = context.get("eq_b");
            EqSolveMethod method;
            Function function;
            switch (eqId) {
                case 1:
                    function = func5;
                    break;
                case 2:
                    function = func22;
                    break;
                case 3:
                    function = myFunc;
                    break;
                default:
                    throw new DialogException();
            }
            switch (eqMethod) {
                case 1:
                    method = new HalfDivisionMethod(accuracy, function);
                    break;
                case 2:
                    method = new NewtonMethod(accuracy, function);
                    break;
                case 3:
                    method = new SimpleIterationMethod(accuracy, function);
                    break;
                default:
                    throw new DialogException();
            }
            EquationResult result = method.solve(a, b);
            context.write(result.toString());
            Charts.draw(function, a, b);
        }));
    }

    public static DialogElement solveEqSystem() {
        return new CustomDialog((context -> {
            double accuracy = context.get("eq_accuracy");
            double x1 = context.get("eq_approx1");
            double x2 = context.get("eq_approx2");
            int eqId = context.get("eq_id");
            SimpleSystemIterMethodForSystems newtonMethodForSystems;
            switch (eqId) {
                case 1:
                    newtonMethodForSystems = new SimpleSystemIterMethodForSystems(accuracy, system1);
                    break;
                case 2:
                    newtonMethodForSystems = new SimpleSystemIterMethodForSystems(accuracy, system2);
                    break;
                default:
                    throw new DialogException();
            }
            SystemEquationResult[] results = newtonMethodForSystems.solve(new double[] {x1, x2});
            for (SystemEquationResult result : results) {
                context.write(result.toString());
            }
            if (results[0].getSuccess())
                Charts.drawSystem(newtonMethodForSystems.getSystem(), results[0].getResult(), results[1].getResult());
        }));
    }
}
