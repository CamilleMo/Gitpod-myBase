rm -rf mlflow_projects/04_scikit_project/artifacts
pipenv run mlflow run mlflow_projects/04_scikit_project/ --experiment-name=scikit_project -P intercept=false
pipenv run mlflow run mlflow_projects/04_scikit_project/ --experiment-name=scikit_project -P intercept=true
(cd mlflow_projects/04_scikit_project/artifacts && tar c .) | (cd artifacts && tar xf -)