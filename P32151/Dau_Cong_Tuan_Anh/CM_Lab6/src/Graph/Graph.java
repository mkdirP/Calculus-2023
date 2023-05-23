package Graph;

import IO.InputSet;
import Model.Algorithm.Algorithm;
import Model.Function.Function;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.chart.ui.ApplicationFrame;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

public class Graph extends ApplicationFrame {
    private static final String TITLE = "Graph";
    public Graph(String title) {
        super(title);
    }

    public Graph (String title, Algorithm algorithm, InputSet inputSet, Function function) {
        super(title);
        XYSeriesCollection dataset = createDataset(algorithm, inputSet, function);
        JFreeChart chart = ChartFactory.createXYLineChart(TITLE,
                null, "Y", dataset, PlotOrientation.VERTICAL,
                true, true, false);
        final ChartPanel chartPanel = new ChartPanel(chart);
        final XYPlot plot = chart.getXYPlot();
        plot.setDomainCrosshairVisible(true);
        plot.setRangeCrosshairVisible(true);
        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer( );
        renderer.setSeriesShapesVisible(0, false);
        renderer.setSeriesShapesVisible(1, false);

        plot.setRenderer( renderer );
        chartPanel.setPreferredSize(new java.awt.Dimension(580, 480));
        setContentPane(chartPanel);
    }

    public XYSeriesCollection createDataset(Algorithm algorithm, InputSet inputSet, Function function) {
        XYSeriesCollection dataset = new XYSeriesCollection();
        inputSet.setH(0.001);
        int n = (int) ((inputSet.getB() - inputSet.getA())/0.001);
        Double[][] tb = algorithm.execute(inputSet, function);
        final XYSeries sr1 = new XYSeries(algorithm.toString());
        for(int i = 0; i < n; ++i) {
            sr1.add(tb[i][0], tb[i][1]);
        }
        dataset.addSeries(sr1);
        final XYSeries sr2 = new XYSeries("exact");
        for(int i = 0; i < n; ++i) {
            sr2.add(tb[i][0], tb[i][3]);
        }
        dataset.addSeries(sr2);
        return dataset;
    }



}
