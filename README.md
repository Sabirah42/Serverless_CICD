# serverless-cicd

This repository provides a skeleton with some files in order for you to get started creating your own CI-CD solution using Jenkins and to create your first AWS Lambda following a common pattern in the industry.

## Desired application diagram

![Application diagram](assets/week2-serverless-cicd.jpg?raw=true "Application diagram")

## Project files

- Under the `www` folder, there are two files: `index.html` and `error.html`. These are the files we will deploy for our static website on an AWS S3 Bucket.
- `deploy_ec2_network_v1.json` is the [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) template to automate the process of creating an EC2 instance on AWS, assign the necessary roles and policies and add some security settings that are needed for Jenkins to be able to run on the EC2 instance. Note that you do not need to know what the whole template does line by line. We will, in fact, spend some more time next week working with these concepts on AWS.
- `your-first-lambda.py` is the Lambda function that you will deploy in AWS and eventually invoke once you deploy your static website on AWS. Modify it to include the names of your group members.
- `sample_unit_test.py` contains some sample unit tests and will serve you to test your CI job in Jenkins. One or more of the tests are failing at the moment. The framework used for the tests is [unittest](https://docs.python.org/3/library/unittest.html)
- `assets` folder. Just support assets for the project (e.g. images). Feel free to add your own when you fork the repo :smile:

## Tasks

### Create an S3 Bucket for your static website on AWS
- S3 is an [Object storage](https://cloud.netapp.com/blog/block-storage-vs-object-storage-cloud) service by AWS. Then, you may be wondering how is it possible that such service can host a static website. You will need to find out how you can enable your bucket to host a static website.

### Setting up Jenkins on an EC2 instance (server)

:information_source: This and the following few tasks related with Jenkins and CI/CD are likely to take some time and dedicated research. It is also likely that you encounter some pebbles (if not stones!) along the way, so this is a great chance to get hands-on and sharpen your debugging skills, read through logs and error messages. You can do this!

- Jenkins can in fact run on your local machine, so why bother really setting up an EC2 instance for Jenkins to run on it?
:pencil: Have a group discussion and think about the advantages and disavantages of each of these approaches before you move on.

- In order to create your EC2 instance with all it needs for you to set up Jenkins, take a look at the `CloudFormation` template added in the project. The template is made to work pretty much as is. The *only section you need to modify* is the identifier for the S3 bucket you created previously. Can you spot where you need to add it?

Then, create a new **stack** based on your CloudFormation template on AWS.

- Install and configure Jenkins on your EC2 instance. You will first need to connect to your EC2 instance. There are several ways to achieve this, you can find an example [here](#supporting-materials).

- You will know you have successfully installed Jenkins after you open your `EC2 instance public http url` on the browser and you get a `Getting Started` window with the following title: `Unlock Jenkins`.

- Once you get to this stage, research how you can gain access to the Jenkins home screen (and I suggest you install the plugins that Jenkins recommends).

### Create new Jenkins item

- Once Jenkins is fully set up. It is time to add a `New Item`. The one we will use for this project will be of type `Pipeline`, and not a freestyle project!

### Add a webhook for GitHub to notify Jenkins

- Now you have successfully installed Jenkins, excellent work! The next step is to figure out how your GitHub repository is going to contact your Jenkins instance when an `event` occurs. And which events should be taken into account? Some of them? All of them?

### Add CI to your project
- Now that you know what CI is. What sort of steps do you think you should include in your Jenkins job (aka `Jenkinsfile`)? What sort of checks should you include before your application is deployed to the Cloud?
- Remember that, ultimately, the idea is for your job to pass all the necessary checks before moving to the CD task.

That's great! But, shouldn't Jenkins have some sort of access to my GitHub repository to access the application files? Maybe you're right! Research the following and discuss in your group: `Jenkins credentials`.

:exclamation: Important: Regarding the above, the only credentials that we are seeking to set are those that will allow Jenkins to succesfully connect to our project GitHub repo :grinning: - So please do not set any sort of Cloud Credentials in Jenkins for you as users of your Jenkins server.

### Add CD to your project
- Great job! Now you have a green CI job, the next step is to be able to deploy your application to the S3 bucket you created initially.

### AWS Lambda

Before moving on to this task, make sure you have successfully deployed your `html` files to your S3 Bucket.

- On the AWS Console, access the AWS Lambda service and create a Python Lambda function whose definition matches the one in the `your-first-lambda.py` file. Do not forget to modify it!

Great job! You've created your first Lambda function on AWS, how exciting! Now you may be wondering, okay, how do we `invoke` it?

### API Gateway

You've reached the last task of the week project, congratulations on the hard and great work! You have a general idea about the purpose of API Gateway from the session on Monday and the diagram. We will use API Gateway on AWS to invoke our Lambda function, however:

- Is this the only way of invoking a Lambda function?
- What are the advantages of using API Gateway?
- Could you invoke a Lambda function directly?

The final task is to create an API Gateway `endpoint` that you can consume in order to invoke your Lambda function.

:bulb: Explore the `www/index.html` file. Can you spot which type of request you should perform?

For an extra stretch, feel free to add additional settings like `metrics` and `logging` to your API Gateway endpoint. You can monitor these on `AWS CloudWatch`.

## Bonus

Think about what could have been improved in this project:
- Is it considered best practice to add both the CI and CD bits in one single script?
- Is there another way in which you could have created the API Gateway and your Lambda function rather than manually through the AWS Console?

Finally, if you have some extra time this week, start reading and getting familiar with Infrastructure Management and Orchestration (using `Terraform`). What benefits do you see it can bring to a larger project or even to this one?

### Supporting Materials

- [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
- [Installing Jenkins](https://www.jenkins.io/doc/book/installing/linux/)
- [Setting up Jenkins on AWS](https://dev.to/alakazam03/setting-up-jenkins-on-aws-21pf)
- [Jenkins: Creating your first pipeline](https://www.jenkins.io/doc/pipeline/tour/hello-world/)
- [Automating Continuous Integration through Jenkins](https://dev.to/alakazam03/automating-continuous-integration-through-jenkins-448b)
- [Using AWS Lambda with Amazon API Gateway](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html)

### Additional Resources

- [AWS S3 Bucket](https://aws.amazon.com/s3/)
- [Terraform](https://www.terraform.io/docs/index.html)
