package org.example.math.integrals

import org.example.math.Function

class SimpsonSolveMethod(leftBound: Double, rightBound: Double, accuracy: Double)
    : IntegralSolveMethod(leftBound, rightBound, accuracy)
{
    override val k: Int = 4

    override fun calculate(func: Function, parts: Int): Double {
        val h: Double = (rightBound-leftBound) / parts
        var sum = func.calculate(leftBound) + func.calculate(rightBound)
        for (i in 1 until parts step 2) {
            sum += 4*func.calculate(leftBound+h*i)
        }
        for (i in 2 until parts step 2) {
            sum += 2*func.calculate(leftBound+h*i)
        }
        return sum * h/3
    }
}