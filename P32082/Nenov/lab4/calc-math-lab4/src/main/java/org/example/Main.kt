package org.example

import org.example.math.approx.*
import org.knowm.xchart.XYChartBuilder
import kotlin.math.exp
import kotlin.math.ln
import kotlin.math.pow

fun main() {
//    val x = arrayOf(1.2, 2.9, 4.1, 5.5, 6.7, 7.8, 9.2, 10.3)
//    val y = arrayOf(7.4, 9.5, 11.1, 12.9, 14.6, 17.3, 18.2, 20.7)

    val x = doubleArrayOf(2.0, 4.0, 6.0, 8.0, 10.0).toTypedArray()
    val y = doubleArrayOf(2.5, 3.7, 4.1, 4.7, 5.4).toTypedArray()

//    f = 6x/(x^4 + 5)
//    val x = Array(11) { i -> 0.2*i+1 }
//    val y = Array(11) { i -> 6*x[i]/(x[i].pow(4)+5)}

//    print("Введите координаты x: ")
//    val xStr = readln().split(" ", ", ")
//    val x = xStr.mapNotNull { it.toDoubleOrNull() }.toTypedArray()
//    print("Введите координаты y: ")
//    val yStr = readln().split(" ", ", ")
//    val y = yStr.mapNotNull { it.toDoubleOrNull() }.toTypedArray()
//    println()

//    if (x.size != xStr.size || y.size != yStr.size || y.size != x.size) {
//        println("Некорректные данные!")
//        return
//    }

    val approximations : List<Approximation> = arrayOf(
//        LinearApproximation(x, y),
//        Polynomial2Approximation(x, y),
//        Polynomial3Approximation(x, y),
//        PowerApproximation(x, y),
//        ExpApproximation(x, y),
        LogApproximation(x, y)
    ).sortedBy { it.standardDeviation }

    approximations.forEach { approx ->
        println(approx.name)
        println("Среднеквадратичное отклонение: %.3f".format(approx.standardDeviation))
        if (approx is LinearApproximation)
            println("Коэффициент Пирса: %.3f".format(approx.correlationRatio))
        println("fi(X): ${x.map { approx.approximate(it) }.roundedContentToString(3)}")
        println("Отклонения: ${approx.deviations.roundedContentToString(3)}")
        println("Коэффициенты: ${approx.ratios.roundedContentToString(3)} \n")
    }

    XYChartBuilder()
        .width(800)
        .height(600)
        .title("График")
        .xAxisTitle("X")
        .yAxisTitle("Y")
        .build()
        .drawSeries(Series(x, y), "Точки")
        .drawFunction(x.first()-1, x.last()+1, 50,
            { approximations[0].approximate(it) }, approximations[0].name)
        .show()
}
