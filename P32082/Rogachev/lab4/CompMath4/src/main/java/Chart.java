import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartUtils;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;
public class Chart {
    public static void draw(ArrayList<Point> in, double[][] ans, int id) {
        XYSeriesCollection lineDataset = new XYSeriesCollection ();
        Algo[] val = Algo.values();

        double a = in.get(0).getX(), b = in.get(in.size() - 1).getX() + 1.0;
        /*XYSeries border = new XYSeries("y=0");
        border.add(a,0);
        border.add(b,0);

        lineDataset.addSeries(border);*/

        XYSeries series0 = new XYSeries("Начальные точки");
        for (Point point : in) {
            series0.add(point.getX(), point.getY());
        }

        XYSeriesCollection markerDataset = new XYSeriesCollection();
        markerDataset.addSeries(series0);



            XYSeries series = new XYSeries(val[id]);

            for (double j = a; j < b; j += (b - a) / 100.0) {
                double y = Function.getFunction(j, val[id], ans[id]);

                if (!Double.isInfinite(y)) {
                    series.add(j, y);
                }
            }

            lineDataset.addSeries(series);


        JFreeChart lineChart = ChartFactory.createXYLineChart(
                "f(x)", "x",
                "y",
                lineDataset, PlotOrientation.VERTICAL,
                true, true, false);
            XYPlot plot = lineChart.getXYPlot();
            XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer();
            renderer.setSeriesLinesVisible(0, false);
            renderer.setSeriesShapesVisible(1, true);
            renderer.setSeriesShape(1, new java.awt.geom.Ellipse2D.Double(-5, -5, 10, 10));
            plot.setDataset(1, markerDataset);
            plot.setRenderer(1, renderer);
        try {
            ChartUtils.saveChartAsJPEG(new File("src/main/resources/chart/charts.jpeg"), lineChart, 1920, 1080);
        } catch (IOException e) {
            System.out.println("Не удалось сохранить график");
        } catch (IllegalArgumentException e) {
            System.out.println("Неправильный формат числа");
        }
    }
}
