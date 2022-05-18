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
    git_url = "/etc/ssh/ssh_config"
    t1 = LocalFilesystemToWasbOperator(task_id='to_wasb',file_path=git_url, container_name='airflow312', blob_name='dags', wasb_conn_id='wasb_default', create_container=True)
