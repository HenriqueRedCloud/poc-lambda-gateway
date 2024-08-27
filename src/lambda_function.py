import json

def lambda_handler(event, context):
    # Log the received event
    print("Received event:", json.dumps(event, indent=2))

    # Extract query parameters
    name = event['queryStringParameters'].get('name', 'World')

    # Create a response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': f'Hello, {name}!'})
    }

    return response
