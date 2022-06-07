# Set up a CI-CD pipeline in Jenkins

## Objectives

Learn to:
- Design a CI-CD pipeline
- Build a CI-CD pipeline using Jenkins
- Interact with AWS using the command line
- Automate the software development lifecycle by connecting different developer tools to each other

## Create a diagram of your desired pipeline

Consult your diagrams again and revisit what you have learned so far about CI-CD pipelines and their benefits.
- What checks and actions should your CI-CD pipeline perform?
- When should these checks and actions be run?

Remember that ultimately, the idea is for the pipeline to only proceed to deploying the code if the checks pass.

![Deployment process diagram](assets/deployment_process_diagram.jpg?raw=true "Deployment process diagram")

If you haven't already, expand the diagram above so that it illustrates in more detail what should happen in the "Jenkins" step.
This will give you a better idea of what you want to use Jenkins for and help you research the right things.

> :information_source: The resources shared with you during the [CI-CD workshop](https://github.com/makersacademy/devops-course/blob/main/workshops/week-2/ci_cd_overview.md) might help with this.

## Set up the pipeline

Below you will find a high-level list of the tasks that are necessary for you to sucessfully set up the Jenkins pipeline in CI-CD.

- Using the Jenkins classic UI, set up a new [Pipeline project](https://www.jenkins.io/doc/book/pipeline/).
- Give Jenkins access to your GitHub repository by giving Jenkins the right **credentials**.
- Using a **webhook**, set up GitHub to automatically trigger your pipeline. What events should ideally trigger your pipeline to run?
- By writing a `Jenkinsfile`, set up the CI part of your pipeline. It should run checks to make sure the code in your repository is good to be deployed.
- Extend the `Jenkinsfile` with a step that deploys the application to the S3 bucket you created initially. 

Once successfully deployed the static website should show the message "Hello all! What happens when you click on the button below?" and a button that says "Click me".

> :information_source: Not all of the tasks above need to be completed in the exact order they are given here.  Guides you may come across in your research might go through these in a slightly different order. So don't worry if you end up deviating from the order presented here.

## Check your understanding

### Understanding the `Jenkinsfile`

You've created a `Jenkinsfile`, but do you know how it works?
Spend some time understanding each line in the file and adding explanatory comments to it.

Here are a few questions to ask yourself and try to answer through a bit of research if need be:

- On what machine do the commands in your Jenkinsfile run?
- What part of your `Jenkinsfile` ensures that the correct version of Python will be available to run the code? How?
- What does the `stage` keyword mean? How does it relate to the diagram you drew to illustrate the CI-CD pipeline you planned?

<details>
<summary><b>Had a go?</b> Check your answers here.</summary>

Below is a `Jenkinsfile` similar to the one you might have written. The important bits are annotated.

If you have some questions or uncertainties left after comparing this with what you found in your research, do bring them up to a coach! 


```Groovy
pipeline {
    // Defines the default "agent" that should be used to run the commands in the rest of this file.
    // A Jenkins agent is the entity that actually executes the commands you specify in the pipeline.
    // Agents run on a (virtual) machine or Docker container.
    // Specifying "any" means that Jenkins will use any available agent.
    // Because we haven't explicitly configured any other way of running agents,
    // Jenkins will use the machine it is installed on to run agents.
    // In this case that means commands will be executed on the EC2 instance we installed Jenkins on.
    agent any

    stages {

        // Defines one logical "piece" of the pipeline called "test".
        // We could have called it something else too.
        // The name can be anything we want but it's best to make it descriptive of what it's meant to achieve.
        stage('test') { 

            // All commands run in this stage will run inside a container based on the python:3.5.1 Docker image. 
            // The Docker container will be spun up by Jenkins automatically. 
            // If we didn't run this step in a Docker container,
            // we'd have to make sure that Python is installed on the EC2 instance
            // so that we can use the `python` command later on to run tests. 
            // Using Docker is any easy way of making sure our commands run in the right environment.
            agent { docker { image 'python:3.5.1' } }

            // This block contains the commands that we want to execute during the "test" part of the pipeline. 
            // The exact commands that go in here are up to us.
            // If any command in this block returns an error, the pipeline fails and stops running.
            steps {

                // The `sh` bit tells Jenkins to run this command inside a shell.
                // The rest of this line is the command needed to get our tests to run. 
                sh 'python sample_unit_test.py'
            }
        }

        // Defines a second piece of the pipeline called "deploy".
        // This stage runs if and only if the previous stage succeeded. 
        stage('deploy') {

            // This step doesn't define an agent to use so it will
            // use the agent specified at the start of the file, i.e. the EC2 instance.
            steps {

                // Uses the AWS CLI to upload all files under www/ to to S3
                sh 'aws s3 cp www/ s3://serverless-cicd.simo.makers.tech --recursive'
            }
        }
    }
}
```

Learn more here:

- [Using Jenkins agents](https://www.jenkins.io/doc/book/using/using-agents/)
- [Pipeline syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
</details>

### How does Jenkins get access to S3?

Via what mechanism did you give Jenkins access to make changes to your S3 bucket? 
Why did you need to do so? 

Illustrate the high-level process by which Jenkins is granted access to S3 on the deployment diagram.
Don't worry about understanding the AWS mechanisms behind this in full detail.
You'll be covering that in a future module!

## Resources

- [Jenkins: Creating your first pipeline](https://www.jenkins.io/doc/pipeline/tour/hello-world/)
- [Automating Continuous Integration through Jenkins](https://dev.to/alakazam03/automating-continuous-integration-through-jenkins-448b)

## Done?

[Go to the next task](task_04.md)