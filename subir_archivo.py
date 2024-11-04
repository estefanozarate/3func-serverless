import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Para depurar el evento que se recibe
    print("Received event:", json.dumps(event))

    bucket_name = event.get('bucket_name')
    file_name = event.get('file_name')
    file_content = event.get('file_content')

    # Verificación básica de parámetros
    if not bucket_name or not file_name or file_content is None:
        return {
            'statusCode': 400,
            'body': json.dumps('Bucket name, file name, and file content are required')
        }

    try:
        # Sube el objeto directamente al bucket
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content.decode('base64'))  # Decodificamos el contenido
        return {
            'statusCode': 200,
            'body': json.dumps(f'File {file_name} uploaded successfully to {bucket_name}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading file: {str(e)}')
        }

