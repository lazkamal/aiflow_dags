import os

from datetime import datetime

from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
DAG_ID = os.path.basename(__file__).replace(".py", "")
DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "email_on_failure": False,
    "email_on_retry": False,
}

with DAG(
    dag_id=DAG_ID,
    description="In this example, we create two tasks which execute sequentially. The first task is to run a notebook at the workspace path '/test' and the second task is to run a JAR uploaded to DBFS",
    schedule_interval='@daily',
    default_args=DEFAULT_ARGS,
    start_date=datetime(2021, 1, 1),
    tags=['databricks Submit Dag'],
    catchup=False,
) as dag:
    # [START howto_operator_databricks_json]
    # Example of using the JSON parameter to initialize the operator.
    new_cluster = {
        'spark_version': '9.1.x-scala2.12',
        'node_type_id': 'r3.xlarge',
        'aws_attributes': {'availability': 'ON_DEMAND'},
        'num_workers': 8,
    }

    notebook_task_params = {
        'new_cluster': new_cluster,
        'notebook_task': {
            'notebook_path': '/Users/airflow@example.com/PrepareData',
        },
    }

    notebook_task = DatabricksSubmitRunOperator(task_id='notebook_task', json=notebook_task_params)
    # [END howto_operator_databricks_json]

    # [START howto_operator_databricks_named]
    # Example of using the named parameters of DatabricksSubmitRunOperator
    # to initialize the operator.
    spark_jar_task = DatabricksSubmitRunOperator(
        task_id='spark_jar_task',
        new_cluster=new_cluster,
        spark_jar_task={'main_class_name': 'com.example.ProcessData'},
        libraries=[{'jar': 'dbfs:/lib/etl-0.1.jar'}],
    )
    # [END howto_operator_databricks_named]
    notebook_task >> spark_jar_task
