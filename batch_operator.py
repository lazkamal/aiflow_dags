from airflow.providers.microsoft.azure.operators.azure_batch import AzureBatchOperator
from datetime import timedelta, datetime

from airflow import DAG

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime.now() - timedelta(minutes=20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(dag_id='batch_operator',
          default_args=default_args,
          schedule_interval='@daily',
          dagrun_timeout=timedelta(seconds=120))
t1_bash = """
echo 'Hello World'
"""
t1 = AzureBatchOperator(
    task_id='test_batch_operator',
    azure_batch_conn_id='azure_batch_default',
    batch_pool_id='airflow-test-pool',
    batch_pool_vm_size='standard_a2_v2',
    batch_job_id='myJob_test',
    batch_task_command_line="echo 'Hello World'",
    batch_task_id='myTask',
    dag=dag)
