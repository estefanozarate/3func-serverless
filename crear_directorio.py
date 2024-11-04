import json
import boto3

def lambda_handler(event, context):
    # Verificar que se recibe el cuerpo de la solicitud
    if 'body' not in event or event['body'] is None:
        return {
            "statusCode": 400,
            "body": json.dumps("Bucket name is required")
        }

    # Obtener el cuerpo directamente si ya es un dict
    body = event.get('body')

    # Si el cuerpo es un string, deserialízalo
    if isinstance(body, str):
        body = json.loads(body)

    # Obtener los parámetros del cuerpo
    bucket_name = body.get('bucket_name')
    directory_name = body.get('directory_name')

    if not bucket_name:
        return {
            "statusCode": 400,
            "body": json.dumps("Bucket name is required")
        }

    # Crear cliente S3
    s3 = boto3.client('s3')

    # Crear un "directorio" en S3 (en realidad, un prefijo con una barra final)
    s3.put_object(Bucket=bucket_name, Key=(directory_name + '/'))

    return {
        "statusCode": 200,
        "body": json.dumps(f"Directory '{directory_name}' created in bucket '{bucket_name}'.")
    }

