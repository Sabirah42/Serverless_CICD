# Set up a CI-CD pipeline in Jenkins

## Objectives

Learn:
- To design a CI-CD pipeline
- To build a CI-CD pipeline using Jenkins
- To interact with AWS using the command line
- How to connect different developer tools to each other in order to automate
  the software development lifecycle
- To debug connectivity issues between tools running in the Cloud

## Task: Create a diagram of your desired pipeline

Previously we mentioned how a CI-CD pipeline involves running tests and checks
on our codebase, and then if those tests pass deploying the code to a production
cloud environment.

Our application is a static website, so we don't have any unit tests for it.
Instead, we're going to use the Javascript tool `html-validate` to check that
our HTML is valid. If, and only if, these checks pass without any errors, we
want to deploy our application to an S3 bucket.

These sorts of checks are a powerful way to improve quality in the systems in
our care, as they will run automatically and help our teams to catch issues
before they get to production. The app not deploying is a pretty strong
incentive to fix the problem!

Before we get started, take a moment to diagram out in more detail what this
pipeline is going to have to do, and in what order.

Here's a starting point:

![Deployment process diagram](assets/deployment_process_diagram.jpg?raw=true
"Deployment process diagram")

Copy out this diagram and add some detail to what Jenkins will need to do.

> :information_source: The resources shared with you during the [CI-CD
> workshop](https://github.com/makersacademy/devops-course/blob/main/workshops/week-2/ci_cd_overview.md)
> might help with this.

## Task: Set up the pipeline

Your task is to set up a CI-CD pipeline in Jenkins according to your design.

You should expect this task to be challenging, and to require significant
research and exploration. You may find out part way through that you need to
change your approach. This is all OK and expected.

Nevertheless, I've broken down the key steps below along with some resources
for you to use. You can try to follow the below closely, or discard it and find
your own way.

## Key steps

1. **Set up a new local git repository for your static website project.**
   Copy the files from `template/` to a new directory outside of this one and
   set it up as a local git repository.

2. **Push your local repository to a new, private Github repository.**  
   Why private? Public will make it easier, but you will be missing some key
   learning for this module, as most repositories in your jobs will be private.

3. **Create a new pipeline in Jenkins.**

4. **Add a pipeline script.**  
   This script should:
   
   1. Clone your repository using the right credentials (more below)
   2. Set up NodeJS to run the checks.
   3. Install the NodeJS dependencies.
   4. Run the checks using `npm run check`.
   5. If and only if the tests pass, deploy the HTML files to S3.

   You are welcome to attempt this work yourself, _however you will encounter
   significant challenges._ These are thrilling challenges representative of
   what your work will be like as a cloud engineer, so if you feel ready I
   absolutely recommend you go for it.

   However, if you are feeling pretty stretched already, I recommend you instead
   use the sample script in the [Resources Section](#resources), which should
   work without too much trouble.

5. **Add your Github credentials.**  
   Jenkins won't magically know your details to access your private repository,
   so you need to provide it with some. You can add these in Manage Jenkins ->
   Credentials -> Global -> Add Credentials.

   Select "Username with password" as the kind.  Put your Github username in the
   'Username' field. Don't put in your Github password to the password field —
   it won't work.
   
   You'll then need to go to Github, finding Settings -> Developer Settings ->
   Personal Access Tokens -> Fine Grained Tokens -> Generate new token.

   The token you're generating will give Jenkins access to perform certain
   actions on your behalf. According to the principle of least privilege (agents
   in a system should have the least permissions necessary to perform their
   work) you should endeavour to give the token permissions _only_ to your
   repository, and _only_ those permissions necessary. These are: 

   * Repository Permissions -> Commit statuses: Read and Write
   * Repository Permissions -> Contents: Read-only
   * Repository Permissions -> Metadata: Read-only

   Generate the token, and then put it in the Password field of your Jenkins
   credentials form. Then hit Create.

   Once you've done this, you'll see that your credential gets an ID. Copy this
   ID and enter it into your pipeline script (if you're using the sample, this
   is called `your-git-credentials-id`)

6. **Try running your pipeline.**  
   Go to your pipeline and click 'Build Now'. If everything's working right,
   this should run 'Clone Repo' and 'Install Dependencies' successfully, and
   then fail at 'Run HTML Check' with some errors about invalid HTML. 
   
   This is good — your check is properly failing and your pipeline is now
   failing.

7. **Fix the HTML.**  
   Fix the HTML, push your changes, and then run the build again. Keep going
   until the 'Run HTML Check' step is green.

   If you'd like to run the checks locally to help you fix them without the full
   cycle, you can install node yourself and then follow the instructions in the
   README.

   Fixing the HTML will take some research, but will teach you a little about
   validation and accessibility too.

   Note that the button won't do anything until later in the challenges.

8. **Add your AWS credentials.**  
   Now that our checks have passed, we see that our deployment is failing. We
   need to add our AWS credentials and the details of our bucket.

   Once more, we should think of the principle of least privilege. We don't want
   to give Jenkins a token that will enable it to do anything nefarious on our
   account. If there was a security vulnerability in Jenkins, this could be very
   nasty.

   In AWS, go to IAM and create a new User Group. We'll add permissions to this
   group directly by going to Permissions -> Add permissions -> Create inline
   policy.

   You want to design a policy that will allow Jenkins permissions to push your
   project to the specific S3 bucket you created earlier. There's a sample
   permissions document in the [Resources](#resources) section if you'd like
   to use it, otherwise you can research and write your own.

   After your User Group is set up, create a new User and add it to the User
   Group you created. Then, open your User and go to Security Credentials ->
   Access Keys -> Create access key -> Other -> Next. Then copy out the Access
   Key ID and the Secret Access Key. **Keep these private, only upload them to
   Jenkins, and then delete them from your computer.**

   Creating the new credential is similar to the Github credential, except you
   should select 'AWS Credentials' rather than 'Username and Password'.

   After this, put the credential ID into the pipeline script as before, and add
   in the name of your S3 bucket too.

9. **Run your build.**  
   After this, your build should pass and you should be able to see the web page
   visible on your S3 bucket.

10. **Set up a Github webhook.**  
    Right now you need to run the CI-CD pipeline manually. Typically these
    pipelines run automatically on a change to the main branch. To achieve this
    you will need to tell Github to inform Jenkins when you push new code.

    You'll need to integrate Github with Jenkins using a feature called
    Webhooks.

## Check your work

To check you've got everything working correctly:

1. Make a change to your `index.html`. Perhaps a new picture.
2. Push it to Github.
3. Don't manually run your build on Jenkins, wait for it to kick in automatically.
4. Watch the build go green
5. Load up your website and verify that it has changed.

## Resources

A sample Jenkins pipeline script:

```jenkins
pipeline {
    agent any

    environment {
        GIT_CREDENTIALS = 'your-git-credentials-id'
        AWS_CREDENTIALS = 'your-aws-credentials-id'
        BUCKET_NAME = 'your-bucket-name'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', credentialsId: env.GIT_CREDENTIALS, url: 'https://github.com/YOUR_REPOSITORY_URL'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.2/install.sh | bash
                    . ~/.nvm/nvm.sh
                    nvm install 16
                    nvm use 16
                    npm install
                '''
            }
        }

        stage('Run HTML Check') {
            steps {
                sh '''
                    . ~/.nvm/nvm.sh
                    npm run check
                '''
            }
        }

        stage('Deploy to S3') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', credentialsId: env.AWS_CREDENTIALS, secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    sh 'aws s3 sync . s3://${BUCKET_NAME}/ --exclude "*" --include "*.html"'
                }
            }
        }
    }
}
```

A sample policy for your User Group:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "BucketPolicy0",
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObjectAcl",
                "s3:GetObject",
                "s3:ListBucket",
                "s3:DeleteObject",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "arn:aws:s3:::kaylack-serverless-cicd",
                "arn:aws:s3:::kaylack-serverless-cicd/*"
            ]
        }
    ]
}
```

## Done?

[Go to the next task](04_set_up_serverless.md)


[Next Challenge](04_set_up_serverless.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=03_set_up_pipeline.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=03_set_up_pipeline.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=03_set_up_pipeline.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=03_set_up_pipeline.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=03_set_up_pipeline.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
