import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartUtils;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.io.File;
import java.io.IOException;

public class Chart {
    public static void draw(double[] y1, double[] y2, double x, double h) {
        XYSeriesCollection lineDataset = new XYSeriesCollection ();

        if (y1 == null || y2 == null) {
            return;
        }

        XYSeries series1 = new XYSeries("Приближенные");
        XYSeries series2 = new XYSeries("Точные");
        for (int i = 0; i < y1.length; i++) {
            series1.add(x, y1[i]);
            series2.add(x, y2[i]);
            x += h;
        }

        lineDataset.addSeries(series2);
        lineDataset.addSeries(series1);

        JFreeChart lineChart = ChartFactory.createXYLineChart(
                "f(x)", "x",
                "y",
                lineDataset, PlotOrientation.VERTICAL,
                true, true, false);

        try {
            ChartUtils.saveChartAsJPEG(new File("src/main/resources/charts.jpeg"), lineChart, 1920, 1080);
        } catch (IOException e) {
            System.out.println("Не удалось сохранить график");
        }
    }
}
