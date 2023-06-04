package org.example.math.slau

import kotlin.math.absoluteValue

fun <T> Array<T>.swap(i: Int, j: Int) {
    val tmp = this[i]
    this[i] = this[j]
    this[j] = tmp
}

class NewtonSolveMethod(private val a: Array<DoubleArray>, private val b: Array<Double>) {
    fun solve() : Array<Double> {
        if (a.isEmpty() || a.size != a[0].size || a.size != b.size)
            throw IllegalArgumentException("incorrect matrix size")
        for (i in 1 until a.size) {
            swapToMaxRow(i)
            for (j in i until a.size) {
                val k = -(a[j][i-1]/a[i-1][i-1])
                a[i-1] = a[i-1].map { it ->
                    it * k
                }.toDoubleArray()
                b[i-1] *= k
                a[j] = a[j].mapIndexed { ii, it ->
                    it + a[i-1][ii]
                }.toDoubleArray()
                b[j] += b[i-1]
            }
        }
        val result = Array(b.size) {0.0}
        for (i in result.indices) {
            val ii = b.size-1-i
            var s = 0.0
            result.slice(0 until i).forEachIndexed { j, it ->
                s += it * a[b.size-1-i][b.size-1-j]
            }
            result[i] = (b[ii]-s)/a[ii][ii]
        }
        result.reverse()
        return result
    }

    private fun swapToMaxRow(i: Int) {
        val maxInd = a.slice(i - 1 until a.size).foldIndexed(i - 1) { ii, acc, it ->
            val toCompare = a[acc][i - 1]
            if (it[i - 1].absoluteValue > toCompare.absoluteValue)
                ii
            else
                acc
        }
        a.swap(maxInd, i - 1)
        b.swap(maxInd, i - 1)
    }
}