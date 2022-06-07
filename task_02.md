# Set up Jenkins

## Objectives

Learn to:
- Use a fundamental AWS service: EC2
- Use SSH to connect to a virtual machine in the Cloud
- Install a software on a virtual machine in the Cloud
- Understand the benefits of hosting developer tools in the Cloud

## Getting started

Set up an [EC2 instance](https://docs.aws.amazon.com/ec2/index.html) using the [CloudFormation]((https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)) [template](deploy_ec2_network_v1.json) provided in this repo and install Jenkins on it.

> :information_source: The Jenkins-related tasks are likely to take some time and dedicated research. It is also likely that you encounter some obstacles along the way, so this is a great chance to get hands-on and sharpen your debugging skills by finding and reading through logs and error messages. You can do this!

## A few tips

1. The template is made to work pretty much as is. The *only section you need to modify* is the identifier for the S3 bucket you created previously. Can you spot where you need to add it?
2. Using the template, you will need to create something called a **stack** using the CloudFormation template on AWS.
3. You will know you have successfully installed Jenkins if when you open the **public IPv4 DNS address** of your EC2 instance in the browser, you get a `Getting Started` page with the following title: `Unlock Jenkins`.
4. Once you've unlocked Jenkins, install the plugins it recommends.

## Check your understanding

Jenkins can in fact run on your local machine, so why bother setting up an EC2 instance for Jenkins to run on it?

:pencil: Have a group discussion and think about the advantages and disavantages of each of these approaches before you move on.
Submit your answers to a coach for feedback.

## Resources

- [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
- [Jenkins on AWS](https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/)

## Done?

[Go to the next task](task_03.md)