def lambda_handler(event, context):
    print("Inside the lambda handler")

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "name1, name2, name3 & name4! You have successfully invoked your first Lambda. Great job!"
    }

    return response