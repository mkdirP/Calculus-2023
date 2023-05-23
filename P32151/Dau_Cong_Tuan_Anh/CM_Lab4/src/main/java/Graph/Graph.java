package Graph;

import Functions.FunctionManager;
import IO.InputSet;
import IO.OutputSet;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.annotations.XYPointerAnnotation;
import org.jfree.chart.annotations.XYTextAnnotation;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.chart.ui.ApplicationFrame;
import org.jfree.chart.ui.RectangleInsets;
import org.jfree.chart.ui.Size2D;
import org.jfree.chart.ui.TextAnchor;
import org.jfree.data.xy.DefaultXYDataset;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.awt.*;
import java.sql.ResultSet;
import java.util.List;

import static java.awt.Color.BLACK;
import static java.awt.Color.RED;

public class Graph extends ApplicationFrame {
    private static final String TITLE = "Graph";
    public Graph(String title) {
        super(title);
    }

    public Graph (String title, List<OutputSet> resultSetList, InputSet inputSet) {
        super(title);
        XYSeriesCollection dataset = createDataset(resultSetList);
        XYSeries xySeries = DataSet.createSeriesFromPoints(inputSet);
        dataset.addSeries(xySeries);
        JFreeChart chart = ChartFactory.createXYLineChart(TITLE,
                null, "Y", dataset, PlotOrientation.VERTICAL,
                true, true, false);
        final ChartPanel chartPanel = new ChartPanel(chart);
        final XYPlot plot = chart.getXYPlot();
//        plot.getRenderer().setSeriesPaint(6, new Color(255, 224, 64));
        plot.setDomainCrosshairVisible(true);
        plot.setRangeCrosshairVisible(true);
        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer( );
        renderer.setSeriesShapesVisible(0, false);
        renderer.setSeriesShapesVisible(1, false);
        renderer.setSeriesShapesVisible(2, false);
        renderer.setSeriesShapesVisible(3, false);
        renderer.setSeriesShapesVisible(4, false);
        renderer.setSeriesShapesVisible(5, false);
        renderer.setSeriesShapesVisible(6, true);
        renderer.setSeriesLinesVisible(6, false);

        plot.setRenderer( renderer );
        chartPanel.setPreferredSize(new java.awt.Dimension(580, 480));
        setContentPane(chartPanel);
    }

    public XYSeriesCollection createDataset(List<OutputSet> resultSetList) {
        XYSeriesCollection dataset = new XYSeriesCollection();
        for(int i = 0 ;i < resultSetList.size(); ++i) {
            dataset.addSeries(DataSet.createSeriesFromFunction(resultSetList.get(i).getEquation(), -1.0, 7.5, 0.1));
        }

        return dataset;
    }


}
