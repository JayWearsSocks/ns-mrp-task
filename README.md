# job application task

This is a job application task for NS for the role of "Medior developer Microservices Reizen en
Prijzen"

## What did I do?

Not accounted for in the task time limit (2 hours):

* Watched an introduction video about AWS Lambda
* Created this git repository
* Created an AWS account (free plan)

Following AWS documentation/ getting started guides:

* Created a Lamdba function + API Gateway from a blueprint and inspected results
  * blueprint is "Create a Microservice that interacts with a DDB table" in python
  * (changed the aws region to eu-central-1)
* Followed link to install AWS SDK. Had to set up auth things for which I paused the time
  * added mfa to my account
  * installed aws cli
  * crated an IAM user and an access key for that user

Steps for setting up the infra for the task:

* Created a DynamoDB table "ns-sales-table" with number ID
* Created a Lambda function "ns-sales-function" with java 21
* Created an API Gateway as a "trigger" of the Lambda function

Tried to get "something" working, but cannot edit the code in the console (has to be uploaded). Looked for documentation/ a minial working example with asw Lambda and Java. Most things I find include a lot more than a simple java program. Having a package manager, deployment code, and maybe infrastructure code for the aws resources is probably the better way to go about it anyway. However, I'm not familiar with the Java ecosystem so it's not an option to set this up locally from scratch. Let's try it again with one of the more complete examples I found from the AWS developer documentation...

## Try again from java example
Example: https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/example-java
