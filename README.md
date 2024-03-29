# Serverless CI-CD

This repository provides a skeleton with some files in order for you to get
started creating:

- your own CI-CD solution using [Jenkins](https://www.jenkins.io/) 
- a Serverless backend for the site you will be deploying using [AWS
  Lambda](https://aws.amazon.com/lambda/) and [Amazon API
  Gateway](https://aws.amazon.com/api-gateway/), following a common industry
  pattern.

On this page you will find:

- [Diagrams](#desired-application-and-deployment-process) that serve as the main
  description of what you should be building.
- A series of high-level [tasks](#getting-started) to guide you through the
  project.
- Some [documentation](#project-files) to help you understand the files in this
  repo 

## Desired application and deployment process

Below, you fill find some diagrams that describe the system you have been asked
to build in a bit more detail. 

Even so, you'll find that they leave some questions unanswered: some arrows have
been left unlabelled and the inner workings of some of the tools involved are
not explained. The missing bits are for you to research and discover!

### Application diagram

The following diagram shows how the application should work once deployed. 

![Application diagram](assets/application_diagram.jpg?raw=true "Application
diagram")

The diagram shows that the app is composed of:
- a static site hosted on S3 and accessible through the browser,
- and a backend which the site sends requests to.

It also shows that the backend should be powered by AWS Lambda and that the
frontend should access AWS Lambda through a service called Amazon API Gateway.

### Deployment process diagram

The next diagram illustrates how the application should be deployed:

- The code for the app should be hosted on GitHub
- Jenkins should be used to automatically deploy the application code to AWS S3.
  
![Deployment process diagram](assets/deployment_process_diagram.jpg?raw=true
"Deployment process diagram")

## Getting Started

As a team, using the diagrams and high-level tasks shared below as a starting
point, map out what you understand so far and what open questions you will need
to research.

**Keep modifying and expanding the diagrams you've been given with what you
find.** At the end of the week, you can submit them to your coach for feedback.
Your coach may also ask you to discuss your diagrams during group check-ins.

### Tasks

1. [Set up S3](01_set_up_s3.md)
2. [Set up Jenkins](02_set_up_jenkins.md)
3. [Set up a CI-CD pipeline in Jenkins](03_set_up_pipeline.md)
4. [Set up the Serverless backend](04_set_up_serverless.md)
5. [Bonus tasks: Deepen your understanding, consolidate and
   explore](05_bonus.md)

## Project files

- In the `template` folder you will find some files for a website. These are the
  files we will deploy for our static website on an AWS S3 Bucket.
- `resources/deploy_ec2_network_v1.json` is the
  [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
  template to automate the process of creating an EC2 instance on AWS, assign
  the necessary roles and policies and add some security settings that are
  needed for Jenkins to be able to run on the EC2 instance. Note that you do not
  need to know what the whole template does line by line. We will, in fact,
  spend some more time next week working with these concepts on AWS.
- `resources/your-first-lambda.py` is the Lambda function that you will deploy
  in AWS and eventually invoke once you deploy your static website on AWS.
  Modify it to include the names of your group members.
- `assets` folder: files in this folder doesn't need to be deployed. It contains
  support assets for this README (e.g. images).


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
