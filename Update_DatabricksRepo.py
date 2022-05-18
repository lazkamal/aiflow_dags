from datetime import datetime

from airflow import DAG
from airflow.providers.databricks.operators.databricks_repos import DatabricksReposUpdateOperator

with DAG(
        dag_id='Update_DatabricksRepo',
        schedule_interval='@daily',
        start_date=datetime.now(),
        tags=['example'],
        catchup=False,
) as dag:
    repo_path = "/Repos/sc87291@inetpsa.com/airflow-repo"
    git_url = "https://github.com/lazkamal/dags_2.git"
    create_repo = DatabricksReposUpdateOperator(task_id='update_repo', repo_path=repo_path, branch='main', databricks_conn_id='databricks_default')
