package org.example

import org.example.math.Function
import org.knowm.xchart.SwingWrapper
import org.knowm.xchart.XYChart
import org.knowm.xchart.XYSeries
import org.knowm.xchart.style.markers.SeriesMarkers
import java.awt.BasicStroke
import java.lang.StringBuilder
import kotlin.math.abs
import kotlin.math.absoluteValue

fun ((x: Double) -> Double).toMath(asString: String = "<Unnamed Function>") = object : Function() {
    override fun calculate(x: Double): Double = this@toMath(x)
    override fun toString(): String = asString
}

data class Series(val x: Array<Double>, val y: Array<Double>)

fun XYChart.drawSeries(series: Series, label: String) : XYChart {
    val chartSeries: XYSeries = this.addSeries(label, series.x.toDoubleArray(), series.y.toDoubleArray())
    chartSeries.lineStyle = BasicStroke(0f)
    chartSeries.marker = SeriesMarkers.DIAMOND
    return this
}

fun XYChart.drawFunction(x: Array<Double>, func: (x: Double) -> Double, label: String) : XYChart {
    val y = x.map { func(it) }
    val chartSeries: XYSeries = this.addSeries(label, x.toDoubleArray(), y.toDoubleArray())
    chartSeries.marker = SeriesMarkers.NONE
    return this
}

fun XYChart.drawFunction(start: Double, end: Double, steps: Int, func: (x: Double) -> Double, label: String) : XYChart {
    val step = abs(end - start) / steps
    val x = Array(steps) { i -> start + step*i }
    val y = x.map { func(it) }
    val chartSeries: XYSeries = this.addSeries(label, x.toDoubleArray(), y.toDoubleArray())
    chartSeries.marker = SeriesMarkers.NONE
    return this
}

fun XYChart.show() {
    SwingWrapper(this).displayChart()
}

fun Array<Double>.roundedContentToString(scale: Int): String {
    val sb = StringBuilder()
    sb.append("{ ")
    this.forEach {
        sb.append("%.${scale}f, ".format(it))
    }
    sb.deleteRange(sb.length-2, sb.length-1)
    sb.append("}")
    return sb.toString().format()
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