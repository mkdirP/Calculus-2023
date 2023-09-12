package org.example.math.approx

import kotlin.math.pow
import kotlin.math.sqrt

abstract class Approximation(x: Array<Double>, y: Array<Double>) {
    abstract val name: String
    abstract val ratios: Array<Double>

    abstract fun approximate(x: Double): Double

    val deviations by lazy {
        x.mapIndexed() { i, it ->
            (approximate(it) - y[i]).pow(2)
        }
    }

    val standardDeviation: Double by lazy {
       sqrt(deviations.sum() / x.size)
    }
}