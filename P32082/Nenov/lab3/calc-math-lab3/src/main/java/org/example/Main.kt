package org.example

import org.example.dialog_sytem.DialogContext
import org.example.dialog_sytem.DialogContextImpl
import org.example.dialog_sytem.DialogElement
import org.example.dialog_sytem.dialogs.BoundedReadDialog
import org.example.dialog_sytem.dialogs.CustomDialog
import org.example.dialog_sytem.dialogs.DialogSequence
import org.example.dialog_sytem.dialogs.ReadDialog
import org.example.dialog_sytem.dialogs.SayDialog
import org.example.dialog_sytem.exceptions.DialogException
import org.example.math.integrals.*
import kotlin.math.pow


fun main() {
    val func1 = { x: Double ->
        -2*x*x*x - 3*x*x + x+ 5
    }.toMath("-2*x^3 - 3x^2 + x + 5")

    val func2 = { x: Double ->
        2.0.pow(x) - x + 1
    }.toMath("2^x - x + 1")

    val func3 = { x: Double ->
        (x*x-4) / x
    }.toMath("(x^2 - 4)/x")

    DialogSequence(
        BoundedReadDialog(Int::class.java, "solve_method", 1, 5,
            "1) Метод левых прямоугольников \n2) Метод правых прямоугольников \n" +
                    "3) Метод средних прямоугольников \n4) Метод трапеции \n5) Метод Симпсона"),
        BoundedReadDialog(Int::class.java, "solve_integral", 1, 3, "1) $func1 \n2) $func2 \n3) $func3"),
        SayDialog("Введите: <левая граница> <правая граница> <точность>"),
        ReadDialog(Double::class.java, "solve_a"),
        ReadDialog(Double::class.java, "solve_b"),
        ReadDialog(Double::class.java, "solve_accuracy"),
        CustomDialog { context ->
            val a: Double = context.get("solve_a")
            val b: Double = context.get("solve_b")
            val solveMethod: IntegralSolveMethod = when(context.get<Int>("solve_method")) {
                1 -> LeftRectSolveMethod(a, b, context.get("solve_accuracy"))
                2 -> RightRectSolveMethod(a, b, context.get("solve_accuracy"))
                3 -> MiddleRectSolveMethod(a, b, context.get("solve_accuracy"))
                4 -> TrapezeSolveMethod(a, b, context.get("solve_accuracy"))
                5 -> SimpsonSolveMethod(a, b, context.get("solve_accuracy"))
                else -> throw DialogException()
            }
            val function = when(context.get<Int>("solve_integral")) {
                1 -> func1
                2 -> func2
                3 -> func3
                else -> throw DialogException()
            }
            println(solveMethod.solve(function))
            Charts.draw(function, a, b)
        }
    ).play(DialogContextImpl(System.`in`, System.out))
}
