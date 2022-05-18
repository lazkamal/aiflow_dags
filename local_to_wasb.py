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
    repo_path = "/Repos/sc87291@inetpsa.com/airflow-repo"
    git_url = "https://github.com/lazkamal/dags_2.git"
    t1 = LocalFilesystemToWasbOperator(file_path='https://github.com/lazkamal/aiflow_dags/blob/main/batch_operator.py', container_name='airflow312', blob_name='dags', wasb_conn_id='wasb_default')