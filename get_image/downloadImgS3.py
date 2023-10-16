import boto3
import requests

# Replace with your AWS credentials
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_REGION = ''
AWS_BUCKET = ''
IMAGE_URL = ''
DOMAIN = ''

# Initialize the S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY, region_name=AWS_REGION)

# URL of the image in S3
image_key = IMAGE_URL.replace(DOMAIN, '')


try:
    # Sử dụng client S3 để tải hình ảnh từ bucket
    response = s3.get_object(Bucket=AWS_BUCKET, Key=image_key)

    # Đọc nội dung của hình ảnh từ response
    image_data = response['Body'].read()

    # Lưu hình ảnh vào file
    with open('downloaded_image.jpg', 'wb') as image_file:
        image_file.write(image_data)

    print("Hình ảnh đã được tải về và lưu thành công")
except Exception as e:
    print("Lỗi:", e)
