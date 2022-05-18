from datetime import datetime

from airflow import DAG
from airflow.providers.databricks.operators.databricks_repos import DatabricksReposCreateOperator

with DAG(
        dag_id='Create_DatabricksRepo',
        schedule_interval='@daily',
        start_date=datetime.now(),
        tags=['example'],
        catchup=False,
) as dag:
    repo_path = "/Repos/sc87291@inetpsa.com/airflow-repo"
    git_url = "https://github.com/lazkamal/dags_2.git"
    create_repo = DatabricksReposCreateOperator(task_id='create_repo', repo_path=repo_path, git_url=git_url, databricks_conn_id='databricks_default')
