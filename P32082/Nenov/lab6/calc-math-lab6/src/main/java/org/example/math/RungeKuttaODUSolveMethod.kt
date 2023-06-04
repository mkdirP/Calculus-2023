package org.example.math

class RungeKuttaODUSolveMethod(
    start: Double,
    end: Double,
    y0: Double,
    func: (x: Double, y: Double) -> Double,
    h: Double,
    eps: Double
) : OneStepODUSolveMethod(start, end, y0, func, h, eps) {
    override val p: Double = 4.0
    override val name: String = "Метод Рунге-Кутта"

    override fun calculateNext(yi: Double, h: Double, x: Double): Double {
        val xi = x-h
        val k1 = h*func(xi, yi)
        val k2 = h*func(xi+h/2, yi+k1/2)
        val k3 = h*func(xi+h/2, yi+k2/2)
        val k4 = h*func(xi+h, yi+k3)
        val r =  yi + 1.0/6.0*(k1 + 2*k2 + 2*k3 + k4)
        return r
    }
}