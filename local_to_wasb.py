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
    git_url = "/opt/airflow/dags/repo/ssh_operator.py"
    t1 = LocalFilesystemToWasbOperator(task_id='to_wasb',file_path=git_url, container_name='dags', blob_name='ssh_operator', wasb_conn_id='wasb_default')
