package Equation.Model.Interface;

import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

public interface SystemEquation {
    public double FxAt(double x, double y);
    public double GxAt(double x, double y);

    public double derivativeFxForX(double x, double y);
    public double derivativeFxForY(double x, double y);
    public double derivativeGxForX(double x, double y);
    public double derivativeGxForY(double x, double y);

    public String getSystemEquation();
    public void addFToSeries(XYSeries series, double x);
    public void addGToSeries(XYSeries series, double x);

    XYSeriesCollection makeDataset(XYSeries series_1, XYSeries series_2);

}
