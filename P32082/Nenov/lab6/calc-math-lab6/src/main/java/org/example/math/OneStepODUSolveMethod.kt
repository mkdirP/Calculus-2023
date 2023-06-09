package org.example.math

import kotlin.math.absoluteValue
import kotlin.math.pow

abstract class OneStepODUSolveMethod(
    start: Double,
    end: Double,
    y0: Double,
    func: (x: Double, y: Double) -> Double,
    h: Double,
    eps: Double
) : ODUSolveMethod(start, end, y0, func, h, eps) {

    protected abstract val p: Double

    protected abstract fun calculateNext(yi: Double, h: Double, x: Double): Double

    override fun calculateNext(calculated: List<Double>, h: Double, x: Double) = calculateNext(calculated.last(), h, x)

    override fun checkError(calculated: List<Double>, h: Double, x: Double): Boolean {
        val y1 = calculated.last()
        val y2 = calculateNext(calculated[calculated.size-2], h/2, x)
        val k = (y1-y2).absoluteValue/(2.0.pow(p)-1)
        return k <= eps
    }
}