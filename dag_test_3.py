from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python import PythonOperator


def test_dagbag():
    dag_bag = DagBag()
    assert not dag_bag.import_errors

with DAG(
    dag_id="dag_test_3",
    schedule_interval="@daily",
    start_date=days_ago(2),
) as dag:
    run_this = PythonOperator(
        task_id="test",
        python_callable=test_dagbag,
    )



