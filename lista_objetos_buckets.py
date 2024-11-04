# lista_objetos_bucket.py
import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    # Aquí, usamos event['body'] directamente sin json.loads()
    body = event['body']  # Esto ya debería ser un dict

    # Extraemos el nombre del bucket
    bucket_name = body.get('bucket_name')  # Asegúrate de que esta clave sea correcta

    if not bucket_name:
        return {
            'statusCode': 400,
            'body': json.dumps('Bucket name is required')
        }

    try:
        objects = s3.list_objects_v2(Bucket=bucket_name)
        object_keys = [obj['Key'] for obj in objects.get('Contents', [])]
        return {
            'statusCode': 200,
            'body': json.dumps(object_keys)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error listing objects: {str(e)}')
        }

