package org.example.math

class ModEulerODUSolveMethod(
    start: Double,
    end: Double,
    y0: Double,
    func: (x: Double, y: Double) -> Double,
    h: Double,
    eps: Double
) : OneStepODUSolveMethod(start, end, y0, func, h, eps) {
    override val p: Double = 2.0
    override val name: String = "Модифицированный метод Эйлера"

    override fun calculateNext(yi: Double, h: Double, x: Double) : Double {
        val f = func(x-h, yi)
        return yi + h/2*(f + func(x, yi + h*f))
    }
}