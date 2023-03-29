package Equation.Model.Interface;

public interface LinearEquation {
    public double resultAt(double x);
    public double firstDerivative(double x);
    public double secondDerivative(double x);
    public String getEquation();
}
