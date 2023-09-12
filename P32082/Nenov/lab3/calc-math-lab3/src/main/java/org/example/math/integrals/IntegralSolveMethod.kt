package org.example.math.integrals

import kotlin.math.pow
import org.example.math.Function

const val START_N_PARTS = 4
const val MAX_N_STEPS = 1024

abstract class IntegralSolveMethod(val leftBound: Double, val rightBound: Double, private val accuracy: Double) {
    protected abstract val k: Int

    abstract fun calculate(func: Function, parts: Int) : Double

    fun solve(func: Function) : IntegralSolveResult{
        var n = START_N_PARTS
        do {
            val result2 = calculate(func, n)
            val result1 = calculate(func, n*2)
            n *= 2
        } while ((result2 - result1)/(2.0.pow(k) - 1) > accuracy && n < MAX_N_STEPS*2)
        return IntegralSolveResult(calculate(func, n/2), n/2)
    }
}