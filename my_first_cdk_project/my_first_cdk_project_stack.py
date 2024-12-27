from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as _s3,
)
from constructs import Construct

class MyFirstCdkProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "MyFirstCdkProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        _s3.Bucket(
            self, 
            "myBucketId",
            bucket_name="my-first-cdk-project-bucket-27122024",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )