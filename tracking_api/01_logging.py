import mlflow

mlflow.set_experiment("naive_experiment")
with mlflow.start_run():
    mlflow.log_param("my_parameter", .05)
    mlflow.log_param("my_parameter", "Hello MLFlow")
    mlflow.log_metric("my_metric", 42)
    