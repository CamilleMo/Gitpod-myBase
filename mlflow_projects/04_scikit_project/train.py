import sys
import numpy as np
from sklearn.linear_model import LinearRegression

import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://localhost:5000")

if __name__ == "__main__":
    np.random.seed(26)

    fit_intercept = True if sys.argv[1]=="true" else False

    x1 = np.random.randn(n_points)
    x2 = np.random.randn(n_points)
    x3 = np.random.randn(n_points)

    Y = 0.2 * x1 + 2 * x2 + 7 * x3 + 1.2
    Y = Y + (np.random.randn(n_points) / 1)  # adding some noise
    BigX = np.array([x1, x2, x3]).T

    reg = LinearRegression(fit_intercept=fit_intercept).fit(BigX, Y)
    print(reg.coef_)
    mlflow.log_metrics({"B1": reg.coef_[0], "B2": reg.coef_[1], "B3": reg.coef_[2]})
    if reg.intercept_:
        print(reg.intercept_)
        mlflow.log_metric("intercept", reg.intercept_)
    mlflow.sklearn.log_model(reg, "model")