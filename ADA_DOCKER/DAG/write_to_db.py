"""
Code that goes along with the Airflow tutorial located at:
https://github.com/apache/incubator-airflow/blob/master/airflow/example_dags/tutorial.py
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from minio import Minio
import tempfile
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime
from pathlib import Path

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG(
    'ada', default_args=default_args, schedule_interval=timedelta(days=1))


df = pd.DataFrame([[1,2,5],
                   [4,6,1],
                   [6,6,4]], columns=['A', 'B', 'C'])

minio_client = Minio(
        endpoint='minio1:9000',
        access_key='asd',
        secret_key='asdasdasd',
        secure=False
)

model = LinearRegression()
model.fit(df[['A', 'B']], df['C'])

with tempfile.NamedTemporaryFile() as temp:
    joblib.dump(value=model, filename=temp.name)
    
    minio_client.fput_object(
            bucket_name = 'model',
            object_name = 'linear{}.pkl'.format(datetime.now()),
            file_path = Path(temp.name)
    )