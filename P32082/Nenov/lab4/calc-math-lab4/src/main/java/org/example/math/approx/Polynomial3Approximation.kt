package org.example.math.approx

import org.example.math.slau.NewtonSolveMethod
import kotlin.math.pow

class Polynomial3Approximation(x: Array<Double>, y: Array<Double>) : Approximation(x, y) {
    override val name: String = "Аппроксимация полиномом 3 степени"

    override val ratios: Array<Double> by lazy {
        var xSum = 0.0
        var xSqSum = 0.0
        var xPow3Sum = 0.0
        var xPow4Sum = 0.0
        var xPow5Sum = 0.0
        var xPow6Sum = 0.0
        var xySum = 0.0
        var xSqYSum = 0.0
        var xPow3YSum = 0.0
        x.forEachIndexed { index, x ->
            xSum += x
            xSqSum += x.pow(2)
            xPow3Sum += x.pow(3)
            xPow4Sum += x.pow(4)
            xPow5Sum += x.pow(5)
            xPow6Sum += x.pow(6)
            xySum += x*y[index]
            xSqYSum += x.pow(2)*y[index]
            xPow3YSum += x.pow(3)*y[index]
        }
        val lMatrix = arrayOf(
            doubleArrayOf(x.size.toDouble(), xSum, xSqSum, xPow3Sum),
            doubleArrayOf(xSum, xSqSum, xPow3Sum, xPow4Sum),
            doubleArrayOf(xSqSum, xPow3Sum, xPow4Sum, xPow5Sum),
            doubleArrayOf(xPow3Sum, xPow4Sum, xPow5Sum, xPow6Sum),
        )
        val rMatrix = arrayOf(y.sum(), xySum, xSqYSum, xPow3YSum)
        NewtonSolveMethod(lMatrix, rMatrix).solve()
    }

    override fun approximate(x: Double): Double {
        return ratios[0] + ratios[1]*x + ratios[2]*x.pow(2) + ratios[3]*x.pow(3)
    }
}