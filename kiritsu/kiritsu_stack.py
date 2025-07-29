from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from constructs import Construct

class KiritsuStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        PythonFunction(
            self,
            "SpyPriceFn",
            entry="lambda",          # ← main.py + requirements.txt live here
            index="main.py",
            handler="handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
        )

