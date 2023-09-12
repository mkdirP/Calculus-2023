package org.example;

import java.awt.BasicStroke;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.Toolkit;
import java.util.function.Function;

import javax.swing.JFrame;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

public class GraphFrame extends JFrame {
    private static final long serialVersionUID = 1L;
    public static final double DEFAULT_STEP = 0.05;

    public GraphFrame(String title) {
        super(title);
    }

    public void graph(double a, double b, Function<Double, Double> function) {
        XYDataset dataset = generateDataset(a, b, function);
        JFreeChart chart = createChart(dataset);
        ChartPanel panel = new ChartPanel(chart);
        setupChartPanel(panel);
        setContentPane(panel);
        pack();
        centerFrame();
        setVisible(true);
    }

    private XYDataset generateDataset(double from, double to, Function<Double, Double> function) {
        XYSeries series = new XYSeries(function.hashCode());
        for (double x = from; x <= to; x += DEFAULT_STEP) {
            double y = function.apply(x);
            if (Double.isFinite(y)) {
                series.add(x, y);
            }
        }
        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(series);
        return dataset;
    }


    private JFreeChart createChart(XYDataset dataset) {
        return ChartFactory.createXYLineChart(
                getTitle(),
                "X",
                "Y",
                dataset,
                PlotOrientation.VERTICAL,
                false,
                true,
                false
        );
    }

    private void setupChartPanel(ChartPanel panel) {
        panel.setMouseWheelEnabled(true);
        panel.setPreferredSize(new Dimension(800, 600));
        XYPlot plot = panel.getChart().getXYPlot();
        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer();
        renderer.setSeriesStroke(0, new BasicStroke(2.0f));
        plot.setRenderer(renderer);
    }

    private void centerFrame() {
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int centerX = (int) (screenSize.getWidth() - getWidth()) / 2;
        int centerY = (int) (screenSize.getHeight() - getHeight()) / 2;
        setLocation(centerX, centerY);
    }
}
