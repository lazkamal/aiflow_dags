import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

dag = DAG(dag_id="dag_test", start_date=airflow.utils.dates.days_ago(3), schedule_interval="@daily")
def test_bash_operator():
    test = BashOperator(task_id="test", bash_command="echo testme", xcom_push=True, dag= dag)
    result = test.execute(context={})
    assert result == "testme"


