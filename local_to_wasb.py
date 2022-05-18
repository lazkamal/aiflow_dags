from datetime import datetime

from airflow import DAG
from airflow.providers.microsoft.azure.transfers.local_to_wasb import LocalFilesystemToWasbOperator

with DAG(
        dag_id='local_to_wasb',
        schedule_interval='@once',
        start_date=datetime.now(),
        tags=['example'],
        catchup=False,
) as dag:
    git_url = "https://github.com/lazkamal/dags_2.git"
    t1 = LocalFilesystemToWasbOperator(task_id='to_wasb',file_path='https://github.com/lazkamal/aiflow_dags/batch_operator.py', container_name='airflow312', blob_name='dags', wasb_conn_id='wasb_default')
