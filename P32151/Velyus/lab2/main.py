from InputCorrect import InputCorrect
from OutputCorrect import VariantsFunctionSolver, SystemSolver

if __name__ == '__main__':
    variants = ["Выбрать функцию и метод из предложенных",
                "Выбрать систему уравнений из предложенных и решить её методом простых итераций"]
    values = [VariantsFunctionSolver, SystemSolver]

    chosen_variant = InputCorrect.get_multiple_choice_input(variants, values, "Что вы хотите решить?")
    chosen_variant().solve()
