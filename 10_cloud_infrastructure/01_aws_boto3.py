"""
AWS와 boto3
=====================================
Python으로 AWS 서비스 사용하기
pip install boto3
"""

# =============================================================================
# 1. boto3 설정
# =============================================================================

"""
AWS 자격 증명 설정 방법:

1. 환경 변수
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   export AWS_DEFAULT_REGION=ap-northeast-2

2. ~/.aws/credentials 파일
   [default]
   aws_access_key_id = your_access_key
   aws_secret_access_key = your_secret_key

3. ~/.aws/config 파일
   [default]
   region = ap-northeast-2

4. 코드에서 직접 (비권장)
   boto3.Session(
       aws_access_key_id='xxx',
       aws_secret_access_key='xxx',
       region_name='ap-northeast-2'
   )
"""

import boto3
from botocore.exceptions import ClientError

# =============================================================================
# 2. S3 (Simple Storage Service)
# =============================================================================

"""
# S3 클라이언트 생성
s3 = boto3.client('s3')

# 버킷 목록
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f"Bucket: {bucket['Name']}")

# 버킷 생성
s3.create_bucket(
    Bucket='my-bucket-name',
    CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-2'}
)

# 파일 업로드
s3.upload_file('local_file.txt', 'my-bucket', 'remote_file.txt')

# 파일 다운로드
s3.download_file('my-bucket', 'remote_file.txt', 'downloaded.txt')

# 파일 목록
response = s3.list_objects_v2(Bucket='my-bucket')
for obj in response.get('Contents', []):
    print(f"  {obj['Key']} - {obj['Size']} bytes")

# 파일 삭제
s3.delete_object(Bucket='my-bucket', Key='remote_file.txt')

# 사전 서명된 URL 생성 (임시 접근 URL)
url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': 'my-bucket', 'Key': 'file.txt'},
    ExpiresIn=3600  # 1시간
)
"""


# S3 유틸리티 클래스
class S3Manager:
    """S3 작업을 위한 유틸리티 클래스"""

    def __init__(self, bucket_name: str):
        self.s3 = boto3.client('s3')
        self.bucket = bucket_name

    def upload_file(self, local_path: str, s3_key: str) -> bool:
        try:
            self.s3.upload_file(local_path, self.bucket, s3_key)
            return True
        except ClientError as e:
            print(f"Upload error: {e}")
            return False

    def download_file(self, s3_key: str, local_path: str) -> bool:
        try:
            self.s3.download_file(self.bucket, s3_key, local_path)
            return True
        except ClientError as e:
            print(f"Download error: {e}")
            return False

    def list_files(self, prefix: str = "") -> list:
        try:
            response = self.s3.list_objects_v2(
                Bucket=self.bucket,
                Prefix=prefix
            )
            return [obj['Key'] for obj in response.get('Contents', [])]
        except ClientError as e:
            print(f"List error: {e}")
            return []

    def get_presigned_url(self, s3_key: str, expires_in: int = 3600) -> str:
        return self.s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': self.bucket, 'Key': s3_key},
            ExpiresIn=expires_in
        )


# =============================================================================
# 3. DynamoDB
# =============================================================================

"""
# DynamoDB 리소스
dynamodb = boto3.resource('dynamodb')

# 테이블 생성
table = dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {'AttributeName': 'user_id', 'KeyType': 'HASH'},  # 파티션 키
        {'AttributeName': 'email', 'KeyType': 'RANGE'}     # 정렬 키
    ],
    AttributeDefinitions=[
        {'AttributeName': 'user_id', 'AttributeType': 'S'},
        {'AttributeName': 'email', 'AttributeType': 'S'}
    ],
    BillingMode='PAY_PER_REQUEST'
)

# 테이블 참조
table = dynamodb.Table('Users')

# 아이템 추가
table.put_item(Item={
    'user_id': 'user123',
    'email': 'user@example.com',
    'name': 'John Doe',
    'age': 30
})

# 아이템 조회
response = table.get_item(Key={
    'user_id': 'user123',
    'email': 'user@example.com'
})
item = response.get('Item')

# 아이템 업데이트
table.update_item(
    Key={'user_id': 'user123', 'email': 'user@example.com'},
    UpdateExpression='SET age = :val',
    ExpressionAttributeValues={':val': 31}
)

# 쿼리
response = table.query(
    KeyConditionExpression='user_id = :uid',
    ExpressionAttributeValues={':uid': 'user123'}
)

# 스캔 (전체 테이블)
response = table.scan(
    FilterExpression='age > :age',
    ExpressionAttributeValues={':age': 25}
)
"""


# =============================================================================
# 4. SQS (Simple Queue Service)
# =============================================================================

"""
# SQS 클라이언트
sqs = boto3.client('sqs')

# 큐 생성
response = sqs.create_queue(
    QueueName='my-queue',
    Attributes={'DelaySeconds': '0'}
)
queue_url = response['QueueUrl']

# 메시지 전송
sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Hello, World!',
    MessageAttributes={
        'Author': {
            'StringValue': 'John',
            'DataType': 'String'
        }
    }
)

# 메시지 수신
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=10,
    WaitTimeSeconds=20  # Long polling
)

for message in response.get('Messages', []):
    print(f"Message: {message['Body']}")
    # 처리 후 삭제
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=message['ReceiptHandle']
    )
"""


# =============================================================================
# 5. Lambda
# =============================================================================

"""
# Lambda 클라이언트
lambda_client = boto3.client('lambda')

# 함수 호출
response = lambda_client.invoke(
    FunctionName='my-function',
    InvocationType='RequestResponse',  # 동기 호출
    Payload=json.dumps({'key': 'value'})
)

result = json.loads(response['Payload'].read())

# 비동기 호출
lambda_client.invoke(
    FunctionName='my-function',
    InvocationType='Event',  # 비동기
    Payload=json.dumps({'key': 'value'})
)
"""


# =============================================================================
# 6. Secrets Manager
# =============================================================================

"""
# Secrets Manager 클라이언트
secrets = boto3.client('secretsmanager')

# 시크릿 생성
secrets.create_secret(
    Name='my-secret',
    SecretString=json.dumps({
        'username': 'admin',
        'password': 'secret123'
    })
)

# 시크릿 조회
response = secrets.get_secret_value(SecretId='my-secret')
secret_data = json.loads(response['SecretString'])
"""


def get_secret(secret_name: str, region: str = 'ap-northeast-2') -> dict:
    """AWS Secrets Manager에서 시크릿 조회"""
    import json

    client = boto3.client('secretsmanager', region_name=region)

    try:
        response = client.get_secret_value(SecretId=secret_name)
        return json.loads(response['SecretString'])
    except ClientError as e:
        raise e


# =============================================================================
# 7. EC2
# =============================================================================

"""
# EC2 클라이언트
ec2 = boto3.client('ec2')

# 인스턴스 목록
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance: {instance['InstanceId']} - {instance['State']['Name']}")

# 인스턴스 시작
ec2.start_instances(InstanceIds=['i-1234567890abcdef0'])

# 인스턴스 중지
ec2.stop_instances(InstanceIds=['i-1234567890abcdef0'])

# 인스턴스 생성
response = ec2.run_instances(
    ImageId='ami-0123456789abcdef0',
    InstanceType='t2.micro',
    KeyName='my-key-pair',
    MinCount=1,
    MaxCount=1
)
"""


# =============================================================================
# 8. CloudWatch
# =============================================================================

"""
# CloudWatch 클라이언트
cloudwatch = boto3.client('cloudwatch')

# 커스텀 메트릭 전송
cloudwatch.put_metric_data(
    Namespace='MyApp',
    MetricData=[
        {
            'MetricName': 'RequestCount',
            'Value': 1,
            'Unit': 'Count',
            'Dimensions': [
                {'Name': 'Environment', 'Value': 'Production'}
            ]
        }
    ]
)

# CloudWatch Logs
logs = boto3.client('logs')

# 로그 그룹 생성
logs.create_log_group(logGroupName='/my-app/logs')

# 로그 스트림 생성
logs.create_log_stream(
    logGroupName='/my-app/logs',
    logStreamName='app-stream'
)

# 로그 이벤트 전송
logs.put_log_events(
    logGroupName='/my-app/logs',
    logStreamName='app-stream',
    logEvents=[
        {'timestamp': int(time.time() * 1000), 'message': 'Hello, World!'}
    ]
)
"""


# =============================================================================
# 9. SNS (Simple Notification Service)
# =============================================================================

"""
# SNS 클라이언트
sns = boto3.client('sns')

# 토픽 생성
response = sns.create_topic(Name='my-topic')
topic_arn = response['TopicArn']

# 구독 추가
sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='user@example.com'
)

# 메시지 발행
sns.publish(
    TopicArn=topic_arn,
    Message='Hello, World!',
    Subject='Notification'
)
"""


# =============================================================================
# 10. 실전 예제: FastAPI + AWS
# =============================================================================

"""
# FastAPI와 AWS 통합 예제

from fastapi import FastAPI, UploadFile, HTTPException
import boto3
import uuid

app = FastAPI()
s3 = boto3.client('s3')
BUCKET_NAME = 'my-app-bucket'


@app.post("/upload")
async def upload_file(file: UploadFile):
    # 고유 파일명 생성
    file_key = f"uploads/{uuid.uuid4()}-{file.filename}"

    try:
        s3.upload_fileobj(file.file, BUCKET_NAME, file_key)
        url = s3.generate_presigned_url(
            'get_object',
            Params={'Bucket': BUCKET_NAME, 'Key': file_key},
            ExpiresIn=86400
        )
        return {"url": url, "key": file_key}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/files")
async def list_files():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix='uploads/')
    files = [obj['Key'] for obj in response.get('Contents', [])]
    return {"files": files}
"""


# =============================================================================
# 정리: AWS boto3 핵심
# =============================================================================

"""
주요 AWS 서비스와 boto3:

1. S3 (스토리지)
   - upload_file(), download_file()
   - generate_presigned_url()

2. DynamoDB (NoSQL DB)
   - put_item(), get_item()
   - query(), scan()

3. SQS (메시지 큐)
   - send_message(), receive_message()
   - delete_message()

4. Lambda (서버리스)
   - invoke()

5. Secrets Manager
   - get_secret_value()

6. CloudWatch (모니터링)
   - put_metric_data()

PHP 비교:
- AWS SDK for PHP와 유사한 구조
- boto3가 더 Pythonic한 인터페이스

자격 증명 우선순위:
1. 코드에서 직접 지정
2. 환경 변수
3. ~/.aws/credentials
4. IAM 역할 (EC2, Lambda 등)
"""
