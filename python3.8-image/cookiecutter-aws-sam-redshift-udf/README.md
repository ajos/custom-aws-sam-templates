# Cookiecutter SAM for Python Lambda functions

This is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template to create a Serverless Redshift Python UDF on Serverless Application Model (SAM) and Python 3.8 container image.

## Usage

Generate a new SAM based Serverless App: 
```bash
git clone git@github.com:ajos/custom-aws-sam-templates.git
## generate project 
sam init --location custom-aws-sam-templates/python3.8-image/cookiecutter-aws-sam-redshift-udf
```

You'll be prompted a few questions to help this cookiecutter template to scaffold this project and after its completed you should see a new folder at your current path with the name of the project you gave as input.

## Options

Option | Description
------------------------------------------------- | ---------------------------------------------------------------------------------
`include_safe_deployment` | Sends by default 10% of traffic for every 1 minute to a newly deployed function using [CodeDeploy + SAM integration](https://github.com/awslabs/serverless-application-model/blob/master/docs/safe_lambda_deployments.rst) - Linear10PercentEvery1Minute

# Credits

* This project has been generated with [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [aws-samples : Cookiecutter SAM for Python Lambda functions](https://github.com/aws-samples/cookiecutter-aws-sam-python)

License
-------

This project is licensed under the terms of the [MIT License with no attribution](/LICENSE)
