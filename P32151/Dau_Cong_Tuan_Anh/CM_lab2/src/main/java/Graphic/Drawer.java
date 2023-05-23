package Graphic;

import Equation.Model.Interface.LinearEquation;
import Equation.Model.Interface.SystemEquation;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.chart.plot.XYPlot;
import org.jfree.chart.renderer.xy.XYLineAndShapeRenderer;
import org.jfree.chart.ui.ApplicationFrame;
import org.jfree.data.xy.*;

import java.awt.*;
import java.awt.geom.Point2D;


public class Drawer extends ApplicationFrame{

    public Drawer(String title) {
        super(title);
    }

    public void drawLinearEquation(LinearEquation equation, double x, double y, double root_x, double root_y) {
        final XYSeries series = new XYSeries(getTitle());
        final XYSeries series_2 = new XYSeries("res");
        series_2.add(root_x, root_y);

        for(double i = -5; i < 5; i += 0.1) {
            series.add(i, equation.resultAt(i));
        }
        final XYSeriesCollection dataset = new XYSeriesCollection( );
        dataset.addSeries(series);
        dataset.addSeries(series_2);

        JFreeChart xylineChart = ChartFactory.createXYLineChart(
                getTitle() ,
                "x" ,
                "y" ,
                dataset,
                PlotOrientation.VERTICAL ,
                true , false , false);

        ChartPanel chartPanel = new ChartPanel( xylineChart );
        chartPanel.setPreferredSize( new java.awt.Dimension( 560 , 367 ) );
        final XYPlot plot = xylineChart.getXYPlot( );
        plot.setDomainCrosshairVisible(true);
        plot.setRangeCrosshairVisible(true);

                XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer( );
//        renderer.setSeriesPaint( 0 , Color.RED );
//        renderer.setSeriesStroke( 0 , new BasicStroke( 1f ) );
        renderer.setSeriesShapesVisible(0, false);
        renderer.setSeriesShapesVisible(1, true);

        plot.setRenderer( renderer );
        setContentPane( chartPanel );
    }

    public void drawSystemEquation(SystemEquation systemEquation, double root_x, double root_y) {
        final XYSeries series_1 = new XYSeries("f_x",false);
        final XYSeries series_2 = new XYSeries("g_x",false);
        final XYSeries res = new XYSeries("root",false);
        res.add(root_x, root_y);
        final XYSeriesCollection dataset = systemEquation.makeDataset(series_1, series_2);
        dataset.addSeries(res);

        JFreeChart xylineChart = ChartFactory.createXYLineChart(
                getTitle(),
                "x",
                "y",
                dataset,
                PlotOrientation.VERTICAL,
                false, false, false);

        ChartPanel chartPanel = new ChartPanel(xylineChart);
        chartPanel.setPreferredSize(new java.awt.Dimension(500, 500));
        final XYPlot plot = xylineChart.getXYPlot();

        XYLineAndShapeRenderer renderer = new XYLineAndShapeRenderer();
        renderer.setSeriesPaint( 0 , Color.RED );
        renderer.setSeriesPaint( 1 , Color.GREEN );
        renderer.setSeriesPaint( 2 , Color.BLUE );
        plot.setDomainCrosshairVisible(true);
        plot.setRangeCrosshairVisible(true);
//        renderer.setSeriesStroke( 0 , new BasicStroke( 1f ) );
        renderer.setSeriesShapesVisible(0, false);
        renderer.setSeriesShapesVisible(1, false);
        renderer.setSeriesShapesVisible(2, true);

        plot.setRenderer(renderer);
            setContentPane(chartPanel);
        }
}
