import sys
import numpy as np
from sklearn.linear_model import LinearRegression

import mlflow

if __name__ == "__main__":
    np.random.seed(26)

    # eta = float(sys.argv[1])  # 0.1
    # mlflow.log_param("learning_rate", eta)
    # n_iter = int(sys.argv[2])  # 100
    # mlflow.log_param("number_of_epochs", n_iter)
    # n_points = 100

    x1 = np.random.randn(n_points)
    x2 = np.random.randn(n_points)
    x3 = np.random.randn(n_points)

    Y = 0.2 * x1 + 2 * x2 + 7 * x3 + 1.2
    Y = Y + (np.random.randn(n_points) / 1)  # adding some noise

    reg = LinearRegression().fit(X, y)
