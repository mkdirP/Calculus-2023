package org.example.math.approx

import org.example.math.slau.NewtonSolveMethod
import kotlin.math.pow

class Polynomial2Approximation(x: Array<Double>, y: Array<Double>) : Approximation(x, y) {
    override val name: String = "Аппроксимация полиномом 2 степени"

    override val ratios: Array<Double> by lazy {
        val xSqSum = x.reduce { acc, it ->
            acc + it*it
        }
        val xPow3Sum = x.reduce { acc, it ->
            acc + it*it*it
        }
        val xPow4Sum = x.reduce { acc, it ->
            acc + it*it*it*it
        }
        val xySum = Array(x.size) { i ->
            x[i]*y[i]
        }.sum()
        val xSqYSum = Array(x.size) { i ->
            x[i]*x[i]*y[i]
        }.sum()
        val xSum = x.sum()
        val matrix = arrayOf(
            doubleArrayOf(x.size.toDouble(), xSum, xSqSum),
            doubleArrayOf(xSum, xSqSum, xPow3Sum),
            doubleArrayOf(xSqSum, xPow3Sum, xPow4Sum)
        )

        NewtonSolveMethod(matrix, arrayOf(y.sum(), xySum, xSqYSum)).solve()
    }

    override fun approximate(x: Double): Double {
        return ratios[0] + ratios[1]*x + ratios[2]*x.pow(2)
    }
}