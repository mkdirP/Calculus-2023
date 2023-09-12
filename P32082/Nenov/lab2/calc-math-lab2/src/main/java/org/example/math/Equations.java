package org.example.math;

import org.example.math.systems.MultiArgFunction;

public class Equations {
    public static final MultiArgFunction[] system1 = new MultiArgFunction[] {
      new MultiArgFunction() {
          @Override
          public double calculate(double... x) {
              return 3*x[1]*x[1]*x[1] + x[0]*x[0]*x[0] + 4;
          }

          @Override
          public String toString() {
              return "x^2 + y^2 - 4 = 0";
          }
      },
        new MultiArgFunction() {
            @Override
            public double calculate(double... x) {
                return 7*x[0]*x[0] + 15*x[0] + x[1]*x[1];
            }

            @Override
            public String toString() {
                return "3x^2 - y = 0";
            }
        }
    };

    public static final MultiArgFunction[] system2 = new MultiArgFunction[] {
            new MultiArgFunction() {
                @Override
                public double calculate(double... x) {
                    return 0.3 - 0.1*x[0]*x[0] - 0.2*x[1]*x[1];
                }

                @Override
                public String toString() {
                    return "x = 0.3 - 0.1x^2 - 0.2y^2";
                }
            },
            new MultiArgFunction() {
                @Override
                public double calculate(double... x) {
                    return 0.7 - 0.2*x[0]*x[0] - 0.1*x[1]*x[0];
                }

                @Override
                public String toString() {
                    return "y = 0.7 - 0.2x^2 - 0.1xy";
                }
            }
    };
    public static final Function func5 = new Function() {
        @Override
        public double calculate(double x) {
            return -2.7*x*x*x-1.48*x*x+19.23*x+6.35;
        }

        @Override
        public String toString() {
            return "-2.7x^3 - 1.48x^2 + 19.23x + 6.23 = 0";
        }
    };
    public static final Function func22 = new Function() {
        @Override
        public double calculate(double x) {
            return x*x*x-3.78*x*x+1.25*x+3.49;
        }

        @Override
        public String toString() {
            return "x^3 - 3.78x^2 + 1.25x + 3.49 = 0";
        }
    };
    public static final Function myFunc = new Function() {
        @Override
        public double calculate(double x) {
            return Math.pow(4, x) + x*x - 5;
        }

        @Override
        public String toString() {
            return "4^x + x^2 - 5 = 0";
        }
    };
}
