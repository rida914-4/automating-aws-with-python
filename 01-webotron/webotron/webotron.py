""" This script controls the console using user-defined commands"""
import boto3
import click


session = boto3.Session(profile_name='pythonDev',
                            aws_access_key_id='AKIAZYQJ5ZVQI4KCR3X6',

                            )
s3 = session.resource('s3')

# Decorator to group the cli commands . Call this
# function and you will have access to all the commands
@click.group()
def cli():
    """ AWS TestCases CLI """
    pass


@cli.command('list-buckets')
def list_buckets():
    """ List buckets"""
    for bucket in s3.buckets.all():
        print(bucket)


@cli.command('list-bucket-objects-all')
def list_buckets_objects_all():
    """ List ALL objects in a bucket """
    for bucket in s3.buckets.all():
        for obj in bucket.objects.all():
            print("Bucket ({}) : Object ({})".format(bucket, obj))


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_buckets_objects(bucket):
    """ List ALL objects in a bucket """
    for obj in s3.Bucket(bucket).objects.all():
        print("Bucket ({}) : Object ({})".format(bucket, obj))


if __name__ == '__main__':
    cli()
