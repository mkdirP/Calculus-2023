package org.example.math.approx

import kotlin.math.exp
import kotlin.math.ln

class LogApproximation(x: Array<Double>, y: Array<Double>) : Approximation(x, y) {
    override val name: String = "Логарифмическая аппроксимация"

    override val ratios: Array<Double> by lazy {
        val approx = LinearApproximation(x.map { ln(it) }.toTypedArray(), y)
        arrayOf(approx.ratios[1], approx.ratios[0])
    }

    override fun approximate(x: Double): Double = ratios[0] * ln(x) + ratios[1]
}