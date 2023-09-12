package Equation.SetEquation.System;

import Equation.Model.Interface.SystemEquation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

public class firstSystemEquation implements SystemEquation {
    private String equations = "2x + 3y^2 = 0 \n 3x^2 + 4y - 3 = 0";
    @Override
    public double FxAt(double x, double y) {
        return 2 * x + 3 * Math.pow(x, 2);
    }

    @Override
    public double GxAt(double x, double y) {
        return 3 * Math.pow(x, 2) + 4 * y - 3;
    }

    @Override
    public double derivativeFxForX(double x, double y) {
        return 2;
    }

    @Override
    public double derivativeFxForY(double x, double y) {
        return 6 * y;
    }

    @Override
    public double derivativeGxForX(double x, double y) {
        return 6*x;
    }

    @Override
    public double derivativeGxForY(double x, double y) {
        return 4;
    }

    @Override
    public String getSystemEquation() {
        return equations;
    }

    @Override
    public void addFToSeries(XYSeries series,  double x) {
        if(x < 0) series.add(x, Math.sqrt(-2 * x / 3));
        else series.add(-x, -Math.sqrt(2 * x / 3));
    }

    @Override
    public void addGToSeries(XYSeries series, double x) {
        series.add (x,(3 - 3 * Math.pow(x, 2)) / 4);
    }

    @Override
    public XYSeriesCollection makeDataset(XYSeries series_1, XYSeries series_2) {
        for (double i = -5; i < 5; i += 0.01) {
            addFToSeries(series_1, i);
            addGToSeries(series_2, i);
        }
        final XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(series_1);
        dataset.addSeries(series_2);

        return dataset;
    }
}
