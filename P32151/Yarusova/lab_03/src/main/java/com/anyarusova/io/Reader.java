package com.anyarusova.io;

import java.util.function.Function;

public interface Reader {
    Function<Double, Double> chooseEquation();

    Function<Double, Double> chooseExtraEquation();

    int chooseMethod();

    double chooseEpsilon();

    double chooseLeftBound();

    double chooseRightBound();
}
