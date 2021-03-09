import json
import os

import boto3
from aws_lambda_powertools import Logger, Metrics, Tracer

# https://awslabs.github.io/aws-lambda-powertools-python/#features
tracer = Tracer()
logger = Logger()
metrics = Metrics()

# Global variables are reused across execution contexts (if available)
session = boto3.Session()

@metrics.log_metrics(capture_cold_start_metric=True)
@logger.inject_lambda_context
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
        AWS Lambda handler
        Parameters
        ----------
        context: object, required
            Lambda Context runtime methods and attributes

        Attributes
        ----------

        context.aws_request_id: str
            Lambda request ID
        context.client_context: object
            Additional context when invoked through AWS Mobile SDK
        context.function_name: str
            Lambda function name
        context.function_version: str
            Function version identifier
        context.get_remaining_time_in_millis: function
            Time in milliseconds before function times out
        context.identity:
            Cognito identity provider context when invoked through AWS Mobile SDK
        context.invoked_function_arn: str
            Function ARN
        context.log_group_name: str
            Cloudwatch Log group name
        context.log_stream_name: str
            Cloudwatch Log stream name
        context.memory_limit_in_mb: int
            Function memory

            https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

        event: dict, required
            Redshift UDF payload Format
            arguments : JSON array wher each element is a record that is an array (in this case 3 arguments to UDF).

            {
              "request_id" : "23FF1F97-F28A-44AA-AB67-266ED976BF40",
              "cluster" : "arn:aws:redshift:xxxx",
              "user" : "master",
              "database" : "db1",
              "external_function": "public.foo",
              "query_id" : 5678234,
              "num_records" : 2,
              "arguments": [
                ["Customer", "id", "0"],
                ["Customer", "id", "1"]
              ]
            }
            https://docs.aws.amazon.com/redshift/latest/dg/udf-creating-a-lambda-sql-udf.html

        Returns
        ------
        Redshift UDF Lambda Expected Output Format
            {
              "success": true,   // true indicates the call succeeded
              "error_msg" : "my function isn't working",  // shall only exist when success != true
              "num_records": 2,      // number of records in this payload
              "results" : [
                1,
                4
              ]
            }
    """
    ret = dict()
    try:
        logger.info({
        "query_id": event['query_id'],
        "num_records": event['num_records']
        })
        tableName = event["arguments"][0][0]
        columnName = event["arguments"][0][1]

        res = []
        for argument in event['arguments']:
            try:
                columnValue = argument[2]
                res.append('hello ' + columnValue)
            except:
                res.append(None)
        ret['success'] = True
        ret['results'] = res
    except Exception as e:
        ret['success'] = False
        ret['error_msg'] = str(e)

    return json.dumps(ret)
