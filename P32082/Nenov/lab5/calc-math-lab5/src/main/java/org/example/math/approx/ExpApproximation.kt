package org.example.math.approx

import kotlin.math.exp
import kotlin.math.ln
import kotlin.math.pow

class ExpApproximation(x: Array<Double>, y: Array<Double>) : Approximation(x, y) {
    override val name: String = "Экспоненциальная аппроксимация"

    override val ratios: Array<Double> by lazy {
        val approx = LinearApproximation(x, y.map { ln(it) }.toTypedArray())
        arrayOf(exp(approx.ratios[1]), approx.ratios[0])
    }

    override fun approximate(x: Double): Double = ratios[0] * exp(ratios[1]*x)
}