package Equation.SetEquation.System;

import Equation.Model.Interface.SystemEquation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

public class secondSystemEquation implements SystemEquation {
    private String equations = "x^2 + y^2 - 4 = 0 \n -3x^2 + y = 0";
    @Override
    public double FxAt(double x, double y) {
        return x*x + y*y - 4;
    }

    @Override
    public double GxAt(double x, double y) {
        return -3*x*x + y;
    }

    @Override
    public double derivativeFxForX(double x, double y) {
        return 2*x;
    }

    @Override
    public double derivativeFxForY(double x, double y) {
        return 2 * y;
    }

    @Override
    public double derivativeGxForX(double x, double y) {
        return -6*x;
    }

    @Override
    public double derivativeGxForY(double x, double y) {
        return 1;
    }

    @Override
    public String getSystemEquation() {
        return equations;
    }

    @Override
    public void addFToSeries(XYSeries series, double x) {
        if(4>= x*x) {
            series.add(x, Math.sqrt(4 - x * x));
        }
        if(x > 2) {
            x = 4 - x;
            series.add(x, -Math.sqrt(4 - x * x));
        }
    }

    @Override
    public void addGToSeries(XYSeries series, double x) {
        series.add (x,3*x*x);
    }

    @Override
    public XYSeriesCollection makeDataset(XYSeries series_1, XYSeries series_2) {
        for (double i = -2; i < 6; i += 0.01) {
            addFToSeries(series_1, i);
            addGToSeries(series_2, i);
        }
        final XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(series_1);
        dataset.addSeries(series_2);

        return dataset;
    }
}
