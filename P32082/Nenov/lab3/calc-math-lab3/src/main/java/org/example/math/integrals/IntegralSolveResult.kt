package org.example.math.integrals

data class IntegralSolveResult(val value: Double, val parts: Int) {
    override fun toString() = String.format("Значение интеграла: %.4f\nС разбиением интервала на %d частей", value, parts)
}

