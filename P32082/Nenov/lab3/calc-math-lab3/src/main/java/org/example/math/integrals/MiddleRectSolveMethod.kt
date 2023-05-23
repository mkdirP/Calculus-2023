package org.example.math.integrals

import org.example.math.Function

class MiddleRectSolveMethod(leftBound: Double, rightBound: Double, accuracy: Double)
    : IntegralSolveMethod(leftBound, rightBound, accuracy)
{
    override val k: Int = 2

    override fun calculate(func: Function, parts: Int): Double {
        val h: Double = (rightBound-leftBound) / parts
        var result = 0.0
        for (i in 0 until parts) {
            result += func.calculate(leftBound+i*h+h/2)
        }
        return result*h
    }
}