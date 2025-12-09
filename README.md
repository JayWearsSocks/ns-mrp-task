# job application task

This is a job application task for NS for the role of "Medior developer Microservices Reizen en
Prijzen"

I made notes on what I did during this task.

## Prep not accounted for in the time limit (2 hours):

* Watched an introduction video about AWS Lambda
* Created this git repository
* Created an AWS account (free plan)

## Steps taken for the task

Following AWS documentation/ getting started guides:

* Created a Lamdba function + API Gateway from a blueprint and inspected results
  * blueprint is "Create a Microservice that interacts with a DDB table" in python
  * (changed the aws region to eu-central-1)
* Followed link to install AWS SDK. Had to set up authentication things for which I paused the time
  * added mfa to my account
  * installed aws cli to login in the terminal
  * crated an IAM user and an access key for that user

I now have an idea what infrastructure we need, so let's try to set it up:

* Created a DynamoDB table "ns-sales-table" with number ID
* Created a Lambda function "ns-sales-function" with java 21
* Created an API Gateway as a "trigger" of the Lambda function

Ran into the java code not being editable in the aws console (as it is for python). So we need to develop locally and deploy (this is what I would want ultimately either way, but it would have been nice to be able to get something working from the aws console first, to know what we're aiming for). 
I looked for examples online and found the aws-lambda-developer-guide. The examples are not just a java file, but also include deployment code and rely on package managers etc. I'm not familiar (yet) with the java ecosystem, so I thought it better to try to follow one example exactly than to set up my own.

## Try some examples from aws-lambda-developer-guide

I tried to follow this guide: https://github.com/awsdocs/aws-lambda-developer-guide/tree/main/sample-apps/blank-java
Installed the SDKMAN! package manager and Gradle build tool. But then at step 2 of the guide, I got a build error. I don't feel like it's a good idea to start debugging this now.

Let's try another sample app called "java-basic".
The first step (create bucket) is the same as in blank-java, so we can copy the output file (with the bucket name) into the java-basic directory and then move to step 2. I get an error that it cannot find java 21, which makes sense as I had java 25 installed, so that could be fixed. But then I run into another problem with the test platform.

## Code based on python blueprint

There isn't much time left to code at all at this point, and I'm not sure it's a good idea to keep installing things on my laptop without doing some research first. I would like to code something, so even though the task asks for java, let's try to work with the basic python example from the aws lambda blueprint since we know we can code that.

We got something working that takes input and checks it (the format is based on the template input for triggers coming from the aws api gateway). I created some test cases in the console to check for missing fields etc.

## Next steps

* Adding database integration (didn't have enough time left to try this, unfortunately)
* Add security measures for invoking the lambda so that only the intended API can access it. (And assign editing rights for developing with a team).
* Set up infrastructure-as-code to deploy the aws infra and the code at the same time, from a repository
* Set up unit tests for the repository code (to run locally)
* Set up test cases to be run automatically after deployment (deploy to a "staging" environment, then test there before deploying to "live")
* Set up performance test cases. Get an idea of the required performance for the business case. Try out some different scenarios e.g. with different memory allocations. Perhaps compare similar lambdas already in use.
* Possible performance bottle-neck could be the database interaction.
  * Maybe these requests can be processed asynchronously: the API received and validates the data, caches the data for some time (or until some amount is accrued) and replies immediately (with some queue-id?). Then stores to the db in a batch. (And perhaps there can be another endpoint for the client to check on the status of storing the data).
  * Maybe the database can be partitioned in some way, e.g. store sales from different souces in different tables.
* From what I learned about AWS lambda, is that a lot of scaling is taken care of automatically. So I'm not sure if it's needed to manually control things like the number of instances of the lambda that are running.


