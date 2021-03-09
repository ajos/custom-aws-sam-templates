import json

from redshift_udf_test import app


def test_lambda_handler(apigw_event, lambda_context):
    ret = app.lambda_handler(apigw_event, lambda_context)

    assert ret['success'] == 'true'
