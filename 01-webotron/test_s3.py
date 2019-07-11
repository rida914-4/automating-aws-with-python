import boto3
import unittest


# nose collects tests from unittest.TestCase subclasses

#def test_aws_acct_setup():
# aws configure --profile pythonDev
# access key = Use access keys to make secure REST or HTTP Query protocol requests to AWS service APIs
# AWS Access Key ID [None]: AKIAZYQJ5ZVQI4KCR3X6
# AWS Secret Access Key [None]: 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
# Default region name [None]: us-east-1
# Default output format [None]: json

# Setup a global config file
# Setup nose logging
# def test_create_session():
#     # Create a session for AWS Interaction
#     session = boto3.Session(profile_name='pythonDev')  # Profile-name is username (IAM)
#     assert session


class S3_testcases(unittest.TestCase):
    """ Console Command : aws s3 ls --profile <username> """

    session = boto3.Session(profile_name='pythonDev',
                            aws_access_key_id='AKIAZYQJ5ZVQI4KCR3X6',
                            aws_secret_access_key='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',
                            )
    s3 = session.resource('s3')

    def check_bucket_exist(self):
        """ Check the number of buckets """
        s3 = self.session.resource('s3')
        for bucket in s3.buckets.all():
            print(bucket)

    def create_bucket(self):
        """ aws s3 mb(make bucket) s3://<bucket name>
            It has to be unique name, no capital
            Creates a public bucket """
        self.s3.create_bucket(Bucket='testcasebuckettwo')

    def test_all(self):
        self.check_bucket_exist()
        self.create_bucket()


