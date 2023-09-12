from Exceptions.IncorrectValueException import IncorrectValueException
from Matrix.Matrix import Matrix
from Matrix.MatrixMethods import MatrixMethods
from Terminal import Terminal

if __name__ == "__main__":

    terminal = Terminal()
    while True:
        terminal.refresh()
        terminal.work()
        print("Хотите продолжить работу с программой? y/n")
        if not input().__eq__('y'):
            break


