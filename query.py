import boto3
import os
import time
from pprint import pprint

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
SLIDO_ACCOUNT_UUID = os.environ['SLIDO_ACCOUNT_UUID']


def athena_query(athena,
                 query,
                 database,
                 workgroup,
                 s3_location,
                 max_iters=20,
                 sleep_time=3):

    response = athena.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': database
        },
        ResultConfiguration={
            'OutputLocation': s3_location
        },
        WorkGroup=workgroup
    )

    execution_id = response['QueryExecutionId']

    while max_iters > 0:
        max_iters -= 1

        response = athena.get_query_execution(QueryExecutionId=execution_id)
        status = response['QueryExecution']['Status']['State']
        if status == 'FAILED':
            return False

        if status == 'SUCCEEDED':
            return athena.get_query_results(
                QueryExecutionId=execution_id
            )

        time.sleep(sleep_time)

    raise Exception("Reached the number of max_iters.")


if __name__ == '__main__':

    params = {
        'region': 'eu-west-1',
        'database': SLIDO_ACCOUNT_UUID,
        'workgroup': SLIDO_ACCOUNT_UUID,
        'bucket': 'slido-dwh-customer-query-results',
        'query': 'SELECT * FROM events LIMIT 10'
    }

    session = boto3.Session()
    athena = session.client('athena',
                            region_name=params["region"],
                            aws_access_key_id=AWS_ACCESS_KEY,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3_location = f's3://{params["bucket"]}/{params["database"]}'

    pprint(athena_query(athena, params['query'], params['database'],
                        params['workgroup'], s3_location))
