package org.example.math

import java.util.LinkedList
import kotlin.math.absoluteValue
import kotlin.math.pow

class AdamsODUSolveMethod(
    start: Double,
    end: Double,
    y0: Double,
    func: (x: Double, y: Double) -> Double,
    h: Double,
    eps: Double,
    private val exactFunc: (x: Double) -> Double
) : ODUSolveMethod(start, end, y0, func, h, eps) {

    private var rungeKuttaSolver = RungeKuttaODUSolveMethod(start, start+h*4, y0, func, h, eps)
    private val fs = LinkedList<Double>()
    override val name: String = "Метод Адамса"

    override fun calculateNext(calculated: List<Double>, h: Double, x: Double): Double {
        if (calculated.size < 4) {
            val fi = func(x, rungeKuttaSolver.result[calculated.size])
            fs.add(fi)
            return rungeKuttaSolver.result[calculated.size]
        }
        val dfi = fs[fs.size-1] - fs[fs.size-2]
        val ddfi = fs[fs.size-1] - 2*fs[fs.size-2] + fs[fs.size-3]
        val dddfi = fs[fs.size-1] - 3*fs[fs.size-2] + 3*fs[fs.size-3] - fs[fs.size-4]
        val yi = calculated.last() + h*fs.last() + h.pow(2)/2*dfi + 5*h.pow(3)/12*ddfi + 3*h.pow(4)/8*dddfi
        fs.removeFirst()
        fs.add(func(x, yi))
        return yi
    }

    override fun onCalculateStart() {
        super.onCalculateStart()
        fs.clear()
        fs.add(func(start, y0))
        rungeKuttaSolver.calculate()
    }

    override fun onMethodReload() {
        super.onMethodReload()
        rungeKuttaSolver = RungeKuttaODUSolveMethod(start, start+h*4, y0, func, h, eps)
    }

    override fun checkError(calculated: List<Double>, h: Double, x: Double): Boolean {
        return (calculated.last()-exactFunc(x)).absoluteValue <= eps
    }
}