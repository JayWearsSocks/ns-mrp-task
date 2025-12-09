import json

methodNotAllowedResponse = {
    'statusCode': '405',
    'body': 'Method Not Allowed',
    'headers': {
        'Allow': 'POST',
        'Content-Type': 'application/json',
    },
}

okResponse = {
    'statusCode': '200',
    'body': 'OK',
    'headers': {
        'Content-Type': 'application/json',
    },
}

def badRequestResponse(message): 
    return {
        'statusCode': '400',
        'body': message,
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def handlePost(body):
    requiredFields = ['saleId', 'saleMessage']
    missingFields = [ field for field in requiredFields if (field not in body)]
    if len(missingFields) > 0:
        return badRequestResponse('Missing field(s): {}'.format(missingFields))

    return postSale(body['saleId'], body['saleMessage'])


def postSale(saleId, saleMessage):
    print("Received request with saleId: {id} and saleMessage: {msg}".format(id=saleId, msg=saleMessage))

    # To do: write to database
    return okResponse


def lambda_handler(event, context):
    '''
    Require event to have 'httpMethod' and 'body' 
    Accept only 'POST' as httpMethod
    Require fields 'saleId' and 'saleMessage' in body
    '''
    if 'httpMethod' not in event:
        return badRequestResponse('Missing http method in event')

    elif event['httpMethod'] == 'POST':
        if 'body' not in event:
            return badRequestResponse('Missing request body')
        return handlePost(event['body'])

    else:
        return methodNotAllowedResponse
