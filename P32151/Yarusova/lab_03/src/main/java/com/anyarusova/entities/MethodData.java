package com.anyarusova.entities;

import java.util.function.Function;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
public class MethodData {
    private final Function<Double, Double> equation;
    private final double a;
    private final double b;
    private final double epsilon;
    private int n;
}
