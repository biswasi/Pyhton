import json
import boto3

def lambda_handler(event, context):
   client = boto3.client('sns')
   Topic_ARN = "arn:aws:sns:us-east-1:166607322176:ReminderTopic"
   response_one = client.publish (
      TargetArn = Topic_ARN,
      Message = json.dumps({'Reminder-Type': "Weekly Reminder", 'Reminder': "Reminder 1 for email", 'Destination': "Email" }),
   )
   response_two = client.publish (
      TargetArn = Topic_ARN,
      Message = json.dumps({'Reminder-Type': "Weekly Reminder", 'Reminder': "Reminder 2 for email", 'Destination': "Email"}),
   )
   response_three = client.publish (
      TargetArn = Topic_ARN,
      Message = json.dumps({'Reminder-Type': "Daily Reminder", 'Reminder': "Reminder 3 from IB", 'Destination': "SQS"}),
   )
   return {
      'statusCode': 200,
      'body': json.dumps({'response_one': response_one, 'response_two': response_two, 'response_three': response_three })
   }
