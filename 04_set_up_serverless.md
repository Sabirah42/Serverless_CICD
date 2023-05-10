# Set up the Serverless backend

## Objectives

Learn to:
- Use AWS Lambda and API Gateway to build a Serverless API backend.

## Task: Diagram the backend

> :warning: Before moving on to this task, make sure you have successfully
> deployed the HTML files to the S3 Bucket. 

Now that automatic deployment of the static site works, the next task is to make
it dynamic by building a backend to which the frontend site can make requests.

For this we're going to use AWS Lambda. This is a type of cloud platform called
serverless, or functions-as-a-service (FaaS). Instead of starting a whole
virtual computer, or a container, we just tell AWS to run one specific function
when we tell it to.

We'll also use AWS API Gateway, which is a service that allows us to create an
HTTP endpoint URL that will invoke (run) our Lambda function.

Revisit your diagram again.

![Application diagram](assets/application_diagram.jpg?raw=true "Application
diagram")

Can you flesh out your understanding of the connection between the static site,
API Gateway and AWS Lambda?

Where could you look to figure out what kind of requests and responses the
arrows represent? Improve this diagram as you learn more.

## Task: Set up the Serverless backend

Your task is to make the button in your `index.html` render some text on the
page by setting it up to call an AWS Lambda function, and then displaying the
response.

You're welcome to work this through yourself, but I've broken down the key steps
below.

## Key Steps

1. **Create an AWS Lambda function.**  
   You can find AWS Lambda in the AWS Console. Set it to use the Python runtime.

2. **Copy in the code from `resources/your-first-lambda.py`.**  
   You can find it in this repository, and copy it directly into the AWS Lambda
   coding interface. You should see this after you've created the lambda, though
   you may need to scroll down.

3. **Deploy the Lambda function.**  
   You can do this by clicking the 'Deploy' button in the top right. You'll need
   to do this every time you make a change to the code.

4. **Test the Lambda function.**  
   You can do this by clicking the 'Test' button in the top right. It will
   prompt you to create an event. If you needed to give parameters to your
   event, you would do it here. But we don't, so we won't — just create it.

   You can then click 'Test' again, and you should see the output of the
   function.

5. **Create an API Gateway endpoint.**  
   This is another area of AWS. Select 'HTTP API', and then 'Lambda' as the
   integration. Then you'll be able to select your Lambda function. After this,
   make it a GET request and whatever path you'd like. Move through to create
   it.

6. **Try it out manually.**  
   Open up your terminal and call your new API endpoint. For me this was:

   ```shell
   ; curl https://4d45w6bn66.execute-api.eu-west-2.amazonaws.com/myCicdLambda
   ```

   You can find the domain under 'Invoke URL' and the route is the one you
   specified earlier. If you need a reminder, you can go to 'Develop -> Routes'.

7. **Set up CORS.**  
   Browsers have security settings to prohibit websites from sending requests to
   other websites. However they also have a mechanism to selectively allow this.
   This is called CORS, or Cross-Origin Resource Sharing.

   Go to Develop -> CORS -> Configure. 
   
   Under 'Access-Control-Allow-Origin' add the URL of your static site
   (including the protocol, e.g.
   `http://my-static-site.s3.eu-west-2.amazonaws.com`).

   Under 'Access-Control-Allow-Methods' add `GET`, since that't the request type
   we've set up our lambda to use.

   Under 'Access-Control-Allow-Headers' add `content-type`, since our requester
   will need to specify what types of responses it is expecting.

   Then click 'Save'.

8. **Update your `index.html` to call the lambda.**  
   There's a space for the URL to your lambda in the `index.html` file. Replace
   the placeholder with the URL of your API Gateway endpoint.

   Assuming your CI-CD process is working smoothly, you can push your changes,
   see it run, and then go visit the website.

## Check your work

If you've done everything correctly, when you click the button on your website
you should see the message from the lambda function come up and the picture
change.

Well done! You've completed all the core material for this module.


[Next Challenge](05_bonus.md)

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=04_set_up_serverless.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=04_set_up_serverless.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=04_set_up_serverless.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=04_set_up_serverless.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fserverless-cicd&prefill_File=04_set_up_serverless.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
