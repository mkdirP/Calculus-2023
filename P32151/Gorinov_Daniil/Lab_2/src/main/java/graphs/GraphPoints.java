package graphs;

import java.awt.*;
import java.awt.geom.Ellipse2D;
import java.util.Map;

import javax.swing.JFrame;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.annotations.XYPointerAnnotation;
import org.jfree.chart.annotations.XYTextAnnotation;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYItemRenderer;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

public class GraphPoints extends JFrame {
    private static final int WIDTH = 800;
    private static final int HEIGHT = 600;

    public GraphPoints(Map<Double, Double> points, Double answer) {
        super("Graph Points with Answer");

        setSize(WIDTH, HEIGHT);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Создание набора данных для графика
        XYSeriesCollection dataset = new XYSeriesCollection();
        XYSeries series = new XYSeries("Points");
        points.forEach(series::add);
        dataset.addSeries(series);

        // Создание графика
        JFreeChart chart = ChartFactory.createXYLineChart(
                "Graph Points with Answer", // Заголовок графика
                "X", // Название оси X
                "Y", // Название оси Y
                dataset, // Набор данных для графика
                PlotOrientation.VERTICAL, // Ориентация графика
                true, // Отображать легенду
                true, // Включить инструменты для масштабирования и сохранения
                false // Не отображать URL в легенде
        );

        // Настройка внешнего вида графика
        chart.setBackgroundPaint(Color.white);
        XYPlot plot = chart.getXYPlot();
        plot.setBackgroundPaint(Color.white);
        plot.setRangeGridlinePaint(Color.lightGray);
        plot.setDomainGridlinePaint(Color.lightGray);

        Shape shape = new Ellipse2D.Double(-5, -5, 10, 10);
        XYPointerAnnotation annotation = new XYPointerAnnotation("Answer",
                answer, 0.0, -Math.PI / 4);
        annotation.setArrowPaint(Color.green);
        annotation.setTipRadius(0);
        annotation.setBaseRadius(20);
        //annotation.setShape(shape);
        plot.addAnnotation(annotation);

        // Создание панели для отображения графика
        ChartPanel chartPanel = new ChartPanel(chart);
        chartPanel.setPreferredSize(new Dimension(WIDTH, HEIGHT));
        setContentPane(chartPanel);

        setVisible(true);
    }
}
