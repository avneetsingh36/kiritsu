from aws_cdk import Stack
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_lambda as _lambda
from constructs import Construct

class KiritsuStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _lambda.Function(
                self, "LocalWeatherLambda",
                runtime=_lambda.Runtime.PYTHON_3_12,
                handler="main.handler",
                code=_lambda.Code.from_asset("lambda")
        )
