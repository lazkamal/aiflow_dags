from airflow.providers.microsoft.azure.operators.azure_batch import AzureBatchOperator
from airflow.providers.microsoft.azure.batch.models import ResourceFile

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
resource_file= ResourceFile(storage_container_url='https://airflow312.blob.core.windows.net/dags/PRD01__tutorial.py?sp=r&st=2022-05-15T21:50:40Z&se=2022-05-16T05:50:40Z&spr=https&sv=2020-08-04&sr=b&sig=ufrI%2ByNKyFLLmlusJH3TWIyfALHtR%2BkPs6uz89M73Ao%3D')
t1 = AzureBatchOperator(
    task_id='test_batch_operator',
    azure_batch_conn_id='azure_batch_default',
    batch_pool_id='airflow-test-pool',
    batch_pool_vm_size='standard_a2_v2',
    batch_job_id='myJob_test',
    batch_task_command_line= "/bin/bash -c 'printenv | grep AZ_BATCH; sleep 90s'",
    batch_task_id='myTask2',
    vm_publisher='canonical',
    vm_offer='ubuntuserver',
    vm_sku='18.04-lts',
    vm_node_agent_sku_id='batch.node.ubuntu 18.04',
    target_dedicated_nodes=1,
    dag=dag)
