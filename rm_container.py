import json
import boto3

def lambda_handler(event, context):
    
    ssm_client = boto3.client('ssm', region_name='ap-south-1')
    
    command = f"sudo docker rm -f $(sudo docker ps -q | awk 'FNR <= 1 {{print}}')"
    
    params = {
        "commands": [command]
    }
    
    response = ssm_client.send_command(
        DocumentName="AWS-RunShellScript",
        InstanceIds=["i-0b1b5389145225917"],
        TimeoutSeconds=600,
        Parameters=params
    )
    
    print(response)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Removed Docker Container!')
    }
