package org.example;

import org.example.math.Function;
import org.example.math.systems.MultiArgFunction;
import org.knowm.xchart.SwingWrapper;
import org.knowm.xchart.XYChart;
import org.knowm.xchart.XYChartBuilder;
import org.knowm.xchart.XYSeries;
import org.knowm.xchart.style.Styler;
import org.knowm.xchart.style.markers.Marker;
import org.knowm.xchart.style.markers.SeriesMarkers;

import java.awt.*;
import java.util.ArrayList;
import java.util.List;

import static java.lang.Double.NaN;

public class Charts {
    public static void draw(Function function, double lBound, double rBound) {
        double step = Math.abs(rBound-lBound) / 100;
        double current = lBound;
        List<Double> xData = new ArrayList<>();
        List<Double> yData = new ArrayList<>();
        while (current <= rBound) {
            xData.add(current);
            yData.add(function.calculate(current));
            current += step;
        }
        // Chart look
        XYChart chart = new XYChartBuilder()
                .width(800)
                .height(600)
                .title("График")
                .xAxisTitle("X")
                .yAxisTitle("Y")
//                .theme(Styler.ChartTheme.Matlab)
                .build();
        chart.getStyler().setDefaultSeriesRenderStyle(XYSeries.XYSeriesRenderStyle.Area);
        // X axios
        XYSeries xAxios = chart.addSeries("x axios",
                new double[] {lBound-lBound*0.1, rBound+rBound*0.1}, new double[] {0, 0});
        xAxios.setShowInLegend(false);
        xAxios.setLineColor(Color.WHITE);
        xAxios.setMarker(SeriesMarkers.NONE);
        // Function
        XYSeries series = chart.addSeries(function.toString(), xData, yData);
        series.setMarker(SeriesMarkers.NONE);
        new SwingWrapper<>(chart).displayChart();
    }

    public static void drawSystem(MultiArgFunction[] system, double centerX, double centerY) {
        XYChart chart = new XYChartBuilder()
                .width(800)
                .height(600)
                .title("График")
                .xAxisTitle("X")
                .yAxisTitle("Y")
                .theme(Styler.ChartTheme.Matlab)
                .build();
        drawFuncOfMultArgs(chart, centerX, centerY, new MultiArgFunction() {
            @Override
            public double calculate(double... x) {
                return system[0].calculate(x)-x[0];
            }

            @Override
            public String toString() {
                return system[0].toString();
            }
        });
        drawFuncOfMultArgs(chart, centerX, centerY, new MultiArgFunction() {
            @Override
            public double calculate(double... x) {
                return system[1].calculate(x)-x[1];
            }

            @Override
            public String toString() {
                return system[1].toString();
            }
        });
        new SwingWrapper<>(chart).displayChart();
    }

    private static void drawFuncOfMultArgs(XYChart chart, double centerX, double centerY, MultiArgFunction f) {
        List<Double> xData = new ArrayList<>();
        List<Double> yData = new ArrayList<>();
        double step = 0.05;
        for (double x = centerX - 5; x < centerX + 5; x+=step) {
            double last = NaN;
            for (double y = centerY - 5; y < centerY + 5; y+=step) {
                if (!Double.isNaN(last) && f.calculate(x, y) * last < 0) {
                    xData.add(x);
                    yData.add(y);
                }
                last = f.calculate(x, y);
            }
        }
        for (double y = centerY - 5; y < centerY + 5; y+=step) {
            double last = NaN;
            for (double x = centerX - 5; x < centerX + 5; x+=step) {
                if (!Double.isNaN(last) && f.calculate(x, y) * last < 0) {
                    xData.add(x);
                    yData.add(y);
                }
                last = f.calculate(x, y);
            }
        }

        chart.getStyler().setDefaultSeriesRenderStyle(XYSeries.XYSeriesRenderStyle.Scatter);
        XYSeries series = chart.addSeries(f.toString(), xData, yData);
        series.setMarker(SeriesMarkers.CIRCLE);
    }

}
