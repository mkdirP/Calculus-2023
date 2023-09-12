package org.example.math.interpolation

import kotlin.math.absoluteValue

class LagrangeInterpolation(nodes: List<Node>) : Interpolation {
    private val nodes = List(nodes.size) { i ->
        if (i>0 && nodes[i-1].x == nodes[i].x)
            return@List nodes[i].copy(x=nodes[i].x+0.001)
        nodes[i]
    }
    override fun interpolate(x: Double) : Double {
        var result = 0.0
        nodes.forEach { inode ->
            var num = 1.0
            var den = 1.0
            nodes.forEach { jnode ->
                if (inode != jnode) {
                    num *= (x-jnode.x)
                    den *= (inode.x-jnode.x)
                }
            }
            result += inode.y * num / den
        }
        return result
    }
}