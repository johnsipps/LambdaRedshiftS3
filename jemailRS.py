# -*- coding: utf-8 -*-
"""
Created on Wed May 23 03:56:51 2018

@author: John
"""
import boto3
from botocore.exceptions import ClientError
    
def main(value):

    SENDER = "Sender Name <Sender@gmail.com>"
    #print(SENDER)
    RECIPIENT = "recepient@gmail.com"
    AWS_REGION = "us-east-1"
    SUBJECT = "S3:Redshift Triggered- Email notification"
    BODY_TEXT = ("Amazon S3 Put -Redshift automation\r\n"
				"This email was sent with Amazon SES.\r\n" 
				"Table read !.. \r\n Regards, John \r\n"
				)
    BODY_HTML = """<html>
        		<head></head>
				<body>
				<h1>Amazon S3 Put -Redshift automation (Python)</h1>
				<p>This email was sent with Amazon SES! </p>
				<p> Table  """ + value + """
				read successfully ! </p>
					<p> Regards, John</p> 
				</body>
				</html>
							"""       
	
	# The character encoding for the email.
    CHARSET = "UTF-8"
    
    client = boto3.client('ses',region_name=AWS_REGION)
	# Create a new SES resource and specify a region.

# Try to send the email.
    print("sending email..")
    try:        
		#Provide the contents of the email.
        response = client.send_email(
                Destination={'ToAddresses': [RECIPIENT,],},
                Message={
				'Body': {
					'Html': {
						'Charset': CHARSET,
						'Data': BODY_HTML,
					},
					'Text': {
						'Charset': CHARSET,
						'Data': BODY_TEXT,
					},
				},
				'Subject': {
					'Charset': CHARSET,
					'Data': SUBJECT,
				},
			},
			Source=SENDER,
			# If you are not using a configuration set, comment or delete the
			# following line
			#ConfigurationSetName=CONFIGURATION_SET,
		)
    
	# Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])
    return 'Hello from Lambda'