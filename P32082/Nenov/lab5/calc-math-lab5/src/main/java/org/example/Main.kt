package org.example

import org.example.math.interpolation.GaussInterpolation
import org.example.math.interpolation.LagrangeInterpolation
import org.example.math.interpolation.Node
import org.knowm.xchart.XYChartBuilder
import java.awt.Color
import java.io.FileInputStream
import java.io.InputStream
import java.util.Scanner
import kotlin.math.pow

fun main() {
    println("Введите \n1: для ввода точек таблицей с консоли, " +
            "\n2: для ввода таблицей с файла, \n3: для ввода промежутком функции")
    val input = readln()
    val x: List<Double>?
    val y: List<Double>?
    if (input == "1") {
       try {
           val (tmpX, tmpY) = readTable(System.`in`)
           x = tmpX
           y = tmpY
       } catch (e: Exception) {
           println("Что-то пошло не так")
           return
       }
    } else if (input == "2") {
        println("Введите имя файла")
        try {
            val (tmpX, tmpY) = readTable(FileInputStream(readln()))
            x = tmpX
            y = tmpY
        } catch (e: Exception) {
            println("Что-то пошло не так")
            return
        }
    } else if (input == "3") {
        println("Выберите функцию: \n1: x^3 - (x/2)^4 + 5 \n2: 2^(0.3*x) - x/3 + 2")
        val funcNum = readln()
        println("Введите границы исследуемого интервала и шаг через пробел")
        val (start, end, h) = readln().split(" ").map { it.toDoubleOrNull() }
        if (start == null || end == null || h == null || h < 0 || end < start) {
            println("Некорректные исходные данные")
            return
        }
        x = List(((end-start) / h).toInt()) { i -> start+i*h }
        if (funcNum == "1")
            y = List(x.size) { i -> x[i].pow(3) - (x[i]/2).pow(4) + 5 }
        else if (funcNum == "2")
            y = List(x.size) { i -> 2.0.pow(0.3*x[i])-x[i]/3+2 }
        else {
            println("Некорректные исходные данные")
            return
        }
    } else {
        println("некорректный ввод")
        return
    }

    val table = x.mapIndexed { i, it ->  Node(it, y[i]) }
    val lagrangeInterp = LagrangeInterpolation(table)
    val gaussInterp = GaussInterpolation(table)

    println("Таблица конечных разностей")
    println(gaussInterp.dyTable)

    XYChartBuilder()
        .width(800)
        .height(600)
        .title("График")
        .xAxisTitle("X")
        .yAxisTitle("Y")
        .build()
        .drawFunction(x.first(), x.last(), 50, "Многочлен Лагранжа",
            6f, Color.ORANGE) { lagrangeInterp.interpolate(it) }
        .drawFunction(x.first(), x.last(), 50, "Многочлен Гаусса",
            2f, Color.BLUE
        ) { gaussInterp.interpolate(it) }
        .drawSeries(Series(x, y), "Точки")
        .show()
}

fun readTable(stream: InputStream): Pair<List<Double>, List<Double>> {
    print("Введите координаты x: ")
    val scanner = Scanner(stream)
    val xStr = scanner.nextLine().split(" ", ", ")
    val x = xStr.mapNotNull { it.toDoubleOrNull() }.toList()
    print("Введите координаты y: ")
    val yStr = scanner.nextLine().split(" ", ", ")
    val y = yStr.mapNotNull { it.toDoubleOrNull() }.toList()
    println()
    if (x.size != xStr.size || y.size != yStr.size || y.size != x.size) {
        println("Некорректные данные!")
        throw IllegalArgumentException()
    }
    return Pair(x, y)
}