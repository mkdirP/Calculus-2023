package org.example.math.integrals

import org.example.math.Function

class TrapezeSolveMethod(leftBound: Double, rightBound: Double, accuracy: Double)
    : IntegralSolveMethod(leftBound, rightBound, accuracy)
{
    override val k: Int = 2

    override fun calculate(func: Function, parts: Int): Double {
        val h: Double = (rightBound-leftBound) / parts
        var sum = 0.0
        for (i in 1 until parts) {
            sum += func.calculate(leftBound+i*h)
        }
        return (2*sum+leftBound+rightBound) * h/2
    }
}