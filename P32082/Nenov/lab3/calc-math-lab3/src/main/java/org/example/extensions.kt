package org.example

import org.example.dialog_sytem.DialogContext
import org.example.dialog_sytem.DialogElement
import org.example.math.Function

fun ((x: Double) -> Double).toMath(asString: String = "<Unnamed Function>") = object : Function() {
    override fun calculate(x: Double): Double = this@toMath(x)
    override fun toString(): String = asString
}

fun DialogElement.play(context: DialogContext) {
    try {
        this.play(context)
    } catch (e: Exception) {
        e.printStackTrace()
    }
    context.destroy()
}