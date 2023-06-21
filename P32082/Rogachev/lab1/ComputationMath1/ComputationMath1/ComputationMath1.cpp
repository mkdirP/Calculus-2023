#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

void printMatrix(vector<vector<double>> matrix, vector<double> coef) {
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix.size(); j++) {
            cout << matrix[i][j] << ' ';
        }
        cout << coef[i] << endl;
    }
}

void printAnswer(vector<vector<double>> answer) {
    cout << "Error of computional:" << endl;

    for (int i = 1; i < answer.size(); i++) {
        for (int j = 0; j < answer[i].size(); j++) {
            cout << fabs(answer[i][j] - answer[i - 1][j]) << ' ';
        }
        cout << endl;
    }

    cout << "Count of steps: " << answer.size() - 1 << endl;
    cout << "Vector with unknown variables:" << endl;

    for (auto a : answer[answer.size() - 1]) {
        cout << a << ' ';
    }
    cout << endl;

}

void printError(vector<vector<double>> answer, vector<vector<double>> matrix, vector<double> coef) {
    for (int i = 0; i < matrix.size(); i++) {
        double t = 0;
        for (int j = 0; j < matrix.size(); j++) {
            t += matrix[i][j] * answer[answer.size() - 1][j];
        }
        cout << fabs(t - coef[i]) << " ";
    }
    cout << endl;
}

bool checkDiagonal(vector<vector<double>> matrix) {
    bool flag = true;

    for (int i = 0; i < matrix.size(); i++) {
        double x = 0;
        for (int j = 0; j < matrix[i].size(); j++) {
            if (i != j)
                x += fabs(matrix[i][j]);
        }
        if (fabs(matrix[i][i]) < x)
            flag = false;
    }

    return flag;
}

vector<vector<double>> swap(vector<vector<double>> matrix, int x, int y) {
    for (int i = 0; i < matrix.size(); i++) {
        double temp = matrix[i][x];

        matrix[i][x] = matrix[i][y];
        matrix[i][y] = temp;
    }

    return matrix;
}

vector<vector<double>> diagonalize(vector<vector<double>> matrix) {
    for (int i = 0; i < matrix.size(); i++) {
        int cur = i;

        for (int j = 0; j < matrix.size(); j++) {
            if (fabs(matrix[i][cur]) < fabs(matrix[i][j])) {
                cur = j;
            }
        }
        if (cur != i) {
            matrix = swap(matrix, cur, i);
        }
    }

    return matrix;
}

vector<vector<double>> iterations(vector<vector<double>> matrix, vector<double> coef, double epsilon) {
    for (int i = 0; i < matrix.size(); i++) {
        double temp = matrix[i][i];

        coef[i] /= temp;
        for (int j = 0; j < matrix.size(); j++) {
            matrix[i][j] /= -temp;
        }

        matrix[i][i] = 0;
    }

    vector<vector<double>> answer;

    answer.push_back(coef);

    while (1) {
        answer.push_back(coef);

        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix.size(); j++) {
                answer[answer.size() - 1][i] += matrix[i][j] * answer[answer.size() - 2][j];
            }
        }

        double delta = -INFINITY;

        for (int i = 0; i < matrix.size(); i++) {
            delta = max(delta, fabs(answer[answer.size() - 1][i] - answer[answer.size() - 2][i]));
        }

        if (delta < epsilon || answer.size() > 2000) {
            break;
        }
    }

    return answer;
}

void executeProgram(vector<vector<double>> matrix, vector<double> coef, double epsilon) {
    cout << "Read:" << endl;
    printMatrix(matrix, coef);
    cout << epsilon << endl;

    if (checkDiagonal(matrix)) {
        cout << "Matrix has diagonal dominance" << endl;
    }
    else {
        cout << "Matrix hasn't diagonal dominance" << endl;
        matrix = diagonalize(matrix);
        if (!checkDiagonal(matrix)) {
            cout << "Impossible to convert matrix to diagonal dominance" << endl;
        }
        else {
            cout << "Possible to convert" << endl;
        }
    }

    cout << "Matrix: " << endl;
    printMatrix(matrix, coef);

    vector<vector<double>> ans = iterations(matrix, coef, epsilon);

    if (ans.size() > 2000) {
        cout << "Print the vector of unknowns!" << endl;
    }

    cout << "Answer:" << endl;
    printAnswer(ans);
    printError(ans, matrix, coef);
}

int main()
{
    while (1) {
        int x;

        cout << "0 - enter this number, if you want to write data from console" << endl;
        cout << "1 - enter this number, if you want to write data from file" << endl;
        cout << "2 - enter this number, if you want to exit from program" << endl;

        cin >> x;

        if (x == 0) {
            while (1) {
                cout << "Enter matrix size(one number <= 20): ";
                int n;
                cin >> n;
                if (n < 0 || n > 20) {
                    cout << "Invalid input!" << endl;
                    continue;
                }

                cout << "Enter data to calculate in format (x1 x2 ... b1)" << endl;

                vector<vector<double>> matrix(n, vector<double>(n, 0));
                vector<double> coef(n);

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        cin >> matrix[i][j];
                    }
                    cin >> coef[i];
                }

                cout << "Enter accuracy: ";

                double epsilon;

                cin >> epsilon;

                if (epsilon < 0) {
                    cout << "Invalid input (accuracy must be >0)!" << endl;
                    continue;
                }

                executeProgram(matrix, coef, epsilon);
                break;
            }
        }
        else if (x == 1) {
            ifstream file;

            while (1) {
                string fileName;

                cout << "Enter path to file: ";
                cin >> fileName;

                file.open(fileName);
                if (!file.is_open()) {
                    cout << "Invalid filename!" << endl;
                    continue;
                }

                int n;
                file >> n;
                if (n < 0 || n > 20) {
                    cout << "Size must be > 0 and <= 20!" << endl;
                    continue;
                }

                vector<vector<double>> matrix(n, vector<double>(n, 0));
                vector<double> coef(n);

                for (int i = 0; i < n; i++) {
                    for (int j = 0; j < n; j++) {
                        file >> matrix[i][j];
                    }
                    file >> coef[i];
                }

                double epsilon;

                file >> epsilon;

                if (epsilon < 0) {
                    cout << "Invalid input (accuracy must be >0)" << endl;
                    continue;
                }

                executeProgram(matrix, coef, epsilon);

                break;
            }
            file.close();
        }
        else if (x == 2) {
            break;
        }
        else {
            cout << "Invalid input" << endl;
            continue;
        }
    }
}