
"""
This is an example DAG which uses the DatabricksSubmitRunOperator.
In this example, we create two tasks which execute sequentially.
The first task is to run a notebook at the workspace path "/test"
and the second task is to run a JAR uploaded to DBFS. Both,
tasks use new clusters.

Because we have set a downstream dependency on the notebook task,
the spark jar task will NOT run until the notebook task completes
successfully.

The definition of a successful run is if the run has a result_state of "SUCCESS".
For more information about the state of a run refer to
https://docs.databricks.com/api/latest/jobs.html#runstate
"""

from datetime import datetime

from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator

with DAG(
    dag_id='example_databricks_operator',
    schedule_interval='@daily',
    start_date=datetime(2021, 1, 1),
    tags=['example'],
    catchup=False,
) as dag:
    # [START howto_operator_databricks_json]
    # Example of using the JSON parameter to initialize the operator.
    new_cluster = {
        'spark_version': '9.1.x-scala2.12',
        'node_type_id': 'Standard_DS3_v2',
        'num_workers': 8,
    }

    notebook_task_params = {
        'new_cluster': new_cluster,
        'notebook_task': {
            'notebook_path': '/Users/sc87291@inetpsa.com/test1',
            "email_notifications": {
                
                "on_start": [ "kamal.lazhar@external.stellantis.com" ],
                "on_success": [ "kamal.lazhar@external.stellantis.com" ],
                "on_failure": []   
            }
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
        spark_jar_task={'main_class_name': 'org.apache.spark.examples.SparkPi',
                        'parameters': '10'
                       },
        libraries=[{'jar': 'dbfs:/FileStore/sparkpi/sparkpi_assembly_0_1.jar'}],
    )
    
    # [END howto_operator_databricks_named]
    notebook_task >> spark_jar_task
