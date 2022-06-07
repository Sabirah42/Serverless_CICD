# Set up the Serverless backend

## Objectives

Learn to:
- Use AWS Lambda and API Gateway to build a Serverless API backend.

## Getting started

Now that automatic deployment of the static site works, the next task is to make it dynamic by building a backend to which the frontend site can make requests.

> :warning: Before moving on to this task, make sure you have successfully deployed the HTML files to the S3 Bucket. 

## Diagramming the backend

Revisit your diagram again. What services will you need to research next?

![Application diagram](assets/application_diagram.jpg?raw=true "Application diagram")

Can you flesh out your understanding of the connection between the static site, API Gateway and AWS Lambda?

Where could you look to figure out what kind of requests and responses the arrows represent?
Improve this diagram as you learn more.

## Tasks

- Using the AWS Lambda service in the AWS Console, set up set up an Python Lambda function whose definition matches the one in the [`your-first-lambda.py`](your-first-lambda.py) file. Do not forget to modify it!
- Set up an API Gateway **endpoint** which, will **invoke** the Lambda function you created whenever a request is made to it. Explore the [`www/index.html`](www/index.html) file. Can you spot which type of request the website performs?
- Connect the static site to the API Gateway endpoint.

## Check your understanding

You've set up your first Serverless backend, congratulations on the hard and great work!
Here are some questions to help you deepen your understanding of Serverless architectures and AWS Lambda:

- Is API Gateway the only way of invoking a Lambda function? Could you invoke a Lambda function directly? 
- What are the advantages of using API Gateway? Do some research and discuss what you find with a peer, the cohort or a coach.

Feel free to play around and try things out. 

## Resources

- [Using AWS Lambda with Amazon API Gateway](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html)

---

[Go to the next task](task_05.md)