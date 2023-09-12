package org.example.math

import java.util.ArrayList

const val MAX_ITERATIONS = 10_000

abstract class ODUSolveMethod(val start: Double, val end: Double, val y0: Double, val func: (x: Double, y: Double) -> Double,
                              var h: Double, val eps: Double) {
    val result = ArrayList<Double>()
    abstract val name: String

    fun calculate() {
        var iters = 0
        while (result.size < (end-start)/h && iters < MAX_ITERATIONS) {
            onCalculateStart()
            var x = start+h
            while (x < end+h/2 && iters < MAX_ITERATIONS) {
                result.add(calculateNext(result, h, x))
                iters++
                if (!checkError(result, h, x)) {
                    onMethodReload()
                    break
                }
                x += h
            }
        }
        if (iters >= MAX_ITERATIONS)
            throw IllegalArgumentException()
    }

    protected open fun onCalculateStart() {
        result.clear()
        result.add(y0)
    }
    protected open fun onMethodReload() { h /= 2 }
    protected abstract fun calculateNext(calculated: List<Double>, h: Double, x: Double) : Double
    protected abstract fun checkError(calculated: List<Double>, h: Double, x: Double) : Boolean
}