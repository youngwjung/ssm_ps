import boto3


def get_ssmparameter(param_name):
    """
    This function reads a secure parameter from AWS' SSM service.
    The request must be passed a valid parameter name.
    Default Region: A region where an EC2 instance is deployed
    """
    # Create the SSM Client
    ssm = boto3.client('ssm')

    # Get the requested parameter
    response = ssm.get_parameters(
        Names=[
            param_name,
        ],
        WithDecryption=True
    )

    # Store the returned parameter's value in a variable
    if not response['InvalidParameters']:
        param_value = response['Parameters'][0]['Value']
    else:
        param_value = 'InvalidParameter'

    return param_value


def get_ssmparameters_by_path(path, next_token=''):

    # Create the SSM Client
    ssm = boto3.client('ssm')

    # Up to 10 parameters can be retrieved by a request.
    # A token will be returned in a response to indicate a next batch of parameters to be retrieved
    if next_token:
        response = ssm.get_parameters_by_path(
            Path=path,
            Recursive=True,
            WithDecryption=True,
            NextToken=next_token
        )
    else:
        response = ssm.get_parameters_by_path(
            Path=path,
            Recursive=True,
            WithDecryption=True
        )

    return response