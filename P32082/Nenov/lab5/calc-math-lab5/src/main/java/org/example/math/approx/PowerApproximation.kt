package org.example.math.approx

import kotlin.math.exp
import kotlin.math.ln
import kotlin.math.pow

class PowerApproximation(x: Array<Double>, y: Array<Double>) : Approximation(x, y) {
    override val name: String = "Степенная аппроксимация"

    override val ratios: Array<Double> by lazy {
        val approx = LinearApproximation(
            x.map { ln(it) }.toTypedArray(),
            y.map { ln(it) }.toTypedArray()
        )
        arrayOf(exp(approx.ratios[0]), approx.ratios[1])
    }

    override fun approximate(x: Double): Double = ratios[0]*x.pow(ratios[1])
}