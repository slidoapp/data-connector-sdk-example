import boto3
import os
import awswrangler as wr

AWS_ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
SLIDO_ACCOUNT_UUID = os.environ['SLIDO_ACCOUNT_UUID']

params = {
    'region': 'eu-west-1',
    'database': SLIDO_ACCOUNT_UUID,
    'workgroup': SLIDO_ACCOUNT_UUID,
    'bucket': 'slido-dwh-customer-query-results',
    'query': 'SELECT * FROM events LIMIT 10'
}


if __name__ == '__main__':
    session = boto3.Session(region_name=params["region"],
                            aws_access_key_id=AWS_ACCESS_KEY,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    s3_location = f's3://{params["bucket"]}/{params["database"]}'

    result = wr.athena.read_sql_query(
        sql=params['query'],
        database=params['database'],
        s3_output=s3_location,
        workgroup=params['workgroup'],
        boto3_session=session,
        ctas_approach=False
    )

    print(result)
