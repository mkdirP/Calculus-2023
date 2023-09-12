package org.example.math.approx

import org.example.math.slau.NewtonSolveMethod
import kotlin.math.exp
import kotlin.math.pow
import kotlin.math.sqrt

class LinearApproximation( x: Array<Double>, y: Array<Double>) : Approximation(x, y) {
    override val name: String = "Линейная аппроксимация"

    override val ratios: Array<Double> by lazy {
        val xSqSum = x.reduce { acc, it ->
            acc + it*it
        }
        val xy = Array(x.size) { i ->
            x[i]*y[i]
        }
        val matrix = arrayOf(
            doubleArrayOf(xSqSum, x.sum()),
            doubleArrayOf(x.sum(), x.size.toDouble())
        )
        NewtonSolveMethod(matrix, arrayOf(xy.sum(), y.sum())).solve()
    }

    val correlationRatio: Double by lazy {
        val xMean = x.sum() / x.size
        val yMean = y.sum() / y.size
        var a = 0.0
        var b = 0.0
        var c = 0.0
        for (i in x.indices) {
            a += (x[i] - xMean)*(y[i] - yMean)
            b += (x[i] - xMean).pow(2)
            c += (y[i] - yMean).pow(2)
        }
        a / sqrt(b*c)
    }

    override fun approximate(x: Double) : Double = ratios[0]*x + ratios[1]

}