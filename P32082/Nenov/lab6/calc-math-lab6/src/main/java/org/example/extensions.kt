package org.example

import org.example.math.ODUSolveMethod
import org.knowm.xchart.SwingWrapper
import org.knowm.xchart.XYChart
import org.knowm.xchart.XYChartBuilder
import org.knowm.xchart.XYSeries
import org.knowm.xchart.style.markers.SeriesMarkers
import java.awt.BasicStroke
import java.awt.Color
import java.util.ArrayList
import kotlin.math.max
import kotlin.text.StringBuilder

data class Series(val x: List<Double>, val y: List<Double>)

fun XYChartBuilder.buildDefault(label: String = "График") = this.width(800)
    .height(600)
    .title(label)
    .xAxisTitle("X")
    .yAxisTitle("Y")
    .build()!!

fun XYChart.drawSeries(series: Series, label: String) : XYChart {
    val chartSeries: XYSeries = this.addSeries(label, series.x.toDoubleArray(), series.y.toDoubleArray())
    chartSeries.lineStyle = BasicStroke(0f)
    chartSeries.marker = SeriesMarkers.DIAMOND
    return this
}

fun XYChart.drawConnectedSeries(series: Series, label: String, color: Color? = null) : XYChart {
    val chartSeries: XYSeries = this.addSeries(label, series.x.toDoubleArray(), series.y.toDoubleArray())
    chartSeries.marker = SeriesMarkers.NONE
    if (color != null)
        chartSeries.lineColor = color
    return this
}

fun XYChart.drawFunction(x: Array<Double>, label: String, func: (x: Double) -> Double) : XYChart {
    val y = x.map { func(it) }
    val chartSeries: XYSeries = this.addSeries(label, x.toDoubleArray(), y.toDoubleArray())
    chartSeries.marker = SeriesMarkers.NONE
    return this
}

fun XYChart.drawFunction(start: Double, end: Double, step: Double, label: String,
                         thickness: Float, color: Color, func: (x: Double) -> Double) : XYChart {
    val x = Array(((end-start)/step).toInt()+1) { i -> start + step*i }
    val y = x.map { func(it) }
    val chartSeries: XYSeries = this.addSeries(label, x.toDoubleArray(), y.toDoubleArray())
    chartSeries.marker = SeriesMarkers.NONE
    chartSeries.lineWidth = thickness
    chartSeries.lineColor = color
    return this
}

fun List<XYChart>.show() {
    if (isEmpty())
        return
    SwingWrapper(this).displayChartMatrix()
}

fun XYChart.show() {
    SwingWrapper(this).displayChart()
}

fun Iterable<Double>.roundedContentToString(scale: Int): String {
    val sb = StringBuilder()
    sb.append("{ ")
    this.forEach {
        sb.append("%.${scale}f, ".format(it))
    }
    sb.deleteRange(sb.length-2, sb.length-1)
    sb.append("}")
    return sb.toString().format()
}

fun Int.factorial() : Int = (2..this).fold(1) { acc, it -> acc * it }

fun Double.fixedLengthStr(n: Int) : String {
    val length = this.toString().split(".")[0].length
    return "%.${max(0,n-length-1)}f".format(this)
}

fun ODUSolveMethod.interval() : List<Double> {
    val values = ArrayList<Double>()
    var x = start
    while (x < end+h/2) {
        values.add(x)
        x += h
    }
    return values
}

fun ODUSolveMethod.table(df: (Double) -> Double) : String {
    val xs = this.interval()
    return StringBuilder()
        .apply {
            append('\n')
            append(name)
            append('\n')
            repeat(21+name.length) { append('-') }
            append('\n')
        }
        .append("i    ")
        .append("x       ")
        .append("y       ")
        .append("$name    ")
        .append('\n')
        .apply {
            xs.forEachIndexed { i, x ->
                append(i)
                repeat(5-i.toString().length) { append(' ') }
                append(x.fixedLengthStr(6))
                append("  ")
                append(df(x).fixedLengthStr(6))
                append("  ")
                append(result[i].fixedLengthStr(6))
                append('\n')
            }
        }
        .toString()
}