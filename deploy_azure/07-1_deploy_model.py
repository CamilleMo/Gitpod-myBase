from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.webservice import AciWebservice, Webservice

import mlflow.azureml

from xx_secrets import subscription_id

workspace_name = "ml-deployment-platform"
workspace_location = "West Europe"
resource_group = "mlflow-tuto-rg"

workspace = Workspace.create(
    name=workspace_name,
    location=workspace_location,
    resource_group=resource_group,
    subscription_id=subscription_id,
    exist_ok=True,
)

model_name = "LinearRegressionModel"
model_uri = f"models:/{model_name}/1"

aci_service_name = "lr-uat-2"
aci_service_config = AciWebservice.deploy_configuration(cpu_cores=1, memory_gb=1)

azure_service, azure_model = mlflow.azureml.deploy(
    model_uri=model_uri,
    service_name=aci_service_name,
    model_name=model_name,
    workspace=workspace,
    deployment_config=aci_service_config,
    synchronous=True,
)
