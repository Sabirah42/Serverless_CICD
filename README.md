# Serverless CI-CD

This repository provides a skeleton with some files in order for you to get started creating:

- your own CI-CD solution using [Jenkins](https://www.jenkins.io/) 
- a Serverless backend for the site you will be deploying using [AWS Lambda](https://aws.amazon.com/lambda/) and [Amazon API Gateway](https://aws.amazon.com/api-gateway/), following a common industry pattern.

In this README you will find:

- [Diagrams](#desired-application-and-deployment-process) that serve as the main description of what you should be building.
- A series of high-level [tasks](#getting-started) to guide you through the project.
- Some [documentation](#documentation) to help you understand the files in this repo 
- [Resources](#supporting-materials) that can serve as starting points to help you tackle some of the tasks.

## Desired application and deployment process

Below, you fill find some diagrams that describe the system you have been asked to build in a bit more detail. 

Even so, you'll find that they leave some questions unanswered: some arrows have been left unlabelled and the inner workings of some of the tools involved are not explained.
The missing bits are for you to research and discover!

### Application diagram

The following diagram shows how the application should work once deployed. 

![Application diagram](assets/application_diagram.jpg?raw=true "Application diagram")

The diagram shows that the app is composed of:
- a static site hosted on S3 and accessible through the browser,
- and a backend which the site sends requests to.
  
The backend should be powered by AWS Lambda. The frontend should access AWS Lambda through the Amazon API Gateway.

### Deployment process diagram

The next diagram illustrates how the application should be deployed:

- The code for the app should be hosted on GitHub
- Jenkins should be used to automatically deploy the application code to AWS S3.
  
![Deployment process diagram](assets/deployment_process_diagram.jpg?raw=true "Deployment process diagram")


## Getting Started

As a team, using the diagrams and high-level tasks shared below as a starting point, map out what you understand so far, what open questions you have, and what you will need to research.

Keep modifying and expanding the diagrams you've been given with what you find.

## Set up S3

S3 is an [Object storage](https://cloud.netapp.com/blog/block-storage-vs-object-storage-cloud) service by AWS. 

- Create an S3 Bucket and configure it to host your static website.
- Check that the static site works by visiting it in your browser.

## Set up Jenkins

Set up an [EC2 instance](https://docs.aws.amazon.com/ec2/index.html) using the [CloudFormation]((https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)) [template](deploy_ec2_network_v1.json) provided in this repo and install Jenkins on it.

> :information_source: The Jenkins-related taasks are likely to take some time and dedicated research. It is also likely that you encounter some obstacles along the way, so this is a great chance to get hands-on and sharpen your debugging skills by finding and reading through logs and error messages. You can do this!

### Some hints

1. The template is made to work pretty much as is. The *only section you need to modify* is the identifier for the S3 bucket you created previously. Can you spot where you need to add it?
2. Using the template, you will need to create something called a **stack** using the CloudFormation template on AWS.
3. You will know you have successfully installed Jenkins if when you open the **public IPv4 DNS address** of your EC2 instance in the browser, you get a `Getting Started` page with the following title: `Unlock Jenkins`.
4. Once you've unlocked Jenkins, install the plugins it recommends.

### Check your understanding

Jenkins can in fact run on your local machine, so why bother setting up an EC2 instance for Jenkins to run on it?

:pencil: Have a group discussion and think about the advantages and disavantages of each of these approaches before you move on.

## Set up a CI-CD pipeline in Jenkins

### Create a diagram of your desired pipeline

Consult your diagram(s) again and revisit what you know so far about CI-CD pipelines and their benefits.

![Deployment process diagram](assets/deployment_process_diagram.jpg?raw=true "Deployment process diagram")

What checks and actions should your CI-CD pipeline perform? When should these checks and actions be run?

Remember that, ultimately, the idea is for your pipeline to only proceed to deploying the code if the checks pass.

If you haven't already, expand the diagram above so that it illustrates in more detail what should happens in the "Jenkins" step.
This will give you a better idea of what you want to use Jenkins for and help you research the right things.

> :information_source: You can find many examples of CI-CD pipeline diagrams online that you can use for inspiration. The resources shared with you during the CI-CD workshop will also help with this.

### Set up the pipeline

Below you will find a high-level list of the tasks that are necessary for you to sucessfully set up the Jenkins pipeline in CI-CD.

- Using the Jenkins classic UI, set up a new [Pipeline project](https://www.jenkins.io/doc/book/pipeline/).
- Give Jenkins access to your GitHub repository by giving Jenkins the right **credentials**.
- Using a **webhook**, set up GitHub to automatically trigger your pipeline to run. What events should ideally trigger your pipeline to run?
- By writing a `Jenkinsfile`, set up the CI part of your pipeline. It should run checks to make sure the code in your repository is good to be deployed.
- Extend your `Jenkinsfile` with a step that deploys your application to the S3 bucket you created initially.

> :information_source: Not all of the tasks above need to be completed in the exact order they are given here.  Guides you may come across in your research might go through these in a slightly different order. Don't worry if you end performing some steps in a different order from the one given here.

### Check your understanding

#### Understanding the `Jenkinsfile`

You've created a `Jenkinsfile`, but do you know how it works?
Spend some time understanding each line in the file and adding explanatory comments to it.

Here are a few questions to ask yourself:
- On what machine do the commands in your Jenkinsfile run?
- What part of your `Jenkinsfile` ensures that the correct version of Python will be available to run the code?

#### How does Jenkins get access to your repo?

You've set up a connection between Jenkins running on the EC2 instance and your GitHub repository.
But how does it work?

- How does Jenkins find out there was a change to your GitHub repo? 
- How does Jenkins retrieve a copy of the repository? Where does it clone your repository to?

Try to be as detailed and specific as possible! Perhaps a [sequence diagram](https://playground.diagram.codes/d/sequence) could be a good fit for this?

![Application diagram](assets/jenkins_github_sequence_diagram.svg?raw=true "Application diagram")

The documentation for the Jenkins Git Plugin as well as reading the Jenkins logs will help you figure out what happens behind the scenes when you do a push.

## Set up the Serverless backend

Now that automatic deployment of the static site works, the next task is to make it dynamic by building a backend for it and connecting it to the static site.

> :warning: Before moving on to this task, make sure you have successfully deployed your HTML files to your S3 Bucket.

### Diagramming the backend

Revisit your diagram(s) again.
What services will you need to research next?

![Application diagram](assets/application_diagram.jpg?raw=true "Application diagram")

Can you flesh out your understanding of the connection between the static site, API Gateway and AWS Lambda?

Where could you look to figure out what kind of requests and responses the the arrows represent?

Improve this diagram as you learn more.

### Tasks

- Using the AWS Lambda service in the AWS Console, set up set up an Python Lambda function whose definition matches the one in the [`your-first-lambda.py`](your-first-lambda.py) file. Do not forget to modify it!
- Set up an API Gateway **endpoint** which, will **invoke** the Lambda function you created whenever a request is made to it. Explore the [`www/index.html`](www/index.html) file. Can you spot which type of request your website performs?
- Connect the static site to the API Gateway endpoint.

### Check your understanding

You've set up your first Serverless backend, congratulations on the hard and great work!
Here are some questions to help you deepen your understanding of what you've built:

- Is API Gateway the only way of invoking a Lambda function?
- What are the advantages of using API Gateway?
- Could you invoke a Lambda function directly?

Feel free to play around and try things out. 

## Bonus

### Improve your CI-CD pipeline

Think about what could have been improved in this project:

- Are there any drawbacks to putting both the CI and CD bits in one single `Jenkinsfile`? Can you find a way to put them in separate scripts but preserve the automatic deployment behaviour?
- Is there another way in which you could have created the API Gateway and your Lambda function rather than manually through the AWS Console?

### Monitoring and logging

Configure your Serverless backend so that you can monitor and view logs for it in [AWS CloudWatch](https://aws.amazon.com/cloudwatch/).

### Look ahead

If you have some extra time this week, start reading and getting familiar with Infrastructure Management and Orchestration using **Terraform**.
What benefits do you see it can bring to a larger project or even to this one?

## Documentation

### Project files

- Under the `www` folder, there are two files: `index.html` and `error.html`. These are the files we will deploy for our static website on an AWS S3 Bucket.
- `deploy_ec2_network_v1.json` is the [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) template to automate the process of creating an EC2 instance on AWS, assign the necessary roles and policies and add some security settings that are needed for Jenkins to be able to run on the EC2 instance. Note that you do not need to know what the whole template does line by line. We will, in fact, spend some more time next week working with these concepts on AWS.
- `your-first-lambda.py` is the Lambda function that you will deploy in AWS and eventually invoke once you deploy your static website on AWS. Modify it to include the names of your group members.
- `sample_unit_test.py` contains some sample unit tests and will serve you to test your CI job in Jenkins. One or more of the tests are failing at the moment. The framework used for the tests is [unittest](https://docs.python.org/3/library/unittest.html)
- `assets` folder: files in this folder doesn't need to be deployed. It contains support assets for this README (e.g. images).

## Supporting Materials

- [AWS S3 Bucket](https://aws.amazon.com/s3/)
- [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
- [Jenkins on AWS](https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/)
- [Jenkins: Creating your first pipeline](https://www.jenkins.io/doc/pipeline/tour/hello-world/)
- [Automating Continuous Integration through Jenkins](https://dev.to/alakazam03/automating-continuous-integration-through-jenkins-448b)
- [Using AWS Lambda with Amazon API Gateway](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html)

### Additional Resources

- [Terraform](https://www.terraform.io/docs/index.html)
