import boto3

# Create an S3 client
s3 = boto3.client('s3')

def upload():
    # Set the name of the bucket and name of the file in S3
    bucket_name = 'bucket-name'
    file_name = 'file-name'

    # Upload the file to S3
    s3.upload_file(file_name, bucket_name, file_name)

    print("File uploaded successfully!")

def retrieve():

    # Configure the bucket and the object key
    bucket_name = 'my-bucket'
    object_key = 'path/to/myfile.txt'

    # Download the file
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    content = response['Body'].read().decode('utf-8')

    # Print the contents of the file
    print(content)

upload()

retrieve()
