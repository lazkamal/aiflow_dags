from airflow.providers.microsoft.azure.operators.azure_batch import AzureBatchOperator
from azure.mgmt.batch.models import ResourceFile

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
  
resource_file = ResourceFile(
        storage_container_url='https://airflow312.blob.core.windows.net/dags?sv=2020-08-04&ss=bfqt&srt=co&sp=rwdlacupitfx&se=2022-05-25T16:44:32Z&st=2022-05-16T08:44:32Z&spr=https&sig=laWAbUpNd%2FNGmPMA4PqeVsXjfMPFszCk2gV%2Fl3U7E%2FU%3D',
        file_path='hello_world.py')
t1 = AzureBatchOperator(
        task_id='test_batch_operator',
        azure_batch_conn_id='azure_batch_default',
        batch_pool_id='airflow-test-pool',
        batch_pool_vm_size='standard_a2_v2',
        batch_job_id='myJob_test',
        batch_task_command_line="python3 hello_world.py",
        batch_task_id='myTask4',
        batch_task_resource_files=[resource_file],
        vm_publisher='canonical',
        vm_offer='ubuntuserver',
        vm_sku='18.04-lts',
        vm_node_agent_sku_id='batch.node.ubuntu 18.04',
        target_dedicated_nodes=1,
        dag=dag)
