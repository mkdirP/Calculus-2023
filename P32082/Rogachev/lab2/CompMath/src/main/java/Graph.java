import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartUtils;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.io.File;
import java.io.IOException;

public class Graph {
    public void drawFunction(double a, double b, int n, int m){
        XYSeriesCollection lineDataset = new XYSeriesCollection ();
        XYSeries series = new XYSeries("Function");

        a -= 1;
        b += 1;

        for (double i = a; i <= b; i += (b - a) / 50) {
            series.add(i, Function.getFunction(i, n));
        }

        XYSeries border = new XYSeries("Border");
        border.add(a,0);
        border.add(b,0);

        if (m == 5) {
            XYSeries line = new XYSeries("Line");
            for (double i = a; i <= b; i += (b - a) / 50) {
                line.add(i, Function.getFiFunction(i, a, b, n));
            }
            lineDataset.addSeries(line);
            XYSeries line1 = new XYSeries("X=Y");
            for (double i = a; i <= b; i += (b - a) / 50) {
                line1.add(i, i);
            }
            lineDataset.addSeries(line1);
        }

        lineDataset.addSeries(series);
        lineDataset.addSeries(border);

        drawChart(lineDataset, n);
    }

    public void drawChart(XYSeriesCollection seriesCollection, int n) {
        JFreeChart lineChart = ChartFactory.createXYLineChart(
                "f(x)", "x",
                "y",
                seriesCollection, PlotOrientation.VERTICAL,
                false, true, false);

        try {
            ChartUtils.saveChartAsJPEG(new File("src/main/resources/Chart" + n + ".jpeg"), lineChart, 1920, 1080);
        } catch (IOException e) {
            System.out.println("Не удалось сохранить график");
        }
    }

    public void drawTwoFunction(int n){
        XYSeriesCollection lineDataset = new XYSeriesCollection ();
        XYSeries series1 = new XYSeries("FunctionUp");
        XYSeries series2 = new XYSeries("FunctionDown");

        double r;

        if (n == 1) {
            r = 2;
        } else {
            r = 1;
        }

        for (double i = -r; i <= r; i += r / 50.0) {
            series1.add(i, Math.sqrt(r * r - i * i));
        }
        series1.add(r, 0);
        for (double i = r; i >= -r; i -= r / 50.0) {
            series2.add(i, -Math.sqrt(r * r - i * i));
        }
        series2.add(-r, 0);

        XYSeries border = new XYSeries("Border");
        border.add(-r - 1,0);
        border.add(r + 1,0);

        XYSeries line = new XYSeries("Line");

        if (n == 1) {
            for (double i = -r - 1; i <= r + 1; i += r / 25) {
                line.add(i, 3 * i * i);
            }
        } else {
            for (double i = -r - 1; i <= r + 1; i += r / 25) {
                line.add(i, i);
            }
        }

        lineDataset.addSeries(series1);
        lineDataset.addSeries(series2);
        lineDataset.addSeries(border);
        lineDataset.addSeries(line);

        drawChart(lineDataset, 6);
    }
}
