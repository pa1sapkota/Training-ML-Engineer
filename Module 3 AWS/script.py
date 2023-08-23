import json
import pandas as pd
import urllib3
import boto3
import os
import logging
import psycopg2

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")
s3_key_raw = "raw_data/raw.json"
s3_key_clean = "transformeddata/transformed.csv"

http = urllib3.PoolManager()
url = "https://jsonplaceholder.typicode.com/todos"


conn = psycopg2.connect(
                host=os.environ['host'],
                database=os.environ['dbname'],
                user=os.environ['user'],
                password=os.environ['password']
            )
            
cur = conn.cursor()

def lambda_handler(event, context):
    try:
        response = http.request('GET', url)
        if response.status == 200:
            data = json.loads(response.data.decode('utf-8'))  # Parse JSON response content

            # Writing raw data to raw data bucket
            s3_bucket_raw = "apprentice-training-pawan-ml-dev"
            s3.put_object(Bucket=s3_bucket_raw, Key=s3_key_raw, Body=json.dumps(data))
    
            df = pd.DataFrame(data)
            # Applying Transformations
            transformed_1 = df.drop(columns=['userId'])
            transformed_1.columns = transformed_1.columns.str.upper()
            transformed_2 = transformed_1
            transformed_2['COMPLETED'] = transformed_2['COMPLETED'].astype(int)
            transformed_3 = transformed_2
            
            transformed_csv = transformed_3.to_csv(index=False)
            
            # Writing transformed data to clean data bucket
            s3_bucket_clean = "apprentice-training-pawan-ml-clean"
            s3.put_object(Bucket=s3_bucket_clean, Key=s3_key_clean, Body=transformed_csv)   
            
            logger.info(msg="Dumped cleaned data")
            for index, row in transformed_3.iterrows():
                cur.execute(
                    "INSERT INTO pawan_test_etl (ID, TITLE, COMPLETED) "
                    "VALUES (%s, %s, %s)",
                    (
                        row['ID'],
                        row['TITLE'], 
                        row['COMPLETED']
                    )
                )
    
            conn.commit()
            
    except Exception as e:
        logger.error(msg="Error: " + str(e))
        if conn:
            conn.rollback()
            
    finally:
        if conn:
            conn.close()
    
    return {
        'statusCode': 200,
        'body': "Data Uploaded to S3 and RDS"
    }