import json
import boto3

def lambda_handler(event, context):
    # Obtener el nombre del bucket directamente del evento
    body = event.get('body')  # Esto podría ser un diccionario o un string
    if isinstance(body, str):
        body = json.loads(body)  # Convertir solo si es un string

    # Obtener el nombre del bucket del cuerpo
    bucket_name = body.get('bucket_name')
    
    if not bucket_name:
        return {
            'statusCode': 400,
            'body': json.dumps("Bucket name is required")
        }

    s3 = boto3.client('s3')

    try:
        # Crear el bucket
        s3.create_bucket(Bucket=bucket_name)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Bucket {bucket_name} created successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }


