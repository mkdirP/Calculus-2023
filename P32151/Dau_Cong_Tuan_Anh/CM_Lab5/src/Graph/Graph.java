package Graph;

import IO.InputSet;
import Model.Interpolation.Polynomial;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.chart.ui.ApplicationFrame;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import static Utils.Print.printMessage;

public class Graph extends ApplicationFrame {
    private static final String TITLE = "Graph";
    public Graph(String title) {
        super(title);
    }

    public Graph (String title, Polynomial polynomial, InputSet inputSet) {
        super(title);
        XYSeriesCollection dataset = createDataset(polynomial,
                inputSet.getPointList().get(0).getX(),
                inputSet.getPointList().get(inputSet.getSize() - 1).getX());
        XYSeries xySeries = DataSet.createSeriesFromPoints(inputSet);
        dataset.addSeries(xySeries);
        JFreeChart chart = ChartFactory.createXYLineChart(TITLE,
                null, "Y", dataset, PlotOrientation.VERTICAL,
                true, true, false);
        printMessage("1");
        final ChartPanel chartPanel = new ChartPanel(chart);
        printMessage("1");
        final XYPlot plot = chart.getXYPlot();
        printMessage("1");
        plot.setDomainCrosshairVisible(true);
        printMessage("1");
        plot.setRangeCrosshairVisible(true);
        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer( );
        printMessage("1");
        renderer.setSeriesShapesVisible(0, false);
        printMessage("1");
        renderer.setSeriesShapesVisible(1, true);
        printMessage("1");
        renderer.setSeriesLinesVisible(1, false);
        printMessage("1");
        plot.setRenderer( renderer );
        printMessage("1");
        chartPanel.setPreferredSize(new java.awt.Dimension(580, 480));
        printMessage("1");
        setContentPane(chartPanel);
    }

    public XYSeriesCollection createDataset(Polynomial polynomial, Double a, Double b) {
        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(DataSet.createSeriesFromFunction(polynomial, a, b, 0.001));
        return dataset;
    }


}
