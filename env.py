import os
from ssm_ps import get_ssmparameters_by_path

token = ""

while True:
    response = get_ssmparameters_by_path(os.environ['SSM_PATH'], token)

    for param in response['Parameters']:
        os.environ[param['Name']] = param['Value']

    if 'NextToken' in response:
        token=response['NextToken']

    else:
        break