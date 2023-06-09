package org.example.math.interpolation

import org.example.factorial
import org.example.fixedLengthStr
import java.lang.StringBuilder
import kotlin.math.absoluteValue

class GaussInterpolation(nodes: List<Node>) : Interpolation {
    private val nodes = (if (nodes.size % 2 == 0) nodes.subList(0, nodes.size-1) else nodes).mapIndexedNotNull { i, it ->
        if (i == 0)
            return@mapIndexedNotNull it
        if ((nodes[i].x-nodes[i-1].x).absoluteValue < 0.000001) return@mapIndexedNotNull null else nodes[i]
    }
    private val h = (nodes[1].x-nodes[0].x).absoluteValue

    private val dyList: List<List<Double>> by lazy {
        val result = ArrayList<List<Double>>()
        result.add(nodes.map { it.y })
        while (result.last().size > 1) {
            result.add(
                List(result.last().size-1) { i ->
                    result.last()[i + 1] - result.last()[i]
                }
            )
        }
        result.removeFirst()
        result
    }

    val dyTable : String get() {
        val sb = StringBuilder()
        dyList.forEachIndexed { i, dy ->
            sb.append("yΔ${i+1} | ")
            dy.forEach { y ->
                sb.append(y.fixedLengthStr(6))
                sb.append(" | ")
            }
            sb.append("\n")
        }
        return sb.toString()
    }

    override fun interpolate(x: Double): Double {
        val a = nodes[nodes.size/2]
        val t = (x-a.x)/h
        var tMult = t
        var result = a.y
        var diffT = if (x < a.x) 1.0 else -1.0
        dyList.forEachIndexed { i, dy ->
            val dyCenter = getDyCenter(dy, a, x)
            result += dyCenter * tMult / (i+1).factorial()
            tMult *= (t + diffT)
            diffT *= -1
            diffT = (diffT.absoluteValue+(i%2))*(diffT/diffT.absoluteValue)
        }
        return result
    }

    private fun getDyCenter(dy: List<Double>, a: Node, x: Double) : Double {
        if (x > a.x)
            return dy[dy.size/2]
        return if (dy.size > 1)
            dy[(dy.size/2) - (1-dy.size%2)]
        else dy[0]
    }

}