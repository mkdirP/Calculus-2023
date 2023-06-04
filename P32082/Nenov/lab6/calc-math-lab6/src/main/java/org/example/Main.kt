package org.example

import org.example.math.AdamsODUSolveMethod
import org.example.math.ModEulerODUSolveMethod
import org.example.math.RungeKuttaODUSolveMethod
import org.knowm.xchart.XYChartBuilder
import java.awt.Color
import kotlin.math.exp
import kotlin.math.ln
import kotlin.math.pow

fun main() {
    println("Выберите функцию: \n1: y' = y+(1+x)*y^2 \n2: y' = 3*x^2-y \n3: y' = 10^(x+y)")
    val funcNum = readln()
    println("Введите данные в порядке: <начало интервала> <конец интервала> <шаг> <точность>")
    val (start, end, h, e) = readln().split(" ").map { it.toDoubleOrNull() }
    if (start == null || end == null || h == null || e == null || h < 0 || end < start) {
        println("Некорректные исходные данные")
        return
    }
    print("Введите начальные условия дифференцирования y(x0)=")
    val y0 = readln().toDoubleOrNull()
    if (y0 == null) {
        println("Некорректные исходные данные")
        return
    }

    val f1 = { x: Double, y: Double -> y + (1.0+x)*y.pow(2) }
    val df1 = { x: Double -> -exp(x)/( x*exp(x) + y0+exp(start)/(start*exp(start)) ) }

    val f2 = { x: Double, y: Double -> 3*x.pow(2)-y }
    val df2 = { x: Double -> (y0-3*start.pow(2)+6*start-6)* exp(start) /exp(x) + 3*x.pow(2) - 6*x + 6 }

    val f3 = { x: Double, y: Double -> 10.0.pow(x+y) }
    val c3 = 1.0/exp(y0*ln(10.0)) + 10.0*start
    val df3 = { x: Double -> -ln(c3 - 10.0.pow(x))/ln(10.0) }

    val f = when (funcNum) {
        "1" -> f1
        "2" -> f2
        "3" -> f3
        else -> {
            println("Некорректные исходные данные")
            return
        }
    }
    val df = when (funcNum) {
        "1" -> df1
        "2" -> df2
        "3" -> df3
        else -> {
            println("Некорректные исходные данные")
            return
        }
    }

    val methods = listOf(
        ModEulerODUSolveMethod(start, end, y0, f, h, e),
        RungeKuttaODUSolveMethod(start, end, y0, f, h, e),
        AdamsODUSolveMethod(start, end, y0, f, h, e, df)
    )


    // 1 1.5 0.1 0.001
    // -2 2 0.1 0.05
    // 0 0.9 0.1 0.05
    methods.mapNotNull {
        try {
            it.calculate()
        } catch (e: IllegalArgumentException) {
            println("${it.name} не смог найти решения задачи!")
            return@mapNotNull null
        }
        println(it.table(df))
        XYChartBuilder()
            .buildDefault(it.name)
            .drawFunction(start, end, it.h, "Точное значение", 1.8f, Color.BLUE, df)
            .drawConnectedSeries(Series(it.interval(), it.result), "${it.name} (h=${it.h})", Color.RED)
    }.show()
}
