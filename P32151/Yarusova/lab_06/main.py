from get_data import get_data
import methods
import matplotlib.pyplot as plt


equation, result_equation, x0, xn, y0, h, accuracy = get_data()
result_runge, x_runge_kutta = methods.runge_kutta_method(equation, x0, xn, y0, h, accuracy)
result_miln, x_miln = methods.miln_method(equation, x0, xn, y0, h, accuracy)
result_euler, x_modify_euler = methods.modify_euler_method(equation, x0, xn, y0, h, accuracy)
print("Results:")
if result_miln is not None:
    print("Miln method: ")
    for i in range(len(x_miln)):
        print("x = ", round(x_miln[i], 6), "y = ", round(result_miln[i], 6))
    print("-------------------------------------------------")
print("Modify Euler method: ")
for i in range(len(x_modify_euler)):
    print("x = ", round(x_modify_euler[i], 6), "y = ", round(result_euler[i], 6))
print("-------------------------------------------------")
print("Runge-Kutta method: ")
for i in range(len(x_runge_kutta)):
    print("x = ", round(x_runge_kutta[i], 6), "y = ", round(result_runge[i], 6))
print("-------------------------------------------------")
result_equation_points = [result_equation(x) for x in x_miln]
plt.plot(x_miln, result_equation_points, marker=".", label="Equation")
plt.plot(x_miln, result_miln, marker=".", label="Miln method")
plt.plot(x_modify_euler, result_euler, marker=".", label="Modify Euler method")
plt.plot(x_runge_kutta, result_runge, marker=".", label="Runge-Kutta method")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
