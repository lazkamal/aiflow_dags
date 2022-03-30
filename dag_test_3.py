from airflow.models import DagBag
from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.operators.python import PythonOperator


def test_dagbag():


    dag_bag = DagBag(include_examples=False)
    try:
        assert not dag_bag.import_errors
    except AssertionError as msg:
        print(msg)
    
    # dag = dag_bag.dags['databricks_dag']
    # error_msg = f"databricks_dag in {dag.full_filepath} has no description"
    for dag_id, dag in dag_bag.dags.items():
        m = f"{dag_id} in {dag.full_filepath} has description"
        error_msg = f"{dag_id} in {dag.full_filepath} has no description"
        try:
            assert dag.description, error_msg
    # the errror_message provided by the user gets printed
        except AssertionError as msg:
            print(msg)
            continue
        print(m)


with DAG(
        dag_id="dag_test_3",
        schedule_interval="@daily",
        start_date=days_ago(2),
) as dag:
    run_this = PythonOperator(
        task_id="test",
        python_callable=test_dagbag,
    )





