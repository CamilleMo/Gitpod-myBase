pipenv run python mlflow_projects/05_register_a_model/register.py 
pipenv run python mlflow_projects/05_register_a_model/deploy_uat.py
# ! conda init bash ???
pipenv run mlflow models serve -m "models:/LinearRegressionModel/staging" -p 1234 --no-conda

